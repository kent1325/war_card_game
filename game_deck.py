import random
from game_card import Card


class Deck:
    """A class to represent a card deck."""
    def __init__(self, settings):
        """Card Deck instance"""
        self.deck = []
        self.settings = settings

        self.init_deck(self.settings)

    def init_deck(self, settings):
        """Fill deck with cards, from the settings window"""
        for suit in settings.suits:
            for i, value in enumerate(settings.values):
                self.deck.append(Card(value=value, suit=suit, name=settings.names[i]))
                
    def pop(self):
        return self.deck.pop()
                
    def shuffle_deck(self):
        random.shuffle(self.deck)

    def __str__(self):
        return [card.show() for card in self.deck]

    def __len__(self):
        return len(self.deck)
