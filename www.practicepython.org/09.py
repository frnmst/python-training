#!/usr/bin/env python3

# 09.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to 
# guess the number, then tell them whether they guessed too low, too high, or 
# exactly right. Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, 
# print this out.

import random

MIN = 1
MAX = 100

global_attempts = 0
matches = 0
playing = True
while playing:
    match = True
    attempts = 0
    cgnumber = random.randint(MIN,MAX)
    while match:
        # print(cgnumber)
        while True:
            guess = int(input ("Your guess between " + str(MIN) + " and " + str(MAX) + " : "))
            if guess <= MAX and guess >= MIN:
                break

        attempts += 1
        if guess > cgnumber:
            print ("Too high try with a smaller number")
        elif guess < cgnumber:
            print ("Too small try with a bigger number")
        else:
            match = False
            print ("You won")

        print("You made " + str(attempts) + " attemps so far")

    global_attempts += attempts
    matches += 1

    playing = input('Type "exit" to quit the game: ')
    if playing == "exit":
        playing = False
    else:
        playing = True

print ("guesses were " + str(global_attempts) + " on " + str(matches) + " matches")
print ("Your winning ratio was " + str((matches/global_attempts) * 100) + "%")
