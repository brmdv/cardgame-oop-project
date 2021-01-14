from utils.player import Player
from utils.game import Board
from random import sample

# Create 4 players
theano = [
    "Ad",
    "Arlene",
    "Bram",
    "Daniel",
    "Derrick",
    "Gülce",
    "Joren",
    "Louan",
    "Mohammad",
    "Philippe",
    "Regis",
    "Sijal",
    "Simon",
    "Vincent",
]
number_of_players = 4
my_players = [Player(name=name) for name in sample(theano, k=number_of_players)]
print("The players are " + ", ".join(str(player) for player in my_players))

# Start a game
my_board = Board(my_players)
my_board.start_game()