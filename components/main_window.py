from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout

from components.core.gui import Gui
from components.core.menu import Menu
from components.core.widgets import Header


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Gui()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Casino")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.gui.add_layout("main", QVBoxLayout())

        header = Header()
        header.add_widget("title", QLabel("Casino", self))
        self.gui.add_widget("header", "main", header)

        body = Menu()
        self.gui.add_widget("body", "main", body)

        widget = QWidget()
        widget.setLayout(self.gui.get_layout("main"))
        self.setCentralWidget(widget)
        self.show()



