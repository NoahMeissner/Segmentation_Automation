import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QGridLayout
import json
from PIL import Image

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
            width = int(image.size[0] * xfactor)
            height = int(image.size[1] * yfactor)
            image = image.resize((width, height), Image.Resampling.LANCZOS)
            pixmap = QPixmap.fromImage(image.toqimage())
            return pixmap

        # Pictures
        results_path = "/Users/michael_khalfin/bosse/Model/runs/detect/"+graphDirs["results"]
        self.results = load_and_resize_image(results_path, .2, .2)
        pred_path = "/Users/michael_khalfin/bosse/Model/runs/detect/"+graphDirs["pred training"]
        self.pred_training = load_and_resize_image(pred_path, .2, .2)
        conf_path = "/Users/michael_khalfin/bosse/Model/runs/detect/"+graphDirs["confusion matrix"]
        self.confusion_matrix = load_and_resize_image(conf_path, .2, .2)
        #prec_path = "/Users/michael_khalfin/bosse/Model/runs/detect/"+graphDirs["precision recall"]
        #self.precision_recall = load_and_resize_image(prec_path, .2, .2)

        # QLabel widgets to display images
        self.results_label = QLabel()
        self.results_label.setPixmap(self.results)

        self.pred_training_label = QLabel()
        self.pred_training_label.setPixmap(self.pred_training)

        self.confusion_matrix_label = QLabel()
        self.confusion_matrix_label.setPixmap(self.confusion_matrix)

        #self.precision_recall_label = QLabel()
        #self.precision_recall_label.setPixmap(self.precision_recall)

        # Fill Grid
        self.grid_layout.addWidget(self.results_name, 0, 0)
        self.grid_layout.addWidget(self.results_label, 1, 0)

        self.grid_layout.addWidget(self.pred_training_name, 0, 1)
        self.grid_layout.addWidget(self.pred_training_label, 1, 1)

        self.grid_layout.addWidget(self.confusion_matrix_name, 2, 0)
        self.grid_layout.addWidget(self.confusion_matrix_label, 3, 0)

        #self.grid_layout.addWidget(self.precision_recall_name, 2, 1)
        #self.grid_layout.addWidget(self.precision_recall_label, 3, 1)
        self.window.setLayout(self.grid_layout)

def main():
    app = QApplication([])
    Test = TestApp()
    Test.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()