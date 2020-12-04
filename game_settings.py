class Settings:
    card_names = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
                  "EIGHT", "NINE", "TEN", "KNIGHT", "QUEEN", "KING"]
    card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    card_suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

    def __init__(self, values=None, suits=None, names=None):
        """"""
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
        while True:
            try:
                n_players = int(input("Please enter the number of players: "))
                if n_players < 2 or n_players > 52:
                    print("The number of players must be between 2 and 52")
                else:
                    break
            except ValueError as ex:
                print("The entered number was not an integer. Try again.")
        self.number_of_players = n_players
