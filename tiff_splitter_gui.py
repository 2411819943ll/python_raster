import os
import sys
import time
import traceback
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QFileDialog, QTextEdit,
                             QSpinBox, QProgressBar, QMessageBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
import tiff_splitter

# 创建一个工作线程类，用于在后台处理TIFF文件
class TiffProcessingThread(QThread):
    # 定义信号
    update_log = pyqtSignal(str)
    processing_finished = pyqtSignal(bool, str)
    progress_update = pyqtSignal(int, int)  # 当前处理的文件索引, 总文件数
    
    def __init__(self, input_dir, output_dir, cell_size, geojson_path):
        super().__init__()
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.cell_size = cell_size
        self.geojson_path = geojson_path
        self.is_running = True
    
    def run(self):
        try:
            # 重定向标准输出到自定义函数
            self._redirect_output()
            
            # 查找目录下的所有TIFF文件
            tiff_files = []
            for filename in os.listdir(self.input_dir):
                if filename.lower().endswith('.tif'):
                    tiff_path = os.path.join(self.input_dir, filename)
                    tiff_files.append(tiff_path)
            
            if not tiff_files:
                self.update_log.emit(f"错误：在目录 {self.input_dir} 中未找到TIFF文件")
                self.processing_finished.emit(False, "未找到TIFF文件")
                return
            
            # 获取第一个TIFF文件的左上角坐标作为参考
            reference_tiff = tiff_files[0]
            reference_tfw = reference_tiff.replace('.tif', '.tfw')
            
            if not os.path.exists(reference_tfw):
                self.update_log.emit(f"错误：找不到参考TIFF文件的TFW文件：{reference_tfw}")
                self.processing_finished.emit(False, "找不到TFW文件")
                return
            
            _, _, ref_x, ref_y = tiff_splitter.read_tfw_file(reference_tfw)
            reference_coords = (ref_x, ref_y)
            self.update_log.emit(f"使用参考坐标：({ref_x}, {ref_y})进行对齐")
            
            # 在主线程中读取GeoJSON文件并创建polygon_union
            shared_polygon_union = None
            if self.geojson_path and os.path.exists(self.geojson_path):
                try:
                    self.update_log.emit(f"正在读取GeoJSON文件：{self.geojson_path}")
                    import json
                    from shapely.geometry import Polygon
                    from shapely.ops import unary_union
                    
                    with open(self.geojson_path, 'r', encoding='utf-8') as f:
                        geojson_data = json.load(f)
                    
                    # 提取所有多边形要素
                    polygons = []
                    if 'features' in geojson_data:
                        for feature in geojson_data['features']:
                            for ring in feature['geometry']['rings']:
                                # 将GeoJSON几何要素转换为shapely对象
                                polygons.append(Polygon(ring))
                    
                    self.update_log.emit(f"成功加载 {len(polygons)} 个多边形要素")
                    
                    # 创建多边形并集
                    if polygons:
                        try:
                            shared_polygon_union = unary_union(polygons)
                            self.update_log.emit("已创建多边形并集，将用于处理所有TIFF文件")
                        except Exception as e:
                            self.update_log.emit(f"创建多边形并集失败：{e}，将单独处理每个TIFF文件")
                except Exception as e:
                    self.update_log.emit(f"读取GeoJSON文件失败：{e}，将单独处理每个TIFF文件")
            
            # 创建输出目录
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir, exist_ok=True)
            
            # 逐个处理TIFF文件
            for i, tiff_path in enumerate(tiff_files):
                if not self.is_running:
                    self.update_log.emit("处理已取消")
                    self.processing_finished.emit(False, "处理已取消")
                    return
                
                self.update_log.emit(f"\n开始处理文件 {i+1}/{len(tiff_files)}: {tiff_path}")
                self.progress_update.emit(i+1, len(tiff_files))
                
                # 处理单个TIFF文件
                tiff_splitter.process_tiff_file(
                    tiff_path, 
                    self.output_dir, 
                    self.cell_size, 
                    reference_coords, 
                    shared_polygon_union
                )
            
            self.update_log.emit("\n所有TIFF文件处理完成！")
            self.processing_finished.emit(True, "处理完成")
            
        except Exception as e:
            error_msg = f"处理过程中发生错误：{str(e)}\n{traceback.format_exc()}"
            self.update_log.emit(error_msg)
            self.processing_finished.emit(False, error_msg)
    
    def _redirect_output(self):
        """重定向标准输出到信号"""
        class StdoutRedirector:
            def __init__(self, signal_func):
                self.signal_func = signal_func
                self.buffer = ""
            
            def write(self, text):
                self.buffer += text
                if '\n' in self.buffer:
                    lines = self.buffer.split('\n')
                    for line in lines[:-1]:
                        self.signal_func(line)
                    self.buffer = lines[-1]
            
            def flush(self):
                if self.buffer:
                    self.signal_func(self.buffer)
                    self.buffer = ""
        
        self.old_stdout = sys.stdout
        sys.stdout = StdoutRedirector(self.update_log.emit)
    
    def stop(self):
        """停止处理"""
        self.is_running = False
        self.update_log.emit("正在停止处理...")

# 主窗口类
class TiffSplitterGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.processing_thread = None
    
    def init_ui(self):
        # 设置窗口标题和大小
        self.setWindowTitle('TIFF文件切片工具')
        self.setGeometry(100, 100, 800, 600)
        
        # 创建中央部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # 输入目录选择
        input_layout = QHBoxLayout()
        input_label = QLabel('输入目录:')
        self.input_dir_edit = QLineEdit()
        self.input_dir_edit.setReadOnly(True)
        input_browse_btn = QPushButton('浏览...')
        input_browse_btn.clicked.connect(self.browse_input_dir)
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_dir_edit)
        input_layout.addWidget(input_browse_btn)
        main_layout.addLayout(input_layout)
        
        # 输出目录选择
        output_layout = QHBoxLayout()
        output_label = QLabel('输出目录:')
        self.output_dir_edit = QLineEdit()
        self.output_dir_edit.setReadOnly(True)
        output_browse_btn = QPushButton('浏览...')
        output_browse_btn.clicked.connect(self.browse_output_dir)
        output_layout.addWidget(output_label)
        output_layout.addWidget(self.output_dir_edit)
        output_layout.addWidget(output_browse_btn)
        main_layout.addLayout(output_layout)
        
        # GeoJSON文件选择
        geojson_layout = QHBoxLayout()
        geojson_label = QLabel('GeoJSON文件:')
        self.geojson_path_edit = QLineEdit()
        self.geojson_path_edit.setReadOnly(True)
        geojson_browse_btn = QPushButton('浏览...')
        geojson_browse_btn.clicked.connect(self.browse_geojson_file)
        geojson_layout.addWidget(geojson_label)
        geojson_layout.addWidget(self.geojson_path_edit)
        geojson_layout.addWidget(geojson_browse_btn)
        main_layout.addLayout(geojson_layout)
        
        # 单元格大小设置
        cell_size_layout = QHBoxLayout()
        cell_size_label = QLabel('切片单元大小(米):')
        self.cell_size_spinbox = QSpinBox()
        self.cell_size_spinbox.setRange(1, 10000)
        self.cell_size_spinbox.setValue(256)
        cell_size_layout.addWidget(cell_size_label)
        cell_size_layout.addWidget(self.cell_size_spinbox)
        cell_size_layout.addStretch()
        main_layout.addLayout(cell_size_layout)
        
        # 进度条
        progress_layout = QHBoxLayout()
        progress_label = QLabel('处理进度:')
        self.progress_bar = QProgressBar()
        progress_layout.addWidget(progress_label)
        progress_layout.addWidget(self.progress_bar)
        main_layout.addLayout(progress_layout)
        
        # 日志显示区域
        log_label = QLabel('处理日志:')
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        main_layout.addWidget(log_label)
        main_layout.addWidget(self.log_text)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        self.start_btn = QPushButton('开始处理')
        self.start_btn.clicked.connect(self.start_processing)
        self.stop_btn = QPushButton('停止处理')
        self.stop_btn.clicked.connect(self.stop_processing)
        self.stop_btn.setEnabled(False)
        button_layout.addStretch()
        button_layout.addWidget(self.start_btn)
        button_layout.addWidget(self.stop_btn)
        main_layout.addLayout(button_layout)
    
    def browse_input_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, '选择输入目录')
        if dir_path:
            self.input_dir_edit.setText(dir_path)
    
    def browse_output_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, '选择输出目录')
        if dir_path:
            self.output_dir_edit.setText(dir_path)
    
    def browse_geojson_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择GeoJSON文件', '', 'GeoJSON文件 (*.json *.geojson)')
        if file_path:
            self.geojson_path_edit.setText(file_path)
    
    def start_processing(self):
        # 检查输入参数
        input_dir = self.input_dir_edit.text()
        if not input_dir or not os.path.exists(input_dir):
            QMessageBox.warning(self, '警告', '请选择有效的输入目录')
            return
        
        output_dir = self.output_dir_edit.text()
        if not output_dir:
            QMessageBox.warning(self, '警告', '请选择输出目录')
            return
        
        geojson_path = self.geojson_path_edit.text()
        if geojson_path and not os.path.exists(geojson_path):
            QMessageBox.warning(self, '警告', '指定的GeoJSON文件不存在')
            return
        
        cell_size = self.cell_size_spinbox.value()
        
        # 清空日志
        self.log_text.clear()
        self.append_log(f"开始处理TIFF文件\n输入目录: {input_dir}\n输出目录: {output_dir}\n单元格大小: {cell_size}米")
        if geojson_path:
            self.append_log(f"GeoJSON文件: {geojson_path}")
        
        # 创建并启动处理线程
        self.processing_thread = TiffProcessingThread(input_dir, output_dir, cell_size, geojson_path)
        self.processing_thread.update_log.connect(self.append_log)
        self.processing_thread.processing_finished.connect(self.on_processing_finished)
        self.processing_thread.progress_update.connect(self.update_progress)
        self.processing_thread.start()
        
        # 更新UI状态
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.progress_bar.setValue(0)
    
    def stop_processing(self):
        if self.processing_thread and self.processing_thread.isRunning():
            self.processing_thread.stop()
            self.append_log("正在停止处理...")
    
    @pyqtSlot(str)
    def append_log(self, text):
        self.log_text.append(text)
        # 滚动到底部
        cursor = self.log_text.textCursor()
        cursor.movePosition(cursor.End)
        self.log_text.setTextCursor(cursor)
    
    @pyqtSlot(bool, str)
    def on_processing_finished(self, success, message):
        # 更新UI状态
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        
        if success:
            QMessageBox.information(self, '完成', '所有TIFF文件处理完成！')
        else:
            QMessageBox.warning(self, '错误', f'处理过程中发生错误：{message}')
    
    @pyqtSlot(int, int)
    def update_progress(self, current, total):
        progress = int((current / total) * 100) if total > 0 else 0
        self.progress_bar.setValue(progress)

def main():
    app = QApplication(sys.argv)
    window = TiffSplitterGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()