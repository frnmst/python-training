#!/usr/bin/env python3

# 08.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays 
# (using input), compare them, print out a message of congratulations to the 
# winner, and ask if the players want to start a new game)
# Remember the rules:
#
#    Rock beats scissors
#    Scissors beats paper
#    Paper beats rock

playing = True
while playing:
    x = input("Player 1 move (p = paper, r = rock ,s = scissors): ")
    y = input("Player 2 move (p = paper, r = rock ,s = scissors): ")

    if x == 'p' and y == 'r':
        winner = 1
    elif x == 'r' and y == 'p':
        winner = 2
    elif x == 's' and y == 'p':
        winner = 1
    elif x == 'p' and y == 's':
        winner = 2
    elif x == 'r' and y == 's':
        winner = 1
    elif x == 's' and y == 'r':
        winner = 2
    elif x == y:
        winner = False
    else:
        pass

    if winner:
        print ("Player " + str(winner) + " won")
    else:
        print ("Even game")

    playing = input("play again? (y/n): ")
    if playing == 'y':
        playing = True
    else:
        playing = False
