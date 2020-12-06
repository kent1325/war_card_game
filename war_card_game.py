"""Koden er udviklet af:
    Navn: Kent Vugs Nielsen
    email: kniels18@student.aau.dk
    Gruppe: A308b

    Programmet er udviklet selvstændigt og individuelt.
"""

from game_player import Player
from game_deck import Deck
from game_settings import Settings


class War:
    """Overall class to game behavior"""
    def __init__(self):
        """Load game settings and initialize the game"""
        self.playing_field = []
        self.rounds_played = 0
        self.is_game_over = False

        # Load Settings
        self.settings = Settings()

        # Initialize Deck
        self.deck = Deck(self.settings)
        self.deck.shuffle_deck()

        # Initialize Players
        self.players = [Player(name=f"Player {i}") for i in range(1, self.settings.number_of_players + 1)]

        # Give player game cards
        n_cards = len(self.deck)//len(self.players)
        for player in self.players:
            player.initialize_hand(self.deck, n_cards)

    def run_game(self):
        """Start the main loop for the game"""
        while self.rounds_played < 3000:
            if len(self.players) == 1:
                print(f"The ultimate champion of War is: {self.players[0]} and won within {self.rounds_played} rounds")
                self.is_game_over = True
                break

            self.playing_field = []
            for i, player in enumerate(self.players):
                if player.get_hand_size() == 0:
                    self.players.pop(i)
                    print(f"***{player} is out of cards and thereby out of the game.***")
                else:
                    self.playing_field.append(player.play_card())
                    print(f"{player.name} played: {self.playing_field[-1]}")

                if (self.rounds_played % 10) == 0:
                    player.shuffle_hand()

            round_winner_index = self.playing_field.index(max(self.playing_field))
            self.players[round_winner_index].receive_cards(self.playing_field)
            print(f"The round winner is: {self.players[round_winner_index]}\n")

            self.rounds_played += 1

        if not self.is_game_over:
            hand_sizes = []
            for player in self.players:
                hand_sizes.append(player.get_hand_size())
            game_winner_index = hand_sizes.index(max(hand_sizes))
            print(f"The ultimate champion of War (decided by hand size) is: {self.players[game_winner_index]} "
                  f"with hand size: {max(hand_sizes)}")


if __name__ == '__main__':
    # Make a game instance, and run the game.
    war = War()
    war.run_game()
