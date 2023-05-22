from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class ErrorWindow(QWidget):
    def __init__(self, message, *args, **kwargs):
        super(ErrorWindow, self).__init__(*args, **kwargs)
        self.setMinimumSize(200, 100)
        self.setWindowTitle("Error!")
        self.messageLabel = QLabel(message)
        self.private_layout = QGridLayout()
        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(self.hide)
        self.private_layout.addWidget(self.messageLabel, 0, 0, Qt.AlignCenter)
        self.private_layout.addWidget(self.okButton, 1, 0, Qt.AlignCenter)
        self.setLayout(self.private_layout)
        self.show()
