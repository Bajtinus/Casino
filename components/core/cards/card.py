from components.misc import helpers
from data.defaults import A, J, Q, K, HEARTS, DIAMONDS, CLUBS, SPADES, SUITS, VALUES


class Card:
    def __init__(self, value, suit):

        if value not in VALUES:
            raise (ValueError("Invalid card value"))
        if suit not in SUITS:
            raise (ValueError("Invalid suit"))
        self.value = value
        self.suit = suit
        self.name = helpers.int_to_str(value) + " of " + helpers.int_to_str(suit)

    def __str__(self):
        if self.value not in VALUES:
            raise (ValueError("Invalid card value while converting to string"))
        else:
            value = helpers.int_to_str(self.value)

        if self.suit not in SUITS:
            raise (ValueError("Invalid suit while converting to string"))
        else:
            suit = helpers.int_to_str(self.suit)

        return f"{value} of {suit}"
