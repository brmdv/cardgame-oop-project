from utils.player import Player, Deck
from utils.card import Card
from typing import List, Dict, OrderedDict


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
        # Play game as long as any player has any cards left and no player has more than 500 points
        while any([player.number_of_cards > 0 for player in self.players]) and all(
            ([player.score < 500 for player in self.players])
        ):
            for current_player in self.players:
                # Update history with previous turn
                if self.active_cards[current_player] is not None:
                    self.history_cards.append(self.active_cards[current_player])
                # if player has no cards anymore, end turn
                if current_player.number_of_cards == 0:
                    continue
                # play new card
                current_card = current_player.play()
                self.active_cards[current_player] = current_card

            # Give highest card(s) of round +50 points
            winning_value = max(self.active_cards.values()).value
            round_winners = []  # keep winner namer for the bookkeeping part
            for player in self.active_cards:
                if self.active_cards[player].value == winning_value:
                    player.score += 50
                    round_winners.append(str(player))

            # end of turn bookkeeping
            print(f"Turn {self.turn_count} done:")
            print(
                f"\tActive cards: {', '.join([str(card) for card in self.active_cards.values()])}"
            )
            print("\t" + " ".join([f"{name}+50" for name in round_winners]))
            print(f"\t{len(self.history_cards)} cards played before this turn.")
            print()  # print empty line for readabilty
            self.turn_count += 1

        # select game winner and print scores
        results = {}
        for player in self.players:
            if player.score in results:
                results[player.score].append(str(player))
            else:
                results[player.score] = [str(player)]
        print("Game over")
        for i, score in enumerate(sorted(results.keys())[::-1]):
            print(f"{i+1}. {score:>3} PTS: " + ", ".join(results[score]))

    def __str__(self) -> str:
        """
        :return: 'Board (N players, M turns)'
        """
        return f"Board ({len(self.players)} players, {self.turn_count} turns)"
