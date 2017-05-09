#!/usr/bin/env python3

# 20.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Write a function that takes an ordered list of numbers (a list where the
# elements are in order from smallest to largest) and another number. The
# function decides whether or not the given number is inside the list and
# returns (then prints) an appropriate boolean.
# Extras: Use binary search.

import math

# No guarantee for this to work if the test is changed.
# What's more is that it does not work for duplicates.
def get_excluded_list(list):
    excluded = []

    for element in list:
        excluded.append((element*11) - 7)

    return excluded

def bin_search(list,min,max,key):
    if (min <= max):
        mid = math.floor((min+max) / 2)

        if key == list[mid]:
            return True
        elif key > list[mid]:
            # We have already examined mid so we can exclude it from the next
            # searches.
            return bin_search(list,mid+1,max,key)
        elif key < list[mid]:
            return bin_search(list,min,mid-1,key)
    else:
        return False

def bin_search_iterative(list,key):
    min = 0
    max = len(list) - 1
    while min <= max:
        mid = math.floor((min+max) / 2)
        if key == list[mid]:
            return True
        elif key > list[mid]:
            min = mid+1
        elif key < list[mid]:
            max = mid-1

    return False

# Linear search in python
def linear_search_py(list,key):
    return list.count(key) >= 1

def linear_search(list,key):
    for e in list:
        if e == key:
            return True
    return False

def test():
    test_list = [2,3,5,7,11,13,17,19,23]
    min = 0
    max = len(test_list) - 1

    # Sort in case someones edits it. If it's not sorted bin search will fail.
    test_list.sort()

    for k in test_list:
        assert bin_search(test_list,min,max,k)
        assert bin_search_iterative(test_list,k)
        assert linear_search(test_list,k)
        assert linear_search_py(test_list,k)
    for k in get_excluded_list(test_list):
        assert not bin_search(test_list,min,max,k)
        assert not bin_search_iterative(test_list,k)
        assert not linear_search(test_list,k)
        assert not linear_search_py(test_list,k)

    print ("All tests passed")

if __name__ == "__main__":
    test()
