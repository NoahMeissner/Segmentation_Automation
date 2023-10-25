import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QGridLayout
import json

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
        self.grid_layout = QGridLayout()
        #self.accuracy_grid = QGridLayout()
        # Labels
        self.results_name = QLabel("results")
        self.pred_training_name = QLabel("Prediction Training")
        self.confusion_matrix_name = QLabel("Confusion Matrix")
        self.precision_recall_name = QLabel("Precision Recall")
        # Pictures
        self.results = QPixmap(graphDirs["results"])
        self.pred_training = QPixmap(graphDirs["pred training"])
        self.confusion_matrix = QPixmap(graphDirs["confusion matrix"])
        self.precision_recall = QPixmap(graphDirs["precision recall"])

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
        self.grid_layout.addWidget(self.results, 1, 0)

        self.grid_layout.addWidget(self.pred_training_name, 0, 1)
        self.grid_layout.addWidget(self.pred_training_name, 1, 1)

        self.grid_layout.addWidget(self.confusion_matrix_name, 2, 0)
        self.grid_layout.addWidget(self.confusion_matrix, 3, 0)

        self.grid_layout.addWidget(self.precision_recall_name, 2, 1)
        self.grid_layout.addWidget(self.precision_recall, 3, 1)
        self.window.setLayout(self.grid_layout)

def main():
    app = QApplication([])
    Test = TestApp()
    Test.show()


    sys.exit(app.exec())

if __name__ == '__main__':
    main()
