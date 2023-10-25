import sys
from bosse import ChatBotApp
from train_ui import TrainingApp
from results import TestApp

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

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.messages_label = QLabel(f"System: Start Process")
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
        #TODO integrate Program from Joesph
        import time

        time.sleep(10)
        self.next_button.setEnabled((True))





def main():
    app = QApplication([])
    Test = TestApp()
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
        Train_page.hide()
        Test.show()



    start_page.next_button.clicked.connect(open_next_page)
    next_page.next_button.clicked.connect(open_Train)



    sys.exit(app.exec())

if __name__ == '__main__':
    main()

