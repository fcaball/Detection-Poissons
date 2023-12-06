import os
import numpy as np
import cv2
import time
from ultralytics import YOLO
import sys

# VIDEO_DIRS = os.path.join('.', 'videos')
# video_filename = 'poissons1.mp4'

# video_path = os.path.join(VIDEO_DIRS, video_filename)
video_path =sys.argv[2]

# output_dir = os.path.join(VIDEO_DIRS, 'output_videos')
sys.argv[3]


video_path_out = sys.argv[3]+"output_predict_"+sys.argv[1]+".mp4"

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = "../../"+sys.argv[1]+"_epochs/weights/last.pt"

model = YOLO(model_path)

threshold = 0.5

while ret:
    results = model(frame)[0]


    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1), int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()