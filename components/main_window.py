from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QStackedLayout, QMessageBox

from components.controller import file_handler
from components.controller.popup_windows import ExitPopup
from components.core.main_menu import MainMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QStackedLayout()
        self.pages = {}
        self.root = Path(__file__).parent.parent
        self.config = {}

        self.init_ui()
        self.load_config()

    def init_ui(self):
        self.setWindowTitle("Casino")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.pages["main_menu"] = MainMenu()
        self.pages["main_menu"].gui.get_widget("quit_button", "body").clicked.connect(self.exit)

        self.layout.addWidget(self.pages["main_menu"])

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.show()

    def load_config(self):
        config = file_handler.read_json(self.root / "config" / "app_config.json")

        if "geometry" not in config:
            config["geometry"] = {
                "x": 0,
                "y": 0,
                "width": 800,
                "height": 600,
                "fullscreen": True
            }

        self.setGeometry(config["geometry"]["x"], config["geometry"]["y"], config["geometry"]["width"], config["geometry"]["height"])
        self.fullscreen(config["geometry"]["fullscreen"])
        self.config = config

    def update_config(self):
        self.config["geometry"] = {
            "x": self.x(),
            "y": self.y(),
            "width": self.width(),
            "height": self.height(),
            "fullscreen": self.isFullScreen()
        }

    def exit(self):
        self.update_config()
        file_handler.write_json(self.config, self.root / "config" / "app_config.json")

        msg_box = ExitPopup()
        response = msg_box.exec()
        if response == QMessageBox.StandardButton.Yes:
            self.close()

    def fullscreen(self, toggle: bool):
        self.showFullScreen() if toggle else self.showNormal()