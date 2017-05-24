#!/usr/bin/env python3

#
# rbt.py
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
import timeit

from bst import Bst
from rbt import Rbt

MIN_KEY = 1
MAX_KEY = 5000


class Test():
    def __init__(T):
        T.random_keys = random.sample(range(MIN_KEY,MAX_KEY + 1)\
                        , k = MAX_KEY - MIN_KEY + 1)

    def insert_progressive(T):
        pass

    def search(T):
        pass

    def delete(T):
        pass

    def bst_progressive(T):
        t = Bst(MIN_KEY)

        for k in range(MIN_KEY + 1, MAX_KEY + 1):
            t.insert(k)

    def bst_random(T):
        t = None

        for r in T.random_keys:
            if t is None:
                t = Bst(r)
            else:
                t.insert(r)

    def rbt_progressive(T):
        t = Rbt()

        for k in range(MIN_KEY, MAX_KEY + 1):
            t.insert(k)

    def rbt_random(T):
        t = Rbt()
        for k in T.random_keys:
            t.insert(k)

def test(tests):
    test_names = [ ]
    test_names.append("bst_progressive")
    test_names.append("rbt_progressive")
    test_names.append("bst_random")
    test_names.append("rbt_random")
    benchmarks = dict()
    setup ='''from __main__ import Test'''

    for t in test_names:
        print ("Test " + t + "...")
        b = timeit.timeit("T = Test()" + '\n' + "T." + str(t) + "()", setup=setup, number=tests)
        benchmarks[t]=b

    for t in test_names:
        print(t + ": " + str(benchmarks[t]) + " seconds")

    if 'bst_progressive' in benchmarks and 'rbt_progressive' in benchmarks and MAX_KEY > 1024:
        assert benchmarks['bst_progressive'] >= benchmarks['rbt_progressive']

if __name__ == '__main__':
    TESTS = 20

    test(TESTS)
    print("All tests passed")
