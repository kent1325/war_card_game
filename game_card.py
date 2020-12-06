class Card:
    """A class to represent a playing card."""
    def __init__(self, value, suit, name):
        """Card instance"""
        self.value = value
        self.suit = suit
        self.name = name

    def get_card_details(self):
        """returns a informative representation of a card"""
        return f"Name:\t{self.name}\n" \
               f"Suit:\t{self.suit}\n" \
               f"Value:\t{self.value}"

    def show(self):
        """returns a simple representation of a card"""
        return f"{self.name} of {self.suit}"

    def __str__(self):
        return f"{self.name} of {self.suit}"

    def __add__(self, other):
        if isinstance(other, Card):
            return self.value + other.value
        else:
            return self.value + other

    def __lt__(self, other):
        if isinstance(other, Card):
            return self.value < other.value
        else:
            return self.value < other

    def __gt__(self, other):
        if isinstance(other, Card):
            return self.value > other.value
        else:
            return self.value > other
