# Rock Paper Scissors

This program simulates a game of Rock, Paper, Scissors between two 
Players, and reports both Player's scores each round. At the end of the game, it calculates the final scores and reports the winner. 

The game provides for both a human player, as well as computer players 
that implement different in-game strategies. The game can be adapted to 
allow for computer vs computer, human vs computer, or human vs human.

By default, though, it pairs a human player with a randomly selected 
computer strategy.

## Game Rules

Rock beats Scissors; Scissors beats Paper; Paper beats Rock

## Game Modes

Players will have the option of playing in either of 2 game modes.
+ Standard Player Mode
+ Set Rounds Mode

### Standard Player Mode
In the standard player mode, any player who gets three more points than 
the opponent wins the game. Game play will have as many rounds 
$(0 to \infty)$ as is required for a winner to emerge.

### Set Rounds Mode
Here, the player can decide a set amount of rounds for the game to run. 
Once that number is up, the game grinds to a halt and checks if there is
a clear winner. Any player with more points than the opponent is 
declared winner. If no player has more points, the game is tied.

## Player Types
There are three different types of computer players. These include:
+ _Random Player_: A computer player that randomly selects its move
+ _Reflect Player_: Copies the last move of its opponent
+ _Cycle Player_: Linearly moves through each potential move 

# Credits
This Project was done as part of the Udacity Intro to Programming 
Nanodegree