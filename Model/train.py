import sys
print(sys.path)
#sys.path.append("/Users/michael_khalfin/opt/anaconda3/bin/ultralytics")

import os
print(os.getcwd())
sys.path.append(os.getcwd())

from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='config.yaml',
   imgsz=1280,
   epochs=50,
   batch=8,
   name='yolov8n_v8_50e'
)