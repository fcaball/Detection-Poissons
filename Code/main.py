from ultralytics import YOLO

#Load the model
model = YOLO("yolov8n.yaml")

#Use the model
results = model.train(data="config.yaml", epochs=20)

