from PyQt6.QtWidgets import QWidget, QHBoxLayout


class Header(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.widgets = {}

        self.setLayout(self.layout)

    def add_widget(self, name: str, widget: QWidget) -> None:
        self.widgets[name] = widget
        self.layout.addWidget(widget)

    def remove_widget(self, name: str) -> None:
        widget = self.widgets.pop(name)
        widget.deleteLater()

    def get_widget(self, name: str) -> QWidget:
        return self.widgets[name]

