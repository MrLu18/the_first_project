import os
import random
import shutil

def random_copy_images(input_folder, output_folder, num_images):
    # 获取输入文件夹中的所有图像文件
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # 如果要求的图像数量大于输入文件夹中的图像数量，则将要求的数量设为输入文件夹中的图像数量
    num_images = min(num_images, len(image_files))

    # 随机选择要复制的图像文件
    selected_images = random.sample(image_files, num_images)

    # 复制选定的图像文件到输出文件夹
    for image_file in selected_images:
        src_path = os.path.join(input_folder, image_file)
        dst_path = os.path.join(output_folder, image_file)
        shutil.move(src_path, dst_path)

    print(f"{num_images} images copied from {input_folder} to {output_folder}.")

# 使用示例
input_folder = r"E:\high_work\8_23_new_file\images"
output_folder = r"D:\python_program\ultralytics-main\datasets\8_30_obb\train\images"
num_images = 900  # 要剪切的图像数量
random_copy_images(input_folder, output_folder, num_images)