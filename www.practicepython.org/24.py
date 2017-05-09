#!/usr/bin/env python3

# 24.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Time for some fake graphics! Let’s say we want to draw game boards that look 
# like this:
#
# --- --- --- 
#|   |   |   | 
# --- --- ---  
#|   |   |   | 
# --- --- ---  
#|   |   |   | 
# --- --- --- 
#
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other 
# sizes (8x8 for chess, 19x19 for Go, and many more).
# Ask the user what size game board they want to draw, and draw it for them to 
# the screen using Python’s print statement.

def get_board_size(game_id):
    if game_id == "chess":
        return 8
    elif game_id == "tic-tac-toe":
        return 3
    elif game_id == "go":
        return 19
    else:
        try:
            int(game_id)
            return int(game_id)
        except ValueError:
            return False

# Solution found with size = 2 and size = 3
# using pen and paper to find generic properities and patterns.
def draw_board(size):
    for r in range(0,(size*2) + 1):
        if r % 2 == 0:
            print(size * " ---")
        else:
            print((size + 1) * "|   ")

# Run and have a look at the ./23.sh script
if __name__ == '__main__':
    s = input("What game board do you want to display (tic-tac-toe, chess, go, \
<square input size>): ")
    while not s:
        s = input("What game board do you want to display (tic-tac-toe, chess, \
go, <square input size>): ")

    draw_board(get_board_size(s))
