from ultralytics import YOLO
from glob import glob
import cv2
from datetime import  datetime
import os

# 加载训练好的模型
def process_detection(result):
    """
    处理目标检测信息，根据指定的类别输出信息

    参数：
    det: 包含目标检测信息的变量，通常包括位置信息、置信度和类别信息等
    specified_class: 指定的类别信息，当检测到该类别时，输出信息

    返回：
    无
    """
    boxes = result.boxes
    add_a=1 #1表示可以添加 0表示不可以
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")  # 给个合适的格式

    for i in range(len(boxes)):
        add_a=1
        if int(boxes.cls[i].item()) == 0 and len(cls0)<4:#先检测立杆
            if len(cls0) == 0: #没有就直接添加
                cls0[0] = int(boxes.xyxy[i][0].item())
                print(f"在{formatted_now}检测到类别为立杆的目标，目标左上角位置信息为:({int(boxes.xyxy[i][0].item())},{int(boxes.xyxy[i][1].item())})")
            for key in cls0:
               if(abs(cls0[key]-int(boxes.xyxy[i][0].item())))<5:
                   add_a=0 #不添加
            if add_a:
                cls0[key+1]=int(boxes.xyxy[i][0].item()) #key应该是整数变量
                print(f"在{formatted_now}检测到类别为立杆的目标，目标左上角位置信息为:({int(boxes.xyxy[i][0].item())},{int(boxes.xyxy[i][1].item())})")

        add_a = 1
        if int(boxes.cls[i].item())== 1 and len(cls1)<4:#检测扫地杆
            if len(cls1) == 0: #没有就直接添加
                cls1[0] = int(boxes.xyxy[i][0].item())
                print(f"在{formatted_now}检测到类别为扫地杆的目标，目标左上角位置信息为:({int(boxes.xyxy[i][0].item())},{int(boxes.xyxy[i][1].item())})")
            for key in cls1:
               if(abs(cls1[key]-int(boxes.xyxy[i][0].item())))<5:
                   add_a=0 #不添加
            if add_a:
                cls1[key+1]= int(boxes.xyxy[i][0].item()) #key应该是整数变量
                print(f"在{formatted_now}检测到类别为扫地杆的目标，目标左上角位置信息为:({int(boxes.xyxy[i][0].item())},{int(boxes.xyxy[i][1].item())})")

        add_a = 1
        if int(boxes.cls[i].item()) == 2 and len(cls2) < 7:  # 检测水平杆
            if len(cls2) == 0:  # 没有就直接添加
                cls2[0] =   int(boxes.xyxy[i][0].item())
                print(f"在{formatted_now}检测到类别为水平杆的目标，目标左上角位置信息为:({int(boxes.xyxy[i][0].item())},{int(boxes.xyxy[i][1].item())})")
            for key in cls2:
                if (abs(cls2[key] - int(boxes.xyxy[i][0].item()))) < 5:
                    add_a = 0  # 不添加
            if add_a:
                cls2[key + 1] = int(boxes.xyxy[i][0].item()) # key应该是整数变量
                print(f"在{formatted_now}检测到类别为水平杆的目标，目标左上角位置信息为:({int(boxes.xyxy[i][0].item())},{int(boxes.xyxy[i][1].item())})")

        if int(boxes.cls[i].item()) == 3 and len(cls3) < 1:  # 检测斜撑
            if len(cls3) == 0:  # 没有就直接添加
                cls3[0] = int(boxes.xyxy[i][0].item())
                print(f"在{formatted_now}检测到类别为撑杆的目标，目标左上角位置信息为:({int(boxes.xyxy[i][0].item())},{int(boxes.xyxy[i][1].item())})")

        if int(boxes.cls[i].item()) == 4 and len(cls4) < 1:  # 检测爬梯
            if len(cls4) == 0:  # 没有就直接添加
                cls4[0] = int(boxes.xyxy[i][0].item())
                print(f"在{formatted_now}检测到类别为爬梯的目标，目标左上角位置信息为:({int(boxes.xyxy[i][0].item())},{int(boxes.xyxy[i][1].item())})")

        if int(boxes.cls[i].item()) == 5 and len(cls5) < 1:  # 检测脚手架
            if len(cls5) == 0:  # 没有就直接添加
                cls5[0] = int(boxes.xyxy[i][0].item())
                print( f"在{formatted_now}检测到类别为脚手架的目标，目标左上角位置信息为:({int(boxes.xyxy[i][0].item())},{int(boxes.xyxy[i][1].item())})")

        if int(boxes.cls[i].item()) == 6 and len(cls6) < 1:  # 检测挡脚板
            if len(cls6) == 0:  # 没有就直接添加
                cls6[0] = int(boxes.xyxy[i][0].item())
                print(f"在{formatted_now}检测到类别为挡脚板的目标，目标左上角位置信息为:({int(boxes.xyxy[i][0].item())},{int(boxes.xyxy[i][1].item())})")
cls0 = {}
cls1 = {}
cls2 = {}
cls3 = {}
cls4 = {}
cls5 = {}
cls6 = {}
def detect_yolov8(output_folder='/mnt/jrwbxx/yolov8/chaichu/out_frame1'):
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    model = YOLO(r'/mnt/jrwbxx/yolov8/runs/detect/build_pro2/weights/best.pt')

    # 加载图像
    img_paths = glob(r'/mnt/jrwbxx/yolov8/chaichu/*.jpg')

    # 进行检测
    results = model(img_paths)
    for result in results:
        process_detection(result)

        # 保存检测结果图像
    for img_path, result in zip(img_paths, results):
        # 生成输出文件路径
        base_name = os.path.basename(img_path)
        file_name, _ = os.path.splitext(base_name)
        output_path = os.path.join(output_folder, f'{file_name}_det.jpg')

        # 保存检测结果图像
        cv2.imwrite(output_path, result.plot())
    # 打印检测结果
    # results.print()
    # results.show()  # 显示检测结果

if __name__ == '__main__':
    detect_yolov8()