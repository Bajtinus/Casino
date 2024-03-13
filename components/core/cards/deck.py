from components.core.cards.card import Card
from data.defaults import SUITS, VALUES


class Deck:
    def __init__(self):
        self.cards = default_deck()

    def __str__(self) -> str:
        to_return = f"Deck of {len(self.cards)} cards\n"
        to_return += f"[{', '.join(card.name for card in self.cards)}]"
        return to_return


def default_deck() -> list[Card]:
    deck = []
    for suit in SUITS:
        for value in VALUES:
            deck.append(Card(value, suit))
    return deck
