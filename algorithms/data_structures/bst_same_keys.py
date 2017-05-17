#!/usr/bin/env python3

#
# bst_same_keys.py
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

# From exercise 12-1

class BstSameKeysNode(BstNode):
    def __init__(self,key,right=None,left=None,parent=None):
        super().__init__(key,right=None,left=None,parent=None)
        self.b = False

    def _print(self):
        super()._print()
        print("Boolean = " + str(self.b))
        print()

class BstSameKeys(Bst):
    def __init__(self,key):
        self.root = BstSameKeysNode(key)
        self.nodes = 1
        self.id = self

    def __set_root(self,root):
        if root is None:
            return self.root
        else:
            return root

    # Not sure about this one: putting x.b = ...
    # in the while loop leads to an is_bst() method
    # failure. So following is the possible right answer.
    def insert_based_on_b(self,key,root=None):
        x = self.__set_root(root)
        y = None
        z = BstSameKeysNode(key)

        # Find correct position for node z.
        while x is not None:
            y = x
            assert x.key == z.key
            if x.b is True:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y is not None and x is not None:
            assert x.parent is y

        # Was an empty tree.
        if y is None:
            self.root = z
        # Parent vertex connects to son.
        # Change the boolean of the parent only.
        else:
            assert z.key == y.key
            if y.b is True:
                y.b = False
                y.left = z
            else:
                y.b = True
                y.right = z

        self.nodes += 1


    #######
    #######
    #######
    #######


    # "Keep a list of nodes with equal keys at x, and insert z into the list."
    def insert_in_list():
        pass


    #######
    #######
    #######
    #######


    def insert_randomly(self,key,root=None):
        x = self.__set_root(root)
        y = None
        z = BstSameKeysNode(key)
        bool = random.choice([True, False])

        # Find correct position for node z.
        while x is not None:
            y = x
            assert x.key == z.key
            if bool is True:
               x = x.left
            else:
               x = x.right

        z.parent = y

        if y is not None and x is not None:
            assert x.parent is y

        # Was an empty tree.
        if y is None:
            self.root = z
        # Parent vertex connects to son.
        else:
            assert z.key == y.key
            if bool is True:
                y.left = z
            else:
                y.right = z

        self.nodes += 1

def test_a(samples,key):
    t = None

    t = BstSameKeys(key)

    for s in range(1,samples):
        t.insert(key)

    assert t.is_bst()

def test_b(samples,key):
    t = None

    t = BstSameKeys(key)

    for s in range(1,samples):
        t.insert_based_on_b(key)

    assert t.is_bst()


def test_c(samples,key):
    pass

def test_d(samples,key):
    t = None

    t = BstSameKeys(key)

    for s in range(1,samples):
        t.insert_randomly(key)

    assert t.is_bst()

# Test time for both implementations of insert
# Assert that time.insert_improve <= time.insert.
# This should be especially true if all the inserted keys are eual to
# eachother.
def test(tests,verbose=False):
    SAMPLES = 1000
    key = 15
    test_names = [ ]

    # You can comment out unwanted tests here.
    test_names.append("a")
    test_names.append("b")
    # test_names.append("c")
    test_names.append("d")
    benchmarks = dict()

    for t in test_names:
        setup = "from __main__ import test_" + t
        print ("Test " + t + "...")
        b = timeit.timeit("test_" + str(t) + "(" + str(SAMPLES) + "," + str(key) + ")", setup=setup, number=tests)
        benchmarks[t]=b

    for t in test_names:
        print(t + ": " + str(benchmarks[t]) + " seconds")

    if 'a' in benchmarks:
        assert benchmarks['a'] > benchmarks['b']
        assert benchmarks['a'] > benchmarks['d']

# Run n tests and check that the n lists returned are all equal to each other
# knowing that they have been generated randomly, they have the same size
# and the same unique keys. This means that the MAX - MIN + 1 numbers generated
# above are instered in the data structure randomly.
if __name__ == '__main__':
    TESTS = 50

    test(TESTS)
    print ("All tests passed")

