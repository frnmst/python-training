#!/usr/bin/env python3

# 05.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Get element intersection from generic lists.
# Sould be the naive way: O(n^2) + O(internal sorting) + O(search and remove duplicates)

import random

first = random.sample(range(100),10)
second = random.sample(range(100),20)
intersection = []

for i in first:
    if i in second:
        intersection.append(i)
        intersection.sort()
        if intersection.count(i) > 1:
             intersection.remove(i)

print("first = " + str(first))
print("second = " + str(second))
print("intersection = " + str(intersection))
