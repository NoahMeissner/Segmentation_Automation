import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from Model.train import Train
class TrainingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.nextPage = False
        self.setWindowTitle("Bosser")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.messages_label = QLabel(f"System: Train Process")
        self.messages_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.messages_label)

        self.send_button = QPushButton("Start")
        self.send_button.clicked.connect(self.start_button_clicked)
        self.layout.addWidget(self.send_button)

        self.next_button = QPushButton("Next")
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
            self.send_button.setText("next")
            self.send_button.setEnabled(False)
            self.make_pictures()

    def make_pictures(self):
        train_model = Train()
        train_model.train_model()
        self.next_button.setEnabled((True))