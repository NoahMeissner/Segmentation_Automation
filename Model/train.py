import sys
import os
sys.path.append(os.getcwd())
from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='config.yaml',
   imgsz=512,
   epochs=4,
   batch=1,
   name='yolov8n_v8_50e'
)