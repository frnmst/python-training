#!/usr/bin/env python3

#
# bst_sort.py
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

from bst import Bst, BstNode

class BstSort(Bst):
    def insert(T,key,root=None):
        x = T.root
        y = None
        z = BstNode(key)
        # Find correct position for node z.
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y is not None and x is not None:
            assert x.parent is y

        # Was an empty tree.
        if y is None:
            T.root = z
        # Parent vertex connects to son.
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        T.nodes += 1


def test(verbose=False):
    MIN = 1
    MAX = 500

    t = None

    assert MAX >= MIN
    test_values = random.sample(range(MIN,MAX + 1), k = MAX - MIN + 1)

    for v in test_values:
        if t is None:
            t = BstSort(v)
        else:
            t.insert(v)

# Run n tests and check that the n lists returned are all equal to each other
# knowing that they have been generated randomly, they have the same size
# and the same unique keys. This means that the MAX - MIN + 1 numbers generated
# above are instered in the data structure randomly.
if __name__ == '__main__':
    TESTS = 100
    verbose = False
    s = []

    s.append(test())

    for t in range(1,TESTS):
        s.append(test())
        assert s[t-1] == s[t]
    print ("All tests passed")

