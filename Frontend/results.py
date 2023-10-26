import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QGridLayout
import json
from PIL import Image, ImageDraw
import csv
import re


class TestApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        with open("../Backend/DLmodel_results.json", 'r') as json_file:
            graphDirs = json.load(json_file)

        self.setWindowTitle("Bosse")
        self.setGeometry(100, 100, 400, 400)

        self.window = QWidget(self)
        self.setCentralWidget(self.window)
        self.grid_layout = QGridLayout(self.window)

        # Labels
        self.results_name = QLabel("results")
        self.pred_training_name = QLabel("Prediction Training")
        self.confusion_matrix_name = QLabel("Confusion Matrix")
        self.precision_recall_name = QLabel("Precision Recall")

        def load_and_resize_image(image_path, xfactor, yfactor):
            image = Image.open(image_path)
            width = int(400)
            height = int(400)
            image = image.resize((width, height))
            pixmap = QPixmap.fromImage(image.toqimage())
            return pixmap

        def load_and_resize_image_i(image, xfactor, yfactor):
            width = int(image.size[0] * xfactor)
            height = int(image.size[1] * yfactor)
            image = image.resize((width, height))
            pixmap = QPixmap.fromImage(image.toqimage())
            return pixmap

        # Pictures
        results_path = "../Model/runs/detect/"+graphDirs["results"]
        self.results = load_and_resize_image(results_path, .2, .2)
        pred_path = "../Model/runs/detect/"+graphDirs["pred training"]
        self.pred_training = load_and_resize_image(pred_path, .2, .2)
        conf_path = "../Model/runs/detect/"+graphDirs["confusion matrix"]
        self.confusion_matrix = load_and_resize_image(conf_path, .2, .2)

        # Open Image with BoundingBox


        # Read the CSV data from a file
        with open('boundingbox/data0.csv', 'r') as data:
            csv_reader = csv.reader(data)
            bbox_data = []

            for row in csv_reader:
                for cell in row:
                    if cell:
                        points = re.findall(r'\d+', cell)
                        bbox_data.append(list(map(int, points)))

        # Load the image
        image = Image.open('boundingbox/Image0.jpg')

        # Create a drawing object
        draw = ImageDraw.Draw(image)

        # Define bounding box color and width
        bbox_color = (255, 0, 0)  # Red color
        bbox_width = 10

        # Initialize variables to track the current bounding box points
        bbox_points = []

        # Iterate through the bounding box data
        for point in bbox_data:
            if not point:
                # Draw a bounding box when an empty line is encountered
                if len(bbox_points) > 2:
                    draw.polygon(bbox_points, outline=bbox_color, width=bbox_width)
                bbox_points = []  # Reset points for the next bounding box
            else:
                bbox_points.append(point[0])
                bbox_points.append(point[1])
        # Display or save the image with bounding boxes

        self.precision_recall = load_and_resize_image('boundingbox/output_image.png', .2, .2)

        # QLabel widgets to display images
        self.results_label = QLabel()
        self.results_label.setPixmap(self.results)

        self.pred_training_label = QLabel()
        self.pred_training_label.setPixmap(self.pred_training)

        self.confusion_matrix_label = QLabel()
        self.confusion_matrix_label.setPixmap(self.confusion_matrix)

        self.precision_recall_label = QLabel()
        self.precision_recall_label.setPixmap(self.precision_recall)

        # Fill Grid
        self.grid_layout.addWidget(self.results_name, 0, 0)
        self.grid_layout.addWidget(self.results_label, 1, 0)

        self.grid_layout.addWidget(self.pred_training_name, 0, 1)
        self.grid_layout.addWidget(self.pred_training_label, 1, 1)

        self.grid_layout.addWidget(self.confusion_matrix_name, 2, 0)
        self.grid_layout.addWidget(self.confusion_matrix_label, 3, 0)

        self.grid_layout.addWidget(self.precision_recall_name, 2, 1)
        self.grid_layout.addWidget(self.precision_recall_label, 3, 1)
        self.window.setLayout(self.grid_layout)

def main():
    app = QApplication([])
    Test = TestApp()
    Test.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()