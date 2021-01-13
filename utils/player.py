from card import Card
from random import choice as random_choice


class Player:
    """A class for a card player."""

    player_count = 1  # player counter, starting at 1 because humans

    def __init__(self, cards: list, name: str = ""):
        """Create a new player.

        :cards: List of card.Card instances; the player's hand.
        :name: Player's name (optional).
        """

        self.cards = cards
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []
        self.name = name
        # Assign autoincrementing player number
        self.player_number = Player.player_count
        Player.player_count += 1

    def play(self) -> Card:
        """Play a turn. This method will return a random card from the player's hand, which is then added to the history and removed from the hand.
        A summary will be printed, in the form:
        {PLAYER'S NAME} ({TURN}) played: ({CARD COUNT}) {CARD}
        """

        picked_card = random_choice(self.cards)
        self.history.append(picked_card)
        print(
            f"{str(self)} ({self.turn_count}) played: ({self.number_of_cards}) {str(picked_card)}"
        )
        self.cards.remove(picked_card)  # remove card from hand
        self.turn_count += 1  # increase player's turn count
        self.number_of_cards += 1  # increase player's card count

        return picked_card

    def __str__(self) -> str:
        if self.name:
            return self.name
        else:
            return f"Player {self.player_number}"


# testing
# test_player1 = Player([Card("♥", "8"), Card("♣", "J")])
# test_player2 = Player([Card("♥", "A"), Card("♣", "10")], name="Bram")
# print(str(test_player1))
# print(str(test_player2))
# test_player1.play()
# test_player2.play()
# test_player2.play()
# help(Player)
# pass