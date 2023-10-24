import sys
from Backend.chat import getQuestions
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel

class ChatBotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.answer = []
        self.object_q = getQuestions()

        self.questions = self.object_q.get_question()
        self.i = 1
        self.setWindowTitle("Bosser")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.messages_label = QLabel(f"System: {self.questions[0]}")
        self.layout.addWidget(self.messages_label)

        self.user_input = QTextEdit()
        self.layout.addWidget(self.user_input)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.central_widget.setLayout(self.layout)

        # Connect Enter key press event to the "Send" button's click event
        self.send_button.installEventFilter(self)

    def eventFilter(self, source, event):
        if source is self.user_input and event.type() == Qt.EventType.KeyPress and event.key() == Qt.Key.Key_Enter:
            self.send_message()
            return True
        return super().eventFilter(source, event)

    def send_message(self):
        user_message = self.user_input.toPlainText()
        self.answer = self.ask_question(user_message, self.answer)
        print(self.answer)
        self.messages_label.setText(self.messages_label.text() + f"\nUser: {user_message}")
        self.user_input.clear()
        self.messages_label.setText(self.messages_label.text() + f"\nSystemt: {self.questions[self.i]}")
        self.i += 1

    def ask_question(self, input, answer):
        if len(answer) == 4:
            question = self.questions[0] \
                .replace('${type}', answer[0]) \
                .replace('${color}', answer[1]) \
                .replace('${material}', answer[2]) \
                .replace('${size}', answer[3])
            print('this')
            self.questions[5] = question
            set_answer = input
            if set_answer == 'true':
                return answer
            else:
                return []
        else:
            set_answer = input
            if set_answer != 'yes':
                answer.append(set_answer)
            return answer

def main():
    app = QApplication(sys.argv)
    window = ChatBotApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
