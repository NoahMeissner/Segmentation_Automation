import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel

class ChatBotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Chatbot")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.messages_label = QLabel("ChatBot: Hi! How can I help you?")
        self.layout.addWidget(self.messages_label)

        self.user_input = QTextEdit()
        self.layout.addWidget(self.user_input)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.central_widget.setLayout(self.layout)

    def send_message(self):
        user_message = self.user_input.toPlainText()
        chatbot_response = f"ChatBot: You said: {user_message}"
        self.messages_label.setText(self.messages_label.text() + f"\nUser: {user_message}\n{chatbot_response}")
        self.user_input.clear()

def main():
    app = QApplication(sys.argv)
    window = ChatBotApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()