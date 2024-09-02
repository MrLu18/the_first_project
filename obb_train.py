from ultralytics import YOLO

# Load a model
def obb_train():
    model = YOLO("yolov8n-obb.yaml")  # build a new model from YAML
    model = YOLO("yolov8n-obb.pt")  # load a pretrained model (recommended for training)
    model = YOLO("yolov8n-obb.yaml").load("yolov8n.pt")  # build from YAML and transfer weights

    # Train the model
    results = model.train(data="/mnt/jrwbxx/yolov8/datasets/8_30_obb/obb_build_8_30.yaml", epochs=100, imgsz=640)

if __name__ == '__main__':
    obb_train()