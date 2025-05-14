import os
import numpy as np
from PIL import Image
import json
import geojson
from datetime import datetime
import ultralytics
from ultralytics import YOLO


model = YOLO("./fq_map/seg_best.pt")

def pixel_to_spatial_coordinates(pixel_x, pixel_y, image_path):
    """
    将图片上的像素坐标转换为空间坐标
    
    参数:
    pixel_x, pixel_y: 图片上的像素坐标
    image_path: 图片路径，文件名包含左上角空间坐标
    
    返回:
    spatial_x, spatial_y: 对应的空间坐标
    """
    # 从图片名称中提取左上角坐标
    image_name = os.path.basename(image_path)
    image_name_without_ext = os.path.splitext(image_name)[0]
    
    # 假设文件名格式为 "x_y.png"
    coords = image_name_without_ext.split('_')
    if len(coords) < 2:
        raise ValueError(f"图片名称格式不正确: {image_name}")
    
    try:
        top_left_x = int(coords[0])*0.01
        top_left_y = int(coords[1])*0.01
    except ValueError:
        raise ValueError(f"无法从图片名称中提取坐标: {image_name}")
    
    # 获取图片尺寸
    with Image.open(image_path) as img:
        img_width, img_height = img.size
    
    # 计算每个像素对应的实际距离（米）
    # 假设图片覆盖20×20米的区域
    meters_per_pixel_x = 20.0 / img_width
    meters_per_pixel_y = 20.0 / img_height
    
    # 计算空间坐标
    # 注意：像素坐标系原点在左上角，y轴向下，而空间坐标系通常y轴向上
    spatial_x = top_left_x + pixel_x * meters_per_pixel_x
    spatial_y = top_left_y - pixel_y * meters_per_pixel_y  # 减法是因为y轴方向相反
    
    return spatial_x, spatial_y

def convert_boundary_to_spatial(boundary_pixels, image_path):
    """
    将图片上的边界点转换为空间坐标
    
    参数:
    boundary_pixels: 边界点的像素坐标列表，格式为 [(x1,y1), (x2,y2), ...]
    image_path: 图片路径
    
    返回:
    空间坐标列表，格式为 [(x1,y1), (x2,y2), ...]
    """
    spatial_coords = []
    
    for px, py in boundary_pixels:
        sx, sy = pixel_to_spatial_coordinates(px, py, image_path)
        spatial_coords.append((sx, sy))
    
    return spatial_coords

def save_to_geojson(results, output_path):
    """
    将边界结果保存为GeoJSON格式
    
    参数:
    results: 包含边界信息的结果列表
    output_path: 输出文件路径
    """
    features = []
    
    for result in results:
        # 获取空间边界坐标
        spatial_boundary = result["spatial_boundary"]
        
        # 确保多边形闭合（首尾点相同）
        if spatial_boundary[0] != spatial_boundary[-1]:
            spatial_boundary.append(spatial_boundary[0])
        
        # 创建GeoJSON多边形
        polygon = geojson.Polygon([spatial_boundary])
        
        # 创建要素，包含属性信息
        feature = geojson.Feature(
            geometry=polygon,
            properties={
                "image": result["image"],
                "state": result["state"],
                "timestamp": datetime.now().isoformat()
            }
        )
        
        features.append(feature)
    
    # 创建要素集合
    feature_collection = geojson.FeatureCollection(features)
    
    # 保存到文件
    with open(output_path, 'w', encoding='utf-8') as f:
        geojson.dump(feature_collection, f, ensure_ascii=False, indent=4)
    
    print(f"GeoJSON已保存到: {output_path}")

def process_images_in_directory():
    """处理fq_map/pic目录下的所有图片，转换边界坐标"""
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pic_dir = os.path.join(current_dir, "fq_map", "pic")
    
    if not os.path.exists(pic_dir):
        print(f"错误：目录不存在: {pic_dir}")
        return
    
    # 示例：假设您已经提取了边界点
    # 这里需要替换为您实际的边界点提取逻辑
    
    sample_boundary = [(100, 100), (200, 100), (200, 200), (100, 200)]  # 示例边界点
    
    results = []
    
    # 处理目录中的所有图片
    for filename in os.listdir(pic_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(pic_dir, filename)
            
            results_model = model(image_path)
            # 0 泡沫 1 塑料
            box_cls = results_model[0].boxes.cls.cpu().numpy().tolist()

            #列号 行号 列号 行号
            box_xy = results_model[0].boxes.xyxy.cpu().numpy().tolist()
            
            #遍历每一个矩形
            for i in range(len(box_cls)):
                local = box_xy[i] #矩形左上角和右下角坐标
                boundary_pixels = [(local[0], local[1]),(local[2], local[1]), (local[2], local[3]),(local[0], local[3])] #矩形四个顶点像素坐标
                spatial_boundary = convert_boundary_to_spatial(boundary_pixels, image_path)

                results.append({
                    "image": filename,
                    "state": int(box_cls[i]),
                    "pixel_boundary": boundary_pixels,
                    "spatial_boundary": spatial_boundary
                })

                    
            
            #使用opencv绘制到图片上
            # import cv2
            # img = cv2.imread(image_path)
            # for i in range(len(box_cls)):
            #     if box_cls[i] == 1:
            #         cv2.rectangle(img, (int(box_xy[i][0]), int(box_xy[i][1])), (int(box_xy[i][2]), int(box_xy[i][3])), (0, 255, 0), 2)
            # cv2.imwrite("draw_"+filename, img)
            
            # 这里应该是您提取边界的代码
            # boundary_pixels = extract_boundary(image_path)
            #boundary_pixels = sample_boundary  # 使用示例边界点
            
            # 转换为空间坐标
            #spatial_boundary = convert_boundary_to_spatial(boundary_pixels, image_path)
            
            # print(f"图片: {filename}")
            # print(f"像素边界: {boundary_pixels}")
            # print(f"空间边界: {spatial_boundary}")
            # print("-" * 50)
            
            # results.append({
            #     "image": filename,
            #     "state": "塑料",
            #     "pixel_boundary": boundary_pixels,
            #     "spatial_boundary": spatial_boundary
            # })
    
    return results

if __name__ == "__main__":
    results = process_images_in_directory()
    print(f"处理完成，共处理了 {len(results) if results else 0} 张图片")
    
    if results:
        # 创建输出目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_dir, "output")
        os.makedirs(output_dir, exist_ok=True)
        
        # 保存为GeoJSON
        geojson_path = os.path.join(output_dir, "boundaries.geojson")
        save_to_geojson(results, geojson_path)