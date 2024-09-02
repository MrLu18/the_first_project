import os
import shutil

def match_and_copy_files(image_folder, text_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 加载图像文件以获取所有可能的文档
    image_files = {file.lower().split('.jpg')[0]: os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.lower().endswith('.jpg')}

    # 加载文本文件以快速查找匹配的文档
    text_files = {file.lower().split('.txt')[0]: os.path.join(text_folder, file) for file in os.listdir(text_folder) if file.lower().endswith('.txt')}

    # 检查图像文件中的每一个文档是否有对应的文本文件
    for image_doc in image_files:
        if image_doc in text_files:
            # 复制匹配的文本文件到指定文件夹
            png_file = image_files[image_doc]
            txt_file_src = text_files[image_doc]
            txt_file_dst = os.path.join(output_folder, os.path.basename(txt_file_src))
            try:
                # 复制文件
                shutil.copy(txt_file_src, txt_file_dst)
                print(f"Copied {txt_file_src} to {txt_file_dst}")
            except Exception as e:
                print(f"Failed to copy {txt_file_src} to {txt_file_dst}: {e}")
        else:
            print(f"No matching text file found for {image_doc}")

# 例如：
image_folder = r'D:\python_program\ultralytics-main\datasets\8_30_obb\valid\images'
text_folder = r'E:\high_work\8_23_new_file\labels'
output_folder = r'D:\python_program\ultralytics-main\datasets\8_30_obb\valid\labels'

match_and_copy_files(image_folder, text_folder, output_folder)