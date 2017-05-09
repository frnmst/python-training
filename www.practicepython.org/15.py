#!/usr/bin/env python3

# 15.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string, except
# with the words in backwards order.

def reverse_string(string):
    # strcpy (values not pointer)
    strr = string[0:len(string)]

    # strtok
    strr = strr.split(' ')

    # Reverse the order of the list of strings (not the single strings
    # internally)
    strr = strr[::-1]

    # Generate a single string using ASCII 32 as delimiter.
    strr = ' '.join(strr)

    return strr

def main():
    print(str(reverse_string(input('Input a "long" string: '))))

main()
