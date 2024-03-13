from PyQt6.QtWidgets import QApplication

from components.main_window import MainWindow
from components.core.cards.card import Card
from components.core.cards.deck import Deck
from data.defaults import A, J, Q, K, HEARTS, DIAMONDS, CLUBS, SPADES, SUITS, VALUES


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
