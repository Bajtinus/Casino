from PyQt6.QtWidgets import QLayout, QWidget


class Gui:
    def __init__(self):
        self.content = {}

    def add_layout(self, name: str, layout: QLayout) -> None:
        self.content[name] = {"layout": layout, "widgets": {}}

    def get_layout(self, name: str) -> QLayout:
        if name not in self.content:
            raise ValueError(f"Layout \"{name}\" not found")
        return self.content[name]["layout"]

    def add_widget(self, widget_name: str, layout_name: str, widget: QWidget) -> None:
        self.content[layout_name]["widgets"][widget_name] = widget
        self.content[layout_name]["layout"].addWidget(widget)

    def nest_layout(self, to_nest: str, to_nest_in: str) -> None:
        self.content[to_nest_in]["layout"].addLayout(self.content[to_nest]["layout"])