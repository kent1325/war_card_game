import random

class Player:
    def __init__(self, name):
        """"""
        self.name = name
        self.hand = []

    def give_cards(self, deck, num_of_cards):
        for i in range(num_of_cards):
            self.hand.append(deck.pop())

    def show_hand(self):
        return [card.show() for card in self.hand]

    def get_hand_size(self):
        return len(self.hand)
    
    def receive_cards(self, cards):
        self.hand[0:0] = cards
        
    def shuffle_hand(self):
        random.shuffle(self.hand)

    def play_card(self):
        return self.hand.pop()

    def __str__(self):
        return self.name
