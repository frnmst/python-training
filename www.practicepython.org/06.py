#!/usr/bin/env python3

# 06.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Ask the user for a string and print out whether this string is a palindrome or
# not. (A palindrome is a string that reads the same forwards and backwards.)

string_input = input("Input a string and I'll tell you if it's palindriome: ")

# See extended slices https://docs.python.org/2/whatsnew/2.3.html#extended-slices
print(string_input)
print(string_input[::-1])

# Not efficient but very simple to understand.
if string_input == string_input[::-1]:
    print("is palindrome")
else:
    print("is NOT palindrome")
