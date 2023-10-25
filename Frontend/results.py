import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QGridLayout


class TestApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Bosser")
        self.setGeometry(100, 100, 400, 400)

        self.window = QWidget(self)
        self.setCentralWidget(self.window)
        self.grid_layout = QGridLayout()
        self.accurazy_grid = QGridLayout()
        self.name = QLabel("Accuarcy")
        self.result = QLabel("80%")
        self.category = QLabel("category")
        self.category2 = QLabel("category2")
        self.category3 = QLabel("category3")
        self.category = QLabel("category4")
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")
        self.button4 = QPushButton("Button 4")
        self.grid_layout.addWidget(self.button1, 0, 0)
        self.grid_layout.addWidget(self.button2, 0, 1)
        self.grid_layout.addWidget(self.button3, 1, 0)
        self.grid_layout.addWidget(self.button4, 1, 1)
        self.window.setLayout(self.grid_layout)

def main():
    app = QApplication([])
    Test = TestApp()
    Test.show()


    sys.exit(app.exec())

if __name__ == '__main__':
    main()
