#!/usr/bin/env python3

# 16.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Write a password generator in Python. Be creative with how you generate 
# passwords - strong passwords have a mix of lowercase letters, uppercase 
# letters, numbers, and symbols. The passwords should be random, generating a 
# new password every time the user asks for a new password. Include your 
# run-time code in a main method.
# Ask the user how strong they want their password to be. For weak passwords, 
# pick a word or two from a list.

import random
import string

WEAK=SHORT=4
MEDIUM=8
STRONG=LONG=16
WEAK_PASSWORDS=['moon', 'mumble', 'password', 'pwd', 'pen', 'pencil', 'wargames']

TEST_LENGTH=1000

def gen_password(length):

    if length == SHORT:
        # C way (more or less)
        # return WEAK_PASSWORDS[random.randint(0,len(WEAK_PASSWORDS) - 1)]
        # Python way
        return random.choice(WEAK_PASSWORDS)
    elif length == MEDIUM:
        # Return a k sized list of elements chosen from the population with
        # replacement. If the population is empty, raises IndexError.
        return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=MEDIUM))
    else:
        return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=LONG))

def get_password_strength(strength):
    if strength == 'weak':
        return WEAK
    elif strength == 'medium':
        return MEDIUM
    elif strength == 'strong':
        return STRONG
    else:
        return False

def test():
    i = 0
    while i < TEST_LENGTH:
        print (gen_password(SHORT))
        print (gen_password(MEDIUM))
        print (gen_password(LONG))
        i+=1

def main():
    loop = True
    while loop:
        length = get_password_strength(input("Choose a password strength (weak/medium/strong): "))
        if(length):
            loop = False

    print(gen_password(length))

#test()
main()
