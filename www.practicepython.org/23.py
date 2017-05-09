#!/usr/bin/env python3

# 23.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Given two .txt files that have lists of numbers in them, find the numbers
# that are overlapping. One .txt file has a list of all prime numbers under 1000, and
# the other .txt file has a list of happy numbers up to 1000.
# (If you forgot, prime numbers are numbers that can’t be divided by any other
# number. And yes, happy numbers are a real thing in mathematics - you can look
# it up on Wikipedia. The explanation is easier with an example, which I will
# describe below.)

# I have chosen the naive way. But you can also use sets:
# sp = set of the prime numbers
# sh = set of the happy numbers
# sc = sp U sh (intersection)
# You can also the following (also in list comprehensions):
#
# for p in primeslist
#   if p im happylist
#       duplicates.append(p)
#
# This method hash (possibly) a hidden for
# loop with the "if .. in .." construct.
# If the latter is true, the complexity is O(len(primeslist) * 
# len(happylist))

# Load the two lists
def load_file(filename):
    list = []
    with open(filename) as f:
        for line in f:
            list.append(int(line.strip()))

    return list

def get_duplicates(ordered_list):
    duplicates = []
    # Invariants should be ok.
    i = 1
    while i < len(ordered_list) and len(ordered_list) > 1:
        if ordered_list[i-1] == ordered_list[i]:
            duplicates.append(ordered_list[i])
        i += 1

    return duplicates

# Run and have a look at the ./23.sh script
if __name__ == '__main__':
    p = load_file('primenumbers.txt')
    h = load_file('happynumbers.txt')
    s = sorted(p + h)
    d = get_duplicates(s)
    print(d)
    print("Number of duplicates = " + str(len(d)))
