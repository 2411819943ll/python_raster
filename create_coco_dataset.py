import os
import json
import shutil
from datetime import datetime
import glob

def create_coco_dataset():
    """
    将qk_01文件夹下的json和图片整理为标准COCO数据集格式
    参考org_dataset文件夹结构
    处理三个类别：浮球、新鱼排、旧鱼排
    """
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 源数据目录
    source_dir = os.path.join(current_dir, "qk_01")
    
    # 目标数据集目录
    target_dir = os.path.join(current_dir, "coco_dataset")
    
    # 创建目标目录结构
    images_dir = os.path.join(target_dir, "images")
    annotations_dir = os.path.join(target_dir, "annotations")
    labels_dir = os.path.join(target_dir, "labels")  # 添加YOLO格式标签目录
    
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(annotations_dir, exist_ok=True)
    os.makedirs(labels_dir, exist_ok=True)  # 创建YOLO标签目录
    
    # 定义类别
    categories = [
        {"id": 1, "name": "浮球", "supercategory": "marine"},
        {"id": 2, "name": "新鱼排", "supercategory": "marine"},
        {"id": 3, "name": "旧鱼排", "supercategory": "marine"}
    ]
    
    # 初始化COCO格式数据
    coco_data = {
        "info": {
            "description": "Marine Objects Dataset",
            "url": "",
            "version": "1.0",
            "year": datetime.now().year,
            "contributor": "",
            "date_created": datetime.now().strftime("%Y-%m-%d")
        },
        "licenses": [
            {
                "id": 1,
                "name": "Unknown",
                "url": ""
            }
        ],
        "images": [],
        "annotations": [],
        "categories": categories
    }
    
    # 获取所有json文件
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    
    # 类别名称到ID的映射
    category_map = {
        '3':"浮球",
        '2':"新鱼排",
        '1':"旧鱼排"
    }
    
    image_id = 1
    annotation_id = 1
    
    # 处理每个json文件
    for json_file in json_files:
        base_name = os.path.basename(json_file)
        image_name = base_name.replace(".json", ".jpg")  # 假设图片是jpg格式
        
        # 如果不是jpg，尝试其他格式
        if not os.path.exists(os.path.join(source_dir, image_name)):
            image_name = base_name.replace(".json", ".png")
        
        if not os.path.exists(os.path.join(source_dir, image_name)):
            print(f"警告：找不到对应的图片文件：{base_name}")
            continue
        
        # 复制图片到目标目录
        source_image = os.path.join(source_dir, image_name)
        target_image = os.path.join(images_dir, image_name)
        shutil.copy2(source_image, target_image)
        
        # 读取json文件
        with open(json_file, 'r', encoding='utf-8') as f:
            try:
                source_data = json.load(f)
            except json.JSONDecodeError:
                print(f"错误：无法解析JSON文件：{json_file}")
                continue
        
        # 获取图片信息
        try:
            from PIL import Image
            img = Image.open(source_image)
            width, height = img.size
        except Exception as e:
            print(f"错误：无法获取图片尺寸：{source_image}, {str(e)}")
            width, height = 0, 0
        
        # 添加图片信息
        image_info = {
            "id": image_id,
            "file_name": image_name,
            "width": width,
            "height": height,
            "date_captured": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "license": 1,
            "coco_url": "",
            "flickr_url": ""
        }
        
        coco_data["images"].append(image_info)
        
        # 为YOLO格式标注创建txt文件
        txt_filename = os.path.splitext(image_name)[0] + ".txt"
        txt_filepath = os.path.join(labels_dir, txt_filename)
        iddict = {'2':2, '0':0, '1':1}
        # 处理标注信息
        if isinstance(source_data, dict) and "shapes" in source_data:
            # 打开txt文件用于写入YOLO格式标注
            with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
                # labelme格式
                for shape in source_data["shapes"]:
                    id = shape["label"]
                    points = shape["points"]
                    print(f"label: {id}, points: {points}")
                    # 
                    
                    # 确定类别ID
                    category_id = iddict[id]

                    
                    # 计算边界框
                    x_coords = [p[0] for p in points]
                    y_coords = [p[1] for p in points]
                    
                    x_min = min(x_coords)
                    y_min = min(y_coords)
                    box_width = max(x_coords) - x_min
                    box_height = max(y_coords) - y_min
                    
                    # 创建COCO格式的标注
                    annotation = {
                        "id": annotation_id,
                        "image_id": image_id,
                        "category_id": category_id,
                        "bbox": [x_min, y_min, box_width, box_height],
                        "area": box_width * box_height,
                        "segmentation": [sum([[p[0], p[1]] for p in points], [])],
                        "iscrowd": 0
                    }
                    
                    coco_data["annotations"].append(annotation)
                    annotation_id += 1
                    
                    # 写入YOLO格式标注 <class-index> <x1> <y1> <x2> <y2> ... <xn> <yn>
                    # 注意：YOLO格式的类别索引从0开始，而COCO从1开始
                    yolo_class_index = int(category_id)
                    
                    # 构建YOLO格式的标注行
                    yolo_line = f"{yolo_class_index}"
                    for x, y in points:
                        # 将坐标归一化到[0,1]范围
                        norm_x = x / width if width > 0 else 0
                        norm_y = y / height if height > 0 else 0
                        yolo_line += f" {norm_x} {norm_y}"
                    
                    # 写入txt文件
                    txt_file.write(yolo_line + "\n")
        else:
            # 尝试其他可能的格式
            print(f"警告：未识别的JSON格式：{json_file}")
        
        image_id += 1
    
    # 保存COCO格式的标注文件
    with open(os.path.join(annotations_dir, "instances.json"), 'w', encoding='utf-8') as f:
        json.dump(coco_data, f, ensure_ascii=False, indent=4)
    
    print(f"数据集创建完成！")
    print(f"图片数量：{len(coco_data['images'])}")
    print(f"标注数量：{len(coco_data['annotations'])}")
    print(f"类别数量：{len(coco_data['categories'])}")
    print(f"数据集保存在：{target_dir}")
    print(f"YOLO格式标注保存在：{labels_dir}")

if __name__ == "__main__":
    create_coco_dataset()