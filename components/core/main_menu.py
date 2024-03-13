from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from components.controller.gui import Gui
from components.core.widgets import Header


class MainMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.gui = Gui()
        self.init_ui()

    def init_ui(self):
        self.gui.add_layout("main", QVBoxLayout())

        header = Header()
        header.add_widget("title", QLabel("Casino"))
        self.gui.add_widget("header", "main", header)

        self.gui.add_layout("body", QVBoxLayout())
        self.gui.add_widget("new_game_button", "body", QPushButton("New Game", self))
        self.gui.add_widget("load_game_button", "body", QPushButton("Load Game", self))
        self.gui.add_widget("options_button", "body", QPushButton("Options", self))
        self.gui.add_widget("quit_button", "body", QPushButton("Quit", self))

        self.gui.nest_layout("body", "main")

        self.gui.add_widget("header", "main", Header())
        self.setLayout(self.gui.get_layout("main"))
