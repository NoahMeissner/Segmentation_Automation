import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QComboBox, QLabel, QVBoxLayout, QWidget

class ImageComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Dropdown")
        self.layout = QVBoxLayout()

        # Create a QComboBox
        self.combo_box = QComboBox()
        self.combo_box.currentIndexChanged.connect(self.update_image_label)
        self.layout.addWidget(self.combo_box)

        # Create a QLabel to display the selected image
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        # Create a dictionary to map object names to image paths
        self.image_map = {
            "Object 1": "image1.png",
            "Object 2": "image2.png",
            "Object 3": "image3.png",
            "Object 4": "image4.png",
        }

        # Add object names to the combo box
        self.combo_box.addItems(self.image_map.keys())

        self.setLayout(self.layout)

    def update_image_label(self, index):
        selected_item = self.combo_box.currentText()
        if selected_item in self.image_map:
            image_path = self.image_map[selected_item]
            pixmap = QPixmap(image_path)
            self.label.setPixmap(pixmap)

def main():
    app = QApplication(sys.argv)
    window = ImageComboBoxDemo()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()