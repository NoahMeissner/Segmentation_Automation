import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel

class TrainingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.send_res = []

        self.setWindowTitle("Training")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.image_label = QLabel()
        pixmap = QPixmap('python.png')
        self.image_label.setPixmap(pixmap)
        self.layout.addWidget(self.image_label)

        self.train_button = QPushButton("Train")
        self.layout.addWidget(self.train_button)

        self.central_widget.setLayout(self.layout)
        self.send_button.installEventFilter(self)

def main():
    app = QApplication(sys.argv)
    window = TrainingApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()