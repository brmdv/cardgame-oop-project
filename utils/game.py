from utils.player import Player, Deck
from utils.card import Card
from typing import List, Dict


class Board:
    """This class describes a board, a game that is played, which contains the
    players, a deck of cards and all other components to represent the playing
    of the game.
    """

    def __init__(self, players: List[Player], deck: Deck = None):
        """Create new Board, with specified list of players and a new Deck.

        :param players: List of Player instances.
        :param deck: Use specific Deck instance for this Board (optional)
        """
        self.players = players
        self.turn_count = 0
        self.active_cards: Dict[Player, Card] = {
            player: None for player in self.players
        }  # last card played by each player
        self.history_cards: List[
            Card
        ] = []  # All played cards in order, not including active_cards
        # Create or reuse deck
        self.deck: Deck = Deck() if deck is None else deck

        def start_game(self):
            """"""
            # if deck is empty, fill and shuffle
            if len(self.deck.cards) == 0:
                self.deck.fill_deck()
                self.deck.shuffle()

            # Distribute cards
            self.deck.distribute(self.players)
