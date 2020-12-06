import random


class Player:
    def __init__(self, name):
        """A player instance"""
        self.name = name
        self.hand = []

    def initialize_hand(self, deck, num_of_cards):
        """Give hand the right amount of cards from deck"""
        for i in range(num_of_cards):
            self.hand.append(deck.pop())

    def show_hand(self):
        """returns a representation of all the cards a player has on hand"""
        return [card.show() for card in self.hand]

    def get_hand_size(self):
        """return the amount of cards in hand"""
        return len(self.hand)
    
    def receive_cards(self, cards):
        """Add cards to card collection in hand"""
        self.hand[0:0] = cards
        
    def shuffle_hand(self):
        """Shuffles the cards a player has"""
        random.shuffle(self.hand)

    def play_card(self):
        """removes the played card from hand"""
        return self.hand.pop()

    def __str__(self):
        return self.name
