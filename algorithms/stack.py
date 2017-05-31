#!/usr/bin/env python3

#
# stack.py
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

# Stack inhertis from the list class
class Stack(list):
    def push(S,key):
        S.append(key)

    # super().method(arg)
    # This does the same thing as:
    # super(C, S).method(arg)
    def pop(S):
        return super().pop()

def test():
    MIN = 2
    MAX = 2000

    n = []
    s = Stack()

    assert MAX >= MIN
    test_values = random.sample(range(MIN,MAX + 1), k = MAX - MIN + 1)

    for v in test_values:
        s.push(v)

    while s:
        n.append(s.pop())

    n.reverse()
    assert n == test_values

if __name__ == '__main__':
    test()
    print ("All tests passed")
