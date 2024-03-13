import json

from pathlib import Path

from components.controller.json_encoder import JsonEncoder


def write_json(data: dict, filename: Path) -> None:
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, cls=JsonEncoder)


def read_json(filename: Path) -> dict:
    with open(filename, "r") as file:
        return json.load(file)
