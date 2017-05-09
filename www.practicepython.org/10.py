#!/usr/bin/env python3

# 10.py
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

# We allow possible duplicates at first.
first_list=random.sample(range(100),10)
second_list=random.sample(range(100),20)
first_list.append(10)
first_list.append(10)
second_list.append(10)
second_list.append(10)
print(first_list)
print(second_list)

# Sets cannot contain duplicates by definition.
first = set()
second = set()
first.update(first_list)
second.update(second_list)
intersection = set()

# Two possible ways: operator and non operator version.
# This is possible for all the other operators also.
intersection = first.intersection(second)
intersection_operator = first & second

print(first)
print(second)
print(intersection)
print(intersection_operator)
