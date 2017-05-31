#!/usr/bin/env python3

#
# bst_radix.py
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
import timeit
from bst import Bst, BstNode

# From exercise 12-2
#
# A radix tree for an alphabet of |sigma| = 2 (two symbols)
# implies that all the possible strings can be originated by a binary tree.
SIGMA = ['0', '1']


###
### NOTE: There is no bst here. It's just a proof of concept.
###

# a < b?
def rule_1(a,b,p,q):
    j =  min(p,q)
    if a[0:j-1] == b[0:j-1] and a[j] < b[j]:
        return True
    else:
        return False

def rule_2(a,b,p,q):
    if p < q and a[0:p] == b[0:p]:
        return True
    else:
        return False

def a_lt_b(a,b,p,q):
    if rule_1(a,b,p,q) or rule_2(a,b,p,q):
        return True
    else:
        return False

# Same examples as in the book.
def test_poc():
    a1 = "10100"
    b1 = "10110"
    p1 = 3
    q1 = 3

    a2 = "10100"
    b2 = "101000"
    p2 = len(a2)-1
    q2 = len(b2)-1

    assert a_lt_b(a1,b1,p1,q1) and a_lt_b(a2,b2,p2,q2)

# Test time for both implementations of insert
# Assert that time.insert_improve <= time.insert.
# This should be especially true if all the inserted keys are eual to
# eachother.
def test(tests,verbose=False):
    test_poc()

# Run n tests and check that the n lists returned are all equal to each other
# knowing that they have been generated randomly, they have the same size
# and the same unique keys. This means that the MAX - MIN + 1 numbers generated
# above are instered in the data structure randomly.
if __name__ == '__main__':
    TESTS = 50

    test(TESTS)
    print ("All tests passed")

