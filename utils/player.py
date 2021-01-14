from utils.card import Card
from random import choice, shuffle
from typing import List


class Player:
    """A class for a card player."""

    player_count = 1  # player counter, starting at 1 because humans

    def __init__(self, name: str = "", cards: List[Card] = None):
        """Create a new player.

        :param cards: List of Card instances; the player's hand.
        :param name: Player's name (optional, if empty → 'Player n').
        """
        self.cards: List[Card]
        if cards is not None:
            self.cards = cards
        else:
            self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history: List[Card] = []
        self.name = name
        # Assign autoincrementing player number
        self.player_number = Player.player_count
        Player.player_count += 1

    def play(self) -> Card:
        """Play a turn. This method will return a random card from the player's
        hand, which is then added to the history and removed from the hand. A
        summary will be printed, in the form:
        {PLAYER'S NAME} ({TURN}) played: ({CARD COUNT}) {CARD}

        :return: A Card instance, the card that is played in this turn.
        """

        picked_card = choice(self.cards)
        self.history.append(picked_card)
        print(
            f"{str(self)} ({self.turn_count}) played: ({self.number_of_cards}) {str(picked_card)}"
        )
        self.cards.remove(picked_card)  # remove card from hand
        self.turn_count += 1  # increase player's turn count
        self.number_of_cards += 1  # increase player's card count

        return picked_card

    def __str__(self) -> str:
        """If name is set, returns name, else this returns 'Player N'"""
        if self.name:
            return self.name
        else:
            return f"Player {self.player_number}"


class Deck:
    """A deck of cards."""

    def __init__(self, cards: List[Card] = None):
        """Create a new deck of cards. Empty by default, but can be initialized
        with a starting hand.

        :param cards: Optional list of Card objects to start with.
        """

        self.cards: List[Card]
        if cards is not None:
            self.cards = cards
        else:
            self.cards = []

    def __str__(self) -> str:
        """
        :return: String with representation of every card in the deck.
        """
        return "Deck [" + ", ".join([str(card) for card in self.cards]) + "]"

    def fill_deck(self):
        """Fills cards with a complete deck of 52 cards. This replaces all cards
        already in the deck, so be careful."""

        self.cards = [
            Card(icon, value)
            for icon in ["♥", "♦", "♣", "♠"]
            for value in [
                "A",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
            ]
        ]

    def shuffle(self):
        """Shuffles all the cards in the deck."""
        shuffle(self.cards)

    def distribute(self, players: List[Player]):
        """Distributes the deck of cards between a given list of players. This
        happens in a one by one way, until all cards are used. The cards are
        moved from this deck to the players, so this function empties the deck.

        :param players: List of Player instances that get the cards.
        """
        player_idx = 0
        # Loop over the deck, giving every card to alternating players
        while len(self.cards) > 0:
            # move last card in deck to current player in list
            picked_card = self.cards.pop()
            players[player_idx].cards.append(picked_card)
            # loop index over players
            player_idx = (player_idx + 1) % len(players)
