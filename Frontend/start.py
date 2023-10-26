import sys
from bosse import ChatBotApp
from train_ui import TrainingApp
from results import TestApp
from robot.connect import Connect

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout



class StartPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.nextPage = False
        self.category_list = ['marker']
        self.setWindowTitle("Bosser")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: #ffffff;")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.messages_label = QLabel(f"Start Quality Assurance")
        self.messages_label.setStyleSheet("font-size: 18pt")
        self.messages_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.messages_label)

        self.send_button = QPushButton("Start")

        self.send_button.setStyleSheet("font-size: 18pt;background-color: #588b8b")
        self.send_button.clicked.connect(self.start_button_clicked)
        self.layout.addWidget(self.send_button)

        self.next_button = QPushButton("Next")
        self.next_button.setStyleSheet(" background-color: #588b8b")
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
        c = Connect()
        c.start_session()
        import time
        time.sleep(5)

        self.next_button.setStyleSheet("font-size: 18pt;background-color: #588b8b")

        self.next_button.setEnabled((True))





def main():
    app = QApplication([])
    start_page = StartPage()
    next_page = ChatBotApp()
    Train_page = TrainingApp()
    start_page.show()

    def open_next_page():
            start_page.hide()
            next_page.show()

    def open_Train():
        next_page.hide()
        Train_page.show()

    def open_Test():
        Test = TestApp()
        Train_page.hide()
        Test.show()



    start_page.next_button.clicked.connect(open_next_page)
    next_page.next_button.clicked.connect(open_Train)
    Train_page.next_button.clicked.connect(open_Test)




    sys.exit(app.exec())

if __name__ == '__main__':
    main()

