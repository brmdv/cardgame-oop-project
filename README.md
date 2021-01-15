# OOP project in Python: Deck of cards 🃏

This is an exercise project, for practicing object-oriented programming in Python. The goal is to create a playing card game where the cards are represented by well-structured classes. Basic classes for card suits, cards, players, decks and games are implemented. 

In the basic "*must-have version*", a game just consists of distributing a full, shuffles deck of cards between all players and letting them play one card turn-by-turn until all cards are used. 

For the extra "*nice-to-have*" additions (which can be found in the branch `nice-to-have`) 

A detailed description of the assigment can be read [here](https://github.com/becodeorg/ANT-Theano-2-27/blob/main/2.python/2.python_advanced/01.OOP/5.oop_project.md). 

## Project file structure

* _utils/_
  * _card.py_
    * `Symbol`: This class describes a playing card symbol. Attributes are `icon` and `color`, the latter can be inferered from `icon`.
      * `.suit_from_name(name)`: a static method that can be used to get the Unicode character for card symbols by their English name. 
    * `Card(Symbol)`: Class that describes a playing card, by expanding `Symbol` with a playing card value.
  * _player.py_
    * `Player`: A class for a card player. Can be given a `name`  and a list of cards.
      * `.play()`: Pick a random card from player's hand and returns it. 
        
        
      * `.cards`: list with player's cards
      * `.history`: list with played card, in order
      * `.turn_count`
      * `.number_of_cards`: number of cards in hand
    * `Deck`: Class for a deck of cards. Can be initiated with provied list of cards, or be filled with a tradional deck of 52.
      * `.fill_deck()` : Fills the deck with 52 cards.
      * `.shuffle()`: Shuffles the deck randomly.
      * `.distribute([Player])`: Distributes all cards over a list of players. The cards are removed from the deck and moved to the players. 
        
      * `.cards`: list with all cards
  * _game.py_
    * `Board`: This class describes a game that is played. It contains the players, a deck of cards and all other components to represent the playing of the game.
      * `.start_game()`: Play a full game. See next section.
        
        
      * `.players`
      * `.turn_count`
      * `.active_cards`: Current cards in the turn.
      * `.history_cards`: All cards in order of playing, without the current turn
      * `.deck`: internal `Deck` object
* _main.py_: Here a game is started with four randomly-named players. 

## How a game is played

Each game takes place inside a `Board` instance. In *main.py* an example game takes place between four randomly-named players. 

1. A `Board` is initialised with players. 

2. A new deck is created and shuffled. Then it is distrubuted between all players. This is done card by card, so if the cards are not neatly divisible over the players, the last players get fewer cards.

3. As long as any player as cards left, a round is played. 
   
   1. First, the cards "on the table" (i.e. active cards) are moved to `.card_history`. 
   
   2. Every player then picks a card, which is then tranferred to the `Board.active_cards`. 
   
   3. In the *nice-to-have* branch, a winner is picked.
   
   4. 