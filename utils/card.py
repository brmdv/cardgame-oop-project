class Symbol:
    """This class describes a playing card symbol."""

    def __init__(self, icon: str, color: str = None):
        """Initialize a card suit.

        :icon: card's suit, one of ♥ ♦ ♣ ♠
        :color: The symbol's color; 'red' or 'black'. If not specified, it is inferred from icon
        """
        self.icon = icon
        # Automatic selection of color based on icon
        if color is None:
            if icon in ["♣", "♠"]:
                self.color = "black"
            elif icon in ["♥", "♦"]:
                self.color = "red"
        else:
            self.color = "color"

    def __str__(self) -> str:
        return self.icon

    @staticmethod
    def suit_from_name(name: str) -> str:
        """A static method that converts the english name of a playing card suit to its corresponding Unicode symbol.

        :name: Name of suit, one of heart diamond club spade.
        """
        # Lookup dictionary
        names = {"heart": "♥", "diamond": "♦", "club": "♣", "spade": "♠"}

        # Take into account plural form of names
        if name[-1] == "s":
            name = name[:-1]

        return names[name]


class Card(Symbol):
    """Class that describes a playing card."""

    def __init__(self, icon: str, value: str, color: str = None):
        """Create new Card.

        :icon: card's suit, one of ♥ ♦ ♣ ♠
        :value: value of card, one of A 2 3 4 5 6 7 8 9 10 J Q K
        :color: color of card's symbol, one of "red", "black". If not specified, inferred from icon.
        """
        super().__init__(icon, color)
        self.value = value

    def __str__(self) -> str:
        return super().__str__() + self.value


# testing
# test_symbol = Symbol(Symbol.suit_from_name("heart"))
# test_card = Card(Symbol.suit_from_name("spades"), "A")
# # testKaart = Card("red", Card.suit_from_name("spade"), "11")
# print(str(test_symbol))
# print(str(test_card))
# pass