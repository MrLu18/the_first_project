import cv2
import os


def extract_frames(video_path, output_folder, fps):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # 获取视频的帧率
    video_fps = cap.get(cv2.CAP_PROP_FPS)

    # 计算帧的间隔
    frame_interval = int(video_fps / fps)

    frame_count = 0
    saved_frame_count = 255

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break


        # 每隔 frame_interval 帧保存一次
        if frame_count % frame_interval == 0:
            frame_name = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")
            cv2.imwrite(frame_name, frame)
            saved_frame_count += 1
            frame=cv2.resize(frame, (640,480))

            #cv2.imshow("frame",frame)
            #cv2.waitKey()


        frame_count += 1

    cap.release()
    print(f"Extracted {saved_frame_count} frames.")


# 示例用法
video_path = r'E:\high_work\8_27_dajian\NVR_ch7_main_20240827100003_20240827101600.dav'
output_folder = r'E:\high_work\8_27_dajian\ch3_8_27'
extract_frames(video_path, output_folder, fps=0.2)
