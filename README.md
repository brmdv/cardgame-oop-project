# OOP project in Python: Deck of cards 🃏

This is an exercise project, for practicing object oriented programming in Python. The goal is to create a playing card game where the cards are being represented by well-structured classes. 

## Project file structure

* _utils/_
	* _card.py_
		* `Symbol`: This class describes a playing card symbol.
		* `Card(Symbol)`: Class that describes a playing card, by expanding `Symbol` with a playing card value.
	* _player.py_
		* `Player`: A class for a card player.
		* `Deck`: Class for a deck of cards. 
	* _game.py_
		* `Board`: This class describes a game that is played. I contains the players, a deck of cards and all other components to represent the playing of the game.
* _main.py_: Here a game is started with four randomly named players. 

## How a game is played
