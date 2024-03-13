from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox


class ExitPopup(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exit")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setText("Are you sure you want to exit?")
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.setDefaultButton(QMessageBox.StandardButton.No)
