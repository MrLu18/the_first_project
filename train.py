from ultralytics import YOLO

# Load a model
def train_yolov8():
    #model = YOLO("yolov8n.yaml")  # build a new model from scratch
    model = YOLO(r"/mnt/jrwbxx/yolov8/runs/detect/build_pro1/weights/best.pt")  # load a pretrained model (recommended for training) 如果想从头开始训练一个权重文件 就不需要这个，如果是微调，那么可以加入这个

    # Use the model
    model.train(data=r"/mnt/jrwbxx/yolov8/datasets/build_pro2/build_pro2.yaml", epochs=100,batch=16,imgsz=640)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set
    # results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
    # path = model.export(format="onnx")  # export the model to ONNX format

if __name__ == '__main__':
    train_yolov8()