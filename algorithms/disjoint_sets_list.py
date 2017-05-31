#!/usr/bin/env python3

#
# disjoint_sets_list.py.py
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

MIN_KEY = 1
MAX_KEY = 10000

class LinkedListNode():
    def __init__(N,set,key):
        N.set = set
        N.member = key
        N.next = None
        N.id = N

    def _print(N):
        print("Node data:")
        print("==========")
        print("Node belongs to: " + str(N.set))
        print("Node key: " + str(N.member))
        print("Node next: " + str(N.next))
        print("Node id: " + str(N.id))
        print()

    # O(1)
    def find_set(N):
        return N.set


# An alias so that we can use the "make_set" function just like in the book.
def make_set(key):
    return DisjointSetList(key)

class DisjointSetList():

    def __init__(S,key):
        S.head = LinkedListNode(set=S,key=key)
        S.tail = S.head
        S.id = S

    def _print(S):
        print("Set data:")
        print("=========")
        print("Set head: " + str(S.head))
        print("Set tail: " + str(S.tail))
        print("Set id: " + str(S.id))
        print()

    # Since it's a custom type of list, iteration must be manual.
    # This means that we can't use the for construct.
    def union(S1,S2):
        # Change set belongs attribute for each object in S2.
        head = S2.head
        while head is not None:
            head.set = S1
            head = head.next

        # Append S2 to S1
        S1.tail.next = S2.head

        # Fix S1 tail to be the last element of S2.
        S1.tail = S2.tail

        # Destroy the second set
        S2 = None

    ###               ###
    ### Extra methods ###
    ###               ###

    def _print_set(S):
        head = S.head
        print("Full list")
        print("=========")
        while head is not None:
            head._print()
            head = head.next

    def length(S):
        head = S.head
        length = 0
        while head is not None:
            length += 1
            head = head.next

        return length

def test_static():
    s1 = make_set(1)
    s2 = make_set(2)
    s3 = make_set(3)
    s4 = make_set(4)

    assert s1.head.find_set() is s1
    assert s2.head.find_set() is s2

    s1.union(s2)
    s3.union(s4)

    assert s1.length() == s3.length()

    assert s1.head.next.next is None
    assert s3.head.next.next is None

    #s1._print_set()

    # assert s2 is None

    #s1._print_set()
    s1.union(s3)
    #s3._print_set()

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
        S[i].union(S[i-1])

    # make set + union operations
    m = n + n - 1

    # The last set has all the keys.
    assert S[n-1].length() == n

    print("Total operations: " + str(m))
    print("Running time: theta(" + str(n) + "^2), because of all the updates \
in each union operation.")

if __name__ == '__main__':
    test_static()
    test_random()
    print("All test passed")
