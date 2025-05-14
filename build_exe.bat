@echo off
echo 正在准备打包TIFF切片工具...

:: 创建临时目录
if not exist upx_temp mkdir upx_temp
cd upx_temp

:: 下载UPX压缩工具
echo 正在下载UPX压缩工具...
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/upx/upx/releases/download/v4.2.2/upx-4.2.2-win64.zip' -OutFile 'upx.zip'"

:: 解压UPX
echo 正在解压UPX...
powershell -Command "Expand-Archive -Path 'upx.zip' -DestinationPath './' -Force"

:: 返回上级目录
cd ..

:: 使用PyInstaller打包应用程序
echo 正在使用PyInstaller打包应用程序...
pyinstaller --clean --upx-dir=upx_temp/upx-4.2.2-win64 tiff_splitter_gui.spec

:: 清理临时文件
echo 正在清理临时文件...
rd /s /q upx_temp
rd /s /q build

echo 打包完成！可执行文件位于dist目录中。
pause