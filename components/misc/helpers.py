


def int_to_str(value: int) -> str:
    if value == 1:
        return "A"
    elif value == 11:
        return "J"
    elif value == 12:
        return "Q"
    elif value == 13:
        return "K"
    elif value in range(2, 11):
        return str(value)
    elif value == 101:
        return "Hearts"
    elif value == 102:
        return "Diamonds"
    elif value == 103:
        return "Clubs"
    elif value == 104:
        return "Spades"
    else:
        raise ValueError("Invalid value")


def str_to_int(value: str) -> int:
    if value == "A":
        return 1
    elif value == "J":
        return 11
    elif value == "Q":
        return 12
    elif value == "K":
        return 13
    elif value == "Hearts" or value == "hearts":
        return 101
    elif value == "Diamonds" or value == "diamonds":
        return 102
    elif value == "Clubs" or value == "clubs":
        return 103
    elif value == "Spades" or value == "spades":
        return 104
    else:
        raise ValueError("Invalid value")
