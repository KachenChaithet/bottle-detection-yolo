from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model.train(
    data=r"C:\Users\User\Documents\keepproject\learningcondainYolo\dataset\data.yaml",
    epochs=50,
    imgsz=640,
    device="cpu"
)