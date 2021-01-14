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
        """Start and play a new game. If the internal Deck is empty, a new one
        will be created and shuffled. The deck is distributed over all players.
        Then every player plays in turns until all cards are used. A summary of
        every turn is printed.
        """

        # if deck is empty, fill and shuffle
        if len(self.deck.cards) == 0:
            self.deck.fill_deck()
            self.deck.shuffle()

        # Distribute cards
        self.deck.distribute(self.players)

        # Game playing
        # Play game as long as any player has any cards left
        while any([len(player.cards) > 0 for player in self.players]):

            for current_player in self.players:
                # Update history with previous turn
                if self.active_cards[current_player] is not None:
                    self.history_cards.append(self.active_cards[current_player])
                # if player has no cards anymore, end turn
                if len(current_player.cards) == 0:
                    continue
                # play new card
                current_card = current_player.play()
                self.active_cards[current_player] = current_card

            # end of turn bookkeeping
            print(f"Turn {self.turn_count} done:")
            print(
                f"\tActive cards: {', '.join([str(card) for card in self.active_cards.values()])}"
            )
            print(f"\t{len(self.history_cards)} cards played before this turn.")
            print("")  # print empty line for readabilty
            self.turn_count += 1

    def __str__(self) -> str:
        """
        :return: 'Board (N players, M turns)'
        """
        return f"Board ({len(self.players)} players, {self.turn_count} turns)"
