# tic-tac-toe
Created a tic-tac-toe game from scratch in Python.

game.py is the base game; handles user input and displays tic-tac-toe board
from the terminal. Computer move is based on a random number generator. With 
with the squares of the board being labeled 1-9 from top to bottom and left
to right.

game_ImprovedComputer.py is the more advanced game; the only difference from
the base is the computer now makes decisions based off of winning configurations
and what the user has previously played. A frequency table is used for the computer
to choose a square based on the relative frequency of that square being a part of
a winning configuration.

Next step is to add a gui for a better user experience.

Might try to add ML to this to get a more advanced computer player. (I've never used ML before)
I don't know if ML would add anything to this. It shouldn't be possible to beat
the computer with how it is set up now.

Each new game file will be an improved version of the game.
