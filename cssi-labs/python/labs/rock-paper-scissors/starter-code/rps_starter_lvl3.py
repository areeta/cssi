#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random

def get_player_move():
    """Asks the user to enter a move as 'r', 'p', or 's', and return it"""
    # TODO
    user_move = input("Enter a move as 'r', 'p', or 's': ")
    return user_move

def get_computer_move():
    """Randomly generates the computer's move and
    returns it in the form of 'r', 'p', or 's'"""
    # TODO
    computer_move = random.randint(0,2)
    if computer_move == 0:
        return "r"
    elif computer_move == 1:
        return "p"
    elif computer_move == 2:
        return "s"

def determine_winner(player_move, comp_move):
    """Takes in a player move and computer move each as 'r', 'p', or 's',
    and returns the winner as 'player', 'computer', or 'tie'"""
    # TODO

    if player_move == "r" and comp_move == "p":
        return "computer"
    elif player_move == "r" and comp_move == "s":
        return "player"
    elif player_move == "s" and compr_move == "r":
        return "computer"
    elif player_move == "s" and comp_move == "p":
        return "player"
    elif player_move == "p" and comp_move == "r":
        return "player"
    elif player_move == "p" and comp_move == "s":
        return "computer"
    elif player_move == comp_move:
        return "tie"

def print_scoreboard(player_wins, comp_wins, ties):
    """Prints out the scoreboard neatly.  Returns nothing."""
    # TODO
    print "Player has won #" + str(player_wins) + " time(s)."
    print "Computer has won #" + str(comp_wins) + " time(s)."
    print "There has been #" + str(ties) + " tie(s)."

def get_move_name(short_move):
    """Takes in 'r', 'p', or 's', and returns 'Rock', 'Paper, or
    'Scissors' respectively. Use this to neatly print move choices"""
    # TODO
    if short_move == "r":
        print("Rock")
    elif short_move == "p":
        print("Paper")
    elif short_move == "s":
        print("Scissors")

# Write your code below - make RPS happen using the functions above!

amount_of_plays = input("How many times do you want to play Tic Tac Toe? ")
player_wins = 0
computer_wins = 0
ties = 0

for x in range(amount_of_plays):
    # this is just "r" or "s" or "p"
    player_short = get_player_move()
    computer_short = get_computer_move()

    # this is the longer version of "r" or "s" or "p"
    print "Player's move was "
    player = get_move_name(player_short)

    print "Computer's move was "
    computer = get_move_name(computer_short)

    winner = determine_winner(player_short, computer_short)

    if winner == "player":
        player_wins += 1
    elif winner == "computer":
        computer_wins += 1
    elif winner == "tie":
        ties += 1

    print_scoreboard(player_wins, computer_wins, ties)

print_scoreboard(player_wins, computer_wins, ties)
