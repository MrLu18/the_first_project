import os

# 需要添加的新行内容，确保它们符合 YOLO 标签格式
new_lines = [
    "2 0.500000 0.520139 0.028125 0.068056\n",
    "2 0.507422 0.760417 0.028125 0.070833\n",
    "2 0.231641 0.529514 0.077344 0.067361\n",
    "2 0.261719 0.730903 0.054688 0.067361\n"
]

# 输入文件夹路径
input_folder = r'E:\high_work\build\label_pro_plus'
output_folder = r'E:\high_work\build\label_pro_plus'

# 遍历文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        # 生成输入文件和输出文件的完整路径
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder,  filename) # 如果需要在前面加标志，可以进行对应修改

        # 读取输入文件
        with open(input_file_path, 'r') as infile:
            lines = infile.readlines()

        # 处理每一行
        processed_lines = []
        for line in lines:
            # 去除行末的换行符
            stripped_line = line.strip()

            # 检查行是否以 '2' 开头
            if not stripped_line.startswith('2'):
                processed_lines.append(line)

        # 在处理后的行集末尾添加新的内容
        processed_lines.extend(new_lines)

        # 写入到输出文件
        with open(output_file_path, 'w') as outfile:
            outfile.writelines(processed_lines)

        print(f"Processed {filename}, result saved to {output_file_path}")

print("所有文件处理完成。")