import os
import cv2
from ultralytics import YOLO


def detect_obb_in_folder(folder_path, output_folder, interval=1):
    # Load the YOLOv8 OBB model
    model = YOLO("/mnt/jrwbxx/yolov8/runs/obb/8_23_obb_only_bar/weights/best.pt")  # Ensure you have the correct path to the trained model

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of image files in the folder
    image_files = sorted(
        [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff'))])

    image_count = 0
    for idx, image_file in enumerate(image_files):
        if idx % interval == 0:  # Process every 'interval' image
            image_path = os.path.join(folder_path, image_file)
            image = cv2.imread(image_path)

            # Perform detection on the image
            results = model(image)

            # Process and save each detection result
            for result in results:
                annotated_image = result.plot()  # Plot the results on the image

                # Save the annotated image
                output_path = os.path.join(output_folder, f"detected_{image_count:04d}.jpg")
                cv2.imwrite(output_path, annotated_image)
                image_count += 1


if __name__ == '__main__':
    folder_path = r"/mnt/jrwbxx/yolov8/chaichu_8_7"  # Specify the path to your input image folder
    output_folder = "/mnt/jrwbxx/yolov8/runs/obb_detect"  # Specify the folder to save the output images
    interval = 5  # Specify the interval (e.g., every 5 images)

    detect_obb_in_folder(folder_path, output_folder, interval)
