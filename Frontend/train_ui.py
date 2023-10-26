import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from Model.train import Train
import json
import shutil


class TrainingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.nextPage = False
        self.setWindowTitle("Bosser")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: #ffffff;")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.messages_label = QLabel(f"System: Train Process")
        self.messages_label.setStyleSheet("font-size: 18pt")
        self.messages_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.messages_label)

        self.send_button = QPushButton("Start")
        self.send_button.setStyleSheet("font-size: 18pt;background-color: #588b8b")
        self.send_button.clicked.connect(self.start_button_clicked)
        self.layout.addWidget(self.send_button)

        self.next_button = QPushButton("Next")
        self.next_button.setStyleSheet("background-color: #588b8b")
        self.next_button.clicked.connect(self.nextButtonClicked)
        self.next_button.setEnabled(False)
        self.layout.addWidget(self.next_button)


        self.central_widget.setLayout(self.layout)
        self.send_button.installEventFilter(self)

    def nextButtonClicked(self):
        if (self.nextPage == True):
            return True
    def start_button_clicked(self):
            self.messages_label.setText("Pictures in Process")
            self.send_button.setEnabled(False)
            self.send_button.setStyleSheet("font-size: 12pt;background-color: #588b8b")

            self.make_pictures()



    def make_pictures(self):
         image_source = '/Users/noahmeissner/Documents/github/bosse/Model/Images/Image0.jpg'
         csv_source = '/Users/noahmeissner/Documents/github/bosse/Model/Images/data0.csv'
         destination_folder = '/Users/noahmeissner/Documents/github/bosse/Frontend/boundingbox'
         shutil.copy(image_source, destination_folder)
         shutil.copy(csv_source, destination_folder)
         train_model = Train()
         lib = train_model.train_model()
         data = {"results": lib + "/results.png",
                 "pred training": lib + "/val_batch1_pred.jpg",
                 "confusion matrix": lib + "/confusion_matrix_normalized.png",
                 "precision recall": lib + "/PR_curve.png"
                 }
         file_path = "../Backend/DLmodel_results.json"
         with open(file_path, 'w') as json_file:
             json.dump(data, json_file)

         self.next_button.setEnabled((True))
         self.next_button.setStyleSheet("font-size: 18pt;background-color: #588b8b")
