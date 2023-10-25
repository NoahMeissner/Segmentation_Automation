import sys
import os
from ultralytics import YOLO
from Model.preprocessing import Preprocess_Data
from Backend.wipe_TrainingData import Wipe

class Train:

   def __init__(self):
      pass
   def train_model(self):
      preprocess = Preprocess_Data()
      preprocess.preprocessing()

      sys.path.append(os.getcwd())

      # Load the model.
      model = YOLO('../Model/yolov8n.pt')

      # Training.
      results = model.train(
         data='../Model/config.yaml',
         imgsz=512,
         epochs=4,
         batch=1,
         name='yolov8n_v8_50e'
      )
      wipe = Wipe()
      wipe.Wipe_Data()

