class Settings:
    """A class to manage game settings."""
    card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    card_suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    card_names = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
                  "EIGHT", "NINE", "TEN", "KNIGHT", "QUEEN", "KING"]
    max_n_players = 26
    min_n_players = 2

    def __init__(self, values=None, suits=None, names=None):
        """Initialize settings attributes"""
        # Load deck with above settings
        if names is None:
            self.names = Settings.card_names
        else:
            self.names = names
        if suits is None:
            self.suits = Settings.card_suits
        else:
            self.suits = suits
        if values is None:
            self.values = Settings.card_values
        else:
            self.values = values

        self.number_of_players = 2

        self.set_num_players()

    def set_num_players(self):
        """Set number of players for the game"""
        while True:
            try:
                n_players = int(input("Please enter the number of players: "))
                if n_players < Settings.min_n_players or n_players > Settings.max_n_players:
                    print(f"The number of players must be between "
                          f"{Settings.min_n_players} and {Settings.max_n_players}")
                else:
                    break
            except ValueError as ex:
                print("The entered number was not an integer. Try again.")
        self.number_of_players = n_players
