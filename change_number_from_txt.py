import os
import tempfile


def modify_lines_in_file(file_path):
    """遍历文件中的每一行，修改每行第一个数字从7变为5"""
    temp_file_path = file_path + '.tmp'

    try:
        with open(file_path, 'r', encoding='utf-8') as file, open(temp_file_path, 'w', encoding='utf-8') as temp_file:
            for line in file:
                if line.strip() and line[0] == '6':
                    line = '2' + line[1:]
                temp_file.write(line)

        # 替换原文件
        os.replace(temp_file_path, file_path)

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)


def process_directory(directory_path):
    """遍历目录中的所有txt文件并修改符合条件的文件"""
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            modify_lines_in_file(file_path)


# 使用示例
directory_path = r'E:\high_work\8_23_new_file\build_obb_clothe_8_15_new\valid\labels'  # 请将这里替换为你的文件夹路径
process_directory(directory_path)