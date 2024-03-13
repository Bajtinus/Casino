from PyQt6.QtWidgets import QWidget, QHBoxLayout

from components.core.gui import Gui


class Header(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.widgets = {}

        self.setLayout(self.layout)

    def add_widget(self, name: str, widget: QWidget) -> None:
        self.widgets[name] = widget
        self.layout.addWidget(widget)

