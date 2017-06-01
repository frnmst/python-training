#!/usr/bin/env python3

#
# disjoint_sets_list_weighted.py
#
# python-training/algorithms (c) 2017 by Franco Masotti
#                            <franco.masotti@student.unife.it>
#
# To the extent possible under law, the person who associated CC0 with
# python-training/algorithms has waived all copyright and related or 
# neighboring rights to python-training/algorithms. This software is 
# distributed without any warranty.
#
# You should have received a copy of the CC0 legalcode along with this
# software.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.

import random
import math

MIN_KEY = 1
MAX_KEY = 1000

from disjoint_sets_list import DisjointSetList

# An alias so that we can use the "make_set" function just like in the book.
def make_set(key):
    return DisjointSetListWeighted(key)

class DisjointSetListWeighted(DisjointSetList):

    def __init__(S,key):
        super().__init__(key)
        S.len = 1

    def _print(S):
        super()._print()
        print("Set length: " + str(S.len))
        print()

    # Since it's a custom type of list, iteration must be manual.
    # This means that we can't use the for construct.
    def union(S1,S2):

        if S2.len <= S1.len:
            head = S2.head
            while head is not None:
                head.set = S1
                head = head.next

            S1.tail.next = S2.head
            S1.tail = S2.tail
            S1.len += S2.len
            S1.tail.next = None

            # This should suffice, however since this is a local scope, it 
            # won't work outside this method...
            S2 = S1

            # ... so we need to return the value and reassign it.
            return S1

        elif S1.len < S2.len:
            head = S1.head
            while head is not None:
                head.set = S2
                head = head.next

            S2.tail.next = S1.head
            S2.tail = S1.tail
            S2.len += S1.len
            S2.tail.next = None

            S1 = S2

            return S2

def test_static():
    s1 = make_set(1)
    s2 = make_set(2)
    s3 = make_set(3)
    s4 = make_set(4)

    assert s1.head.find_set() is s1
    assert s2.head.find_set() is s2

    s = s1.union(s2)
    s = s3.union(s)
    s = s.union(s4)
    print (s3 is s4)

    s1._print_set()

def test_random():

    random_keys = random.sample(range(MIN_KEY,MAX_KEY + 1)\
                                , k = MAX_KEY - MIN_KEY + 1)

    n = len(random_keys)

    S = []

    for k in random_keys:
        S.append(make_set(k))

    # Put all elements in same set.
    # This means that we must perform n-1 unions where
    # n is the starting number of sets.
    for i in range(1,n):
        S[i] = S[i].union(S[i-1])

    for i in range(1,n):
        assert S[i].len == n

if __name__ == '__main__':
    test_static()
    test_random()
    print("All test passed")
