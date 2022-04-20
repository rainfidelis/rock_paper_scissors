#!/usr/bin/env python3
import random
import sys
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


class Player:
    """
    The Player class is the parent class for all of the Players in this game.
    It is a generic player that always plays rock.
    """
    def __init__(self) -> None:
        """
        Initializes the player class with a starting score of zero, a count
        of zero, and no moves.

        Count: Tracks how many times the player has made a move. Useful in the
        ReflectPlayer and CyclePlayer sub-classes.
        Score: Tracks every player's score for the duration of the game.
        _Move: Records the last move of each player.
        """
        self.score = 0
        self.count = 0
        self.my_move = ''
        self.their_move = ''

    def move(self):
        """
        Controls the move made by each player.
        """
        return 'rock'

    def learn(self, my_move, their_move):
        """
        Records the moves made by each player during each game round.
        """
        self.my_move = my_move
        self.other_move = their_move


class RandomPlayer(Player):
    """
    The Random Player class is a typical computer plaer class.
    It randomly selects a move on each call from the list of possible moves.
    """
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    """
    The Human Player class allows a human play the game by entering their
    desired move. The human input is validated against the list of
    possible moves.
    """
    def move(self):
        move = input("Rock, Paper, Scissors > ").lower()
        if move not in moves:
            move = self.move()
        return move


class ReflectPlayer(Player):
    """
    The Reflect Player class is a special type of computer player class.
    It 'remembers' the move the opponent played and plays that move in the
    next round. The first move is randomized.
    """
    def move(self):
        self.count += 1

        if self.count == 1:
            return random.choice(moves)
        elif self.count > 1:
            return self.other_move


class CyclePlayer(Player):
    """
    The Cycle Player class is also a special type of computer player class.
    It 'remembers' what move it played the last round, and moves to the next
    move in the queue for this round. For instance, if it played 'rock'
    this round, it'd play 'paper' next.

    The first move is randomized.
    """
    def move(self):
        self.count += 1

        if self.count == 1:
            return random.choice(moves)

        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def validator(ans, options):
    while True:
        if ans in options:
            break
        else:
            ans = input("You've entered an invalid input. Try again: ")
    return ans


class Game:
    """
    Defines the rules of game play and manages the game. The game has two
    optional game modes.

    1. Standard Play: This game mode only ends when a winner emerges.
    A player is considered a winner when they have 3 points more than their
    opponent.
    2. Set Round: In this game mode, the user can determine the number of
    rounds they wish to play. Once those rounds are complete, the game
    announces the winner, or announces a tie.
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        """
        Controls the game play for each round. Announces a winner for the round
        when there is one, or announces the result as a tie.
        Updates each player's score after each winning round.
        """
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            print("It's a tie!")
        elif beats(move1, move2):
            print("** PLAYER ONE WINS **")
            # update player 1 score
            self.p1.score += 1
        else:
            print("** PLAYER TWO WINS **")
            # update player 1 score
            self.p2.score += 1

        print(f"Score\tPlayer One: {self.p1.score}\t"
              f"Player Two: {self.p2.score}")

        # Record the last move by each player
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def standard_play(self, round=1):
        """
        For any player to win the round, they must have three points
        more than their opponent. The game only ends when a winner emerges.
        """
        while True:
            print(f"\nRound: {round}")
            self.play_round()

            if (self.p1.score - self.p2.score == 3):
                print("")
                print("Player One is ahead by three points and wins the game")
                break
            elif (self.p2.score - self.p1.score == 3):
                print("")
                print("Player Two is ahead by three points and wins the game")
                break
            else:
                round += 1
                continue

    def set_round(self):
        """
        Play for a fixed number of rounds. Calculates the winner once that
        number is complete.
        """
        while True:
            rounds = input("\nHow many rounds will you like to play? ")
            try:
                rounds = int(rounds)
                break
            except ValueError:
                print("You've not entered a valid number. Try again.")

        for round in range(rounds):
            round += 1
            print(f"\nRound: {round}")
            self.play_round()

        print("\nThe rounds are complete!")
        score_diff = self.p1.score - self.p2.score

        if score_diff > 0:
            print(f"Player One wins the game by {score_diff} points.")
        elif score_diff < 0:
            print(f"Player Two wins the game by {abs(score_diff)} points!")
        else:
            print(f"At the end of {rounds} rounds of play, the game is tied!")

    def play_game(self):
        """
        Controls the overall gameplay. Keeps the game running until a winner
        emerges. Starts a new game for as long as the user wants to play.
        """
        print(".............."*5)
        print("ROCK PAPER SCISSORS")
        print(".............."*5)

        print("\nWould you like to play a standard game or play a custom "
              "number of rounds?")
        ans = input("Enter [1 for standard] or [2 for custom]: ")
        valid_ans = validator(ans, options=['1', '2'])

        print("\nGame start!")
        if valid_ans == '1':
            print("\nNote: In standard mode, the game is won when a user has"
                  " three more points than their opponent.")
            self.standard_play()
        elif valid_ans == '2':
            self.set_round()

        again = input("\nWould you like to play again? [Yes/No]\n").lower()
        valid_ans = validator(again, options=['yes', 'no'])

        if valid_ans == 'yes':
            options = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]
            player2 = random.choice(options)
            game = Game(HumanPlayer(), player2)
            game.play_game()
        elif valid_ans == 'no':
            sys.exit("Thanks for playing. Goodbye!!")


if __name__ == '__main__':
    player2 = random.choice([RandomPlayer(), ReflectPlayer(), CyclePlayer()])
    game = Game(HumanPlayer(), player2)
    game.play_game()
