#!/usr/bin/env python3

#
# disjoint_sets_benchmarks.py
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

from disjoint_sets_list import DisjointSetList
from disjoint_sets_list_weighted import DisjointSetListWeighted
from disjoint_sets_forest import DisjointSetTree

MIN_KEY = 1
MAX_KEY = 5000
TESTS = 10

class DisjointSetsTest():
    def __init__(T):
        T.keys = random.sample(range(MIN_KEY,MAX_KEY + 1)\
                        , k = MAX_KEY - MIN_KEY + 1)

    # Notice the running time if list compared to the other two.
    # There is a HUGE improvement by appending the shorter list
    # to the longer list, while a small improvement in using
    # the tree implementation with the two heuristics, by doing
    # progressive union operations in all cases.
    def list(T):
        S = []

        for k in T.keys:
            S.append(DisjointSetList(k))

        for i in range(1,len(T.keys)):
            S[i].union(S[i-1])

    def list_weighted(T):
        S = []

        for k in T.keys:
            S.append(DisjointSetListWeighted(k))

        for i in range(1,len(T.keys)):
            S[i] = S[i].union(S[i-1])

    def tree(T):
        S = []

        for k in T.keys:
            S.append(DisjointSetTree(k))

        for i in range(1,len(T.keys)):
            S[i].union(S[i-1])

def test(tests):
    test_names = [ ]
    test_names.append("list")
    test_names.append("list_weighted")
    test_names.append("tree")
    benchmarks = dict()
    setup ='''from __main__ import DisjointSetsTest'''

    for t in test_names:
        print ("Test " + t + "...")
        b = timeit.timeit("T = DisjointSetsTest()" + '\n' + "T." + str(t) + "()", setup=setup, number=tests)
        benchmarks[t]=b

    for t in test_names:
        print(t + ": " + str(benchmarks[t]) + " seconds")

    if MAX_KEY > 100:
        assert benchmarks['list'] >= benchmarks['list_weighted']
        assert benchmarks['list'] >= benchmarks['tree']

if __name__ == '__main__':
    test(TESTS)
    print("All tests passed")
