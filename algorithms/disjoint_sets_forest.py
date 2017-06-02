#!/usr/bin/env python3

#
# disjoint_sets_forest.py
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

def make_set(key):
    return DisjointSetTree(key)

class DisjointSetTree():
    # Under these attributes a print set method is not possible.
    def __init__(T,key):
        T.parent = T
        T.rank = 0
        T.member = key
        T.id = T

    def _print(T):
        print("Node data:")
        print("==========")
        print("Node key: " + str(T.member))
        print("Node parent: " + str(T.parent))
        print("Node id: " + str(T.id))
        print()

    def find_set(T):
        # While T is not the tree root...
        if T is not T.parent:
            # ... go up in the tree
            T.parent = T.parent.find_set()
        return T.parent

    def link(T1,T2):
        if T1.rank > T2.rank:
            T2.parent = T1
        elif T1.rank < T2.rank:
            T1.parent = T2
        else:
            assert T1.rank == T2.rank
            # Choose a random parent and
            # increase previously chosen node rank by 1.
            value = random.choice([True, False])
            if value is True:
                T2.parent = T1
                T1.rank += 1
            else:
                T1.parent = T2
                T2.rank += 1

    # Union applies the two heuristics at once.
    def union(T1,T2):
        x = T1.find_set()
        y = T2.find_set()
        x.link(y)

def test_path_compression():
    s1 = make_set(1)
    s2 = make_set(2)
    s3 = make_set(3)
    s4 = make_set(4)

    # Prepare to check path compression heuristic (PCH).
    s2.parent = s1
    s3.parent = s2
    s4.parent = s3

    # Enable PCH.
    s4.find_set()

    # Check PCH.
    assert s4.parent is s1
    assert s3.parent is s1
    assert s2.parent is s1

def test_union_by_rank_simple():
    s1 = make_set(1)
    s2 = make_set(2)
    s3 = make_set(3)
    s4 = make_set(4)

    s2.union(s1)
    s3.union(s2)
    s4.union(s3)

    # Since there is a random choice in the first union
    # we have to add a condition in order for the assertions to
    # be valid
    assert s2.parent is s1 or s2.parent is s2
    assert s3.parent is s1 or s3.parent is s2
    assert s4.parent is s1 or s4.parent is s2

def test():
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

if __name__ == '__main__':
    test_path_compression()
    test_union_by_rank_simple()
    test()
    print("All test passed")
