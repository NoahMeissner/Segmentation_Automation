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
      model = YOLO('/Users/noahmeissner/Documents/github/bosse/Model/yolov8n.pt')

      # Training.
      results = model.train(
         data='/Users/noahmeissner/Documents/github/bosse/Model/yolov8n.pt',
         imgsz=512,
         epochs=4,
         batch=1,
         name='/Users/noahmeissner/Documents/github/bosse/Model/runs/detect/yolov8n_v8_50e'
      )
      wipe = Wipe()
      wipe.Wipe_Data()

      result_directory = "/Users/noahmeissner/Documents/github/bosse/Model/runs/detect"
      folders = [f for f in os.listdir(result_directory) if os.path.isdir(os.path.join(result_directory, f))]
      try:
         most_recent_folder = folders[0]
         return most_recent_folder
      except Exception as e:
         return e

