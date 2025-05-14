import os
import numpy as np
import rasterio
from rasterio.windows import Window
from PIL import Image
import json
from shapely.geometry import shape, box, Polygon
from shapely.ops import unary_union

def read_tfw_file(tfw_path):
    """读取TFW文件，获取地理参考信息"""
    with open(tfw_path, 'r') as f:
        lines = f.readlines()
    
    # TFW文件格式：
    # 行1：x方向像素分辨率（像素宽度）
    # 行2：行旋转项（通常为0）
    # 行3：列旋转项（通常为0）
    # 行4：y方向像素分辨率（像素高度，通常为负值）
    # 行5：左上角x坐标
    # 行6：左上角y坐标
    
    x_pixel_size = float(lines[0].strip())
    y_pixel_size = float(lines[3].strip())  # 通常为负值
    top_left_x = float(lines[4].strip())
    top_left_y = float(lines[5].strip())
    
    return x_pixel_size, y_pixel_size, top_left_x, top_left_y

def process_tiff_file(tiff_path, output_dir, cell_size_meters=100, reference_coords=None, shared_polygon_union=None):
    """处理TIFF文件，按照指定的单元大小进行切割"""
    # 导入线程池模块
    from concurrent.futures import ThreadPoolExecutor
    import threading
    
    # 获取对应的TFW文件路径
    tfw_path = tiff_path.replace('.tif', '.tfw')
    
    if not os.path.exists(tfw_path):
        print(f"错误：找不到对应的TFW文件：{tfw_path}")
        return
    
    # 读取TFW文件获取地理参考信息
    x_pixel_size, y_pixel_size, top_left_x, top_left_y = read_tfw_file(tfw_path)
    
    # 如果提供了参考坐标，则进行对齐调整
    if reference_coords is not None:
        ref_x, ref_y = reference_coords
        # 计算调整量，使当前TIFF的左上角坐标与参考坐标对齐
        # 调整为最接近的网格点
        x_adjust = ref_x - top_left_x
        y_adjust = ref_y -  top_left_y
        
        # 应用调整
        if abs(x_adjust)>0.1 or abs(y_adjust)>0.1:
            print(f"警告：当前TIFF文件的左上角坐标与参考坐标不匹配，将进行对齐调整")
        print(f"当前左上角坐标：({top_left_x}, {top_left_y})")
        print(f"参考坐标：({ref_x}, {ref_y})")
        top_left_x = top_left_x + x_adjust
        top_left_y = top_left_y + y_adjust
        
        print(f"坐标已对齐，调整后的左上角坐标：({top_left_x}, {top_left_y})")

    
    # 使用共享的polygon_union对象或者读取geojson文件
    polygons = []
    polygon_union = None
    spatial_index = None
    
    # 如果提供了共享的polygon_union对象，则直接使用
    if shared_polygon_union is not None:
        polygon_union = shared_polygon_union
        print("使用共享的多边形并集进行相交判断")
    # 计算每个单元格对应的像素数
    # 像素大小为正值进行计算 cell_size_meters 图像单元大小
    cell_size_pixels_x = cell_size_meters / abs(x_pixel_size)
    cell_size_pixels_y = cell_size_meters / abs(y_pixel_size)
    # 打开TIFF文件
    with rasterio.open(tiff_path) as src:
        # 获取影像的元数据
        width = src.width
        height = src.height
        
        # 计算需要切割的行数和列数
        num_cols = int(width/ cell_size_pixels_x)
        num_rows = int(height/ cell_size_pixels_y)
        
        # 创建输出目录
        tiff_name = os.path.basename(tiff_path).replace('.tif', '')
        tiff_output_dir = os.path.join(output_dir, tiff_name)
        os.makedirs(tiff_output_dir, exist_ok=True)
        
        print(f"处理文件：{tiff_path}")
        print(f"像素分辨率：x={x_pixel_size}, y={y_pixel_size}")
        print(f"左上角坐标：({top_left_x}, {top_left_y})")
        print(f"影像大小：{width}x{height} 像素")
        print(f"切割单元大小：{cell_size_meters}x{cell_size_meters} 米 ({cell_size_pixels_x}x{cell_size_pixels_y} 像素)")
        print(f"将生成 {num_rows}x{num_cols} 个切片")
        
        # 定义处理单个切片的函数
        def process_tile(row, col):
            # 计算当前单元格的窗口位置
            window_col_off = col * cell_size_pixels_x
            window_row_off = row * cell_size_pixels_y
            
            # 确保窗口不超出影像边界
            window_width = min(cell_size_pixels_x, width - window_col_off)
            window_height = min(cell_size_pixels_y, height - window_row_off)
            
            if window_width <= 0 or window_height <= 0:
                return
            
            # 计算当前单元格左上角的地理坐标
            cell_top_left_x = top_left_x + window_col_off * x_pixel_size
            cell_top_left_y = top_left_y + window_row_off * y_pixel_size
            
            #cell_size_meters 推算出右下角坐标
            cell_bottom_right_x = cell_top_left_x + cell_size_meters
            cell_bottom_right_y = cell_top_left_y - cell_size_meters
            
            # 创建当前窗口的地理边界框
            cell_bbox = box(cell_top_left_x, cell_bottom_right_y, cell_bottom_right_x, cell_top_left_y)
            
            # 检查是否与任何多边形相交
            intersects = False
            if not polygon_union:
                intersects = True
            # 方法1：使用多边形并集进行一次相交判断
            elif polygon_union is not None:
                intersects = cell_bbox.intersects(polygon_union)
            # 方法2：使用空间索引进行快速相交判断
            elif spatial_index is not None:
                # 查询可能相交的多边形
                potential_matches = spatial_index.query(cell_bbox)
                # 检查是否有任何一个多边形与当前单元格相交
                for i in potential_matches:
                    if cell_bbox.intersects(polygons[i]):
                        intersects = True
                        break
            # 方法3：常规方法，遍历所有多边形
            else:
                for polygon in polygons:
                    if cell_bbox.intersects(polygon):
                        intersects = True
                        break
            
            # 如果不相交，跳过此窗口
            if not intersects:
                return
            
            # 使用线程锁确保rasterio读取操作的线程安全
            with rasterio_lock:
                # 读取当前窗口的数据
                window = Window(window_col_off, window_row_off, window_width, window_height)
                data = src.read(indexes=[1, 2, 3], window=window)
            
            # 创建一个1024x1024的空白图像
            output_size = (1024, 1024)
            if len(data.shape) == 3 and data.shape[0] == 3:  # RGB图像
                img = Image.new('RGB', output_size, (0, 0, 0))
                # 将数据调整为PIL可用的格式并粘贴到空白图像上
                temp_img = Image.fromarray(np.transpose(data, (1, 2, 0)).astype(np.uint8))
                temp_img = temp_img.resize(output_size)
                img.paste(temp_img, (0, 0))
            else:  # 单波段图像
                img = Image.new('L', output_size, 0)
                # 如果是单波段，取第一个波段
                temp_img = Image.fromarray(data[0].astype(np.uint8))
                temp_img = temp_img.resize(output_size)
                img.paste(temp_img, (0, 0))
            
            # 生成输出文件名，包含左上角坐标信息
            output_filename = f"{int(cell_top_left_x)}_{int(cell_top_left_y)}.png"
            output_path = os.path.join(tiff_output_dir, output_filename)
            
            # 保存图像
            img.save(output_path)
        
        # 创建线程锁，用于保护rasterio的读取操作
        rasterio_lock = threading.Lock()
        
        # 创建线程池
        # 根据CPU核心数确定线程池大小，但不超过16个线程
        max_workers = min(4, os.cpu_count())
        print(f"创建线程池，线程数：{max_workers}")
        
        # 创建任务列表
        tasks = []
        for row in range(num_rows):
            for col in range(num_cols):
                tasks.append((row, col))
        
        # 使用线程池并行处理切片
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交所有任务到线程池
            futures = [executor.submit(process_tile, row, col) for row, col in tasks]
            
            # 创建进度计数器和锁
            completed = 0
            total = len(tasks)
            progress_lock = threading.Lock()
            
            # 定义回调函数来更新进度
            def update_progress(future):
                nonlocal completed
                with progress_lock:
                    completed += 1
                    if completed % 100 == 0 or completed == total:  # 每处理10个切片或处理完成时更新一次进度
                        percent = (completed / total) * 100
                        print(f"处理进度: {completed}/{total} ({percent:.1f}%)")
            
            # 为每个future添加完成回调
            for future in futures:
                future.add_done_callback(update_progress)
            
            # 等待所有任务完成
            for future in futures:
                try:
                    future.result()  # 获取结果，如果有异常会在这里抛出
                except Exception as e:
                    print(f"处理切片时发生错误: {e}")
                    # 继续处理其他切片
                
        print(f"处理完成，结果保存在：{tiff_output_dir}")

def process_tiff_folder(input_dir, output_dir=None, cell_size_meters=256, geojson_path=None):
    """处理指定文件夹中的所有TIFF文件，并进行坐标对齐和多进程处理"""
    import multiprocessing as mp
    
    # 如果未指定输出目录，则使用默认输出目录
    if output_dir is None:
        # 获取当前脚本所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_dir, "output")
    
    # 创建输出目录
    #判断output_dir是否存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    # 查找目录下的所有TIFF文件
    tiff_files = []
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.tif'):
            tiff_path = os.path.join(input_dir, filename)
            tiff_files.append(tiff_path)
    
    if not tiff_files:
        print(f"错误：在目录 {input_dir} 中未找到TIFF文件")
        return
    
    # 获取第一个TIFF文件的左上角坐标作为参考
    reference_tiff = tiff_files[0]
    reference_tfw = reference_tiff.replace('.tif', '.tfw')
    
    if not os.path.exists(reference_tfw):
        print(f"错误：找不到参考TIFF文件的TFW文件：{reference_tfw}")
        return
    
    _, _, ref_x, ref_y = read_tfw_file(reference_tfw)
    reference_coords = (ref_x, ref_y)
    print(f"使用参考坐标：({ref_x}, {ref_y})进行对齐")
    
    # 在主进程中读取GeoJSON文件并创建polygon_union
    shared_polygon_union = None
    if geojson_path and os.path.exists(geojson_path):
        try:
            print(f"正在读取GeoJSON文件：{geojson_path}")
            with open(geojson_path, 'r', encoding='utf-8') as f:
                geojson_data = json.load(f)
            
            # 提取所有多边形要素
            polygons = []
            if 'features' in geojson_data:
                for feature in geojson_data['features']:
                    for ring in feature['geometry']['rings']:
                        # 将GeoJSON几何要素转换为shapely对象
                        polygons.append(Polygon(ring))
            
            print(f"成功加载 {len(polygons)} 个多边形要素")
            
            # 创建多边形并集
            if polygons:
                try:
                    shared_polygon_union = unary_union(polygons)
                    print("已在主进程中创建多边形并集，将共享给所有子进程")
                except Exception as e:
                    print(f"创建多边形并集失败：{e}，每个进程将单独处理GeoJSON文件")
        except Exception as e:
            print(f"读取GeoJSON文件失败：{e}，每个进程将单独处理GeoJSON文件")
    
    # 创建进程池
    processes = []
    
    # 为每个TIFF文件创建一个处理进程
    for tiff_path in tiff_files:
        # 创建一个新进程来处理TIFF文件
        p = mp.Process(
            target=process_tiff_file, 
            args=(tiff_path, output_dir, cell_size_meters, reference_coords, shared_polygon_union)
        )
        processes.append(p)
        p.start()
        print(f"已启动进程处理文件：{tiff_path}")
    
    # 等待所有进程完成
    for p in processes:
        p.join()
    
    print("所有TIFF文件处理完成！")

def main():
    import argparse
    
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='TIFF文件切片工具')
    parser.add_argument('--input_dir', type=str,default=r'D:\ai\data\nan_2024\longwen', help='输入TIFF文件所在目录路径')
    parser.add_argument('--output_dir', type=str,default=r'D:\ai\data\nan_2024\output', help='输出切片文件的目录路径')
    parser.add_argument('--cell_size', type=int, default=256, help='切片单元大小（米），默认为256')
    parser.add_argument('--geojson_path', type=str,default=r'D:\ai\data\龙文-g\longwen.json', help='GeoJSON文件路径，用于限定处理区域')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 如果未提供输入目录，则使用当前目录
    if args.input_dir is None:
        args.input_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"未指定输入目录，使用当前目录：{args.input_dir}")
    
    # 处理指定目录中的TIFF文件
    process_tiff_folder(args.input_dir, args.output_dir, args.cell_size, args.geojson_path)

if __name__ == "__main__":
    main()