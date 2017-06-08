#!/usr/bin/env python3

#
# queue.py
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

# Queue inhertis from the list class
class Queue(list):
    def enqueue(Q,key):
        Q.append(key)

    # Pop from the start of the list to emulate a queue
    def dequeue(Q):
        return super().pop(0)

    def is_empty(Q):
        return len(Q) == 0

def test():
    MIN = 2
    MAX = 2000

    n = []
    q = Queue()

    assert MAX >= MIN
    test_values = random.sample(range(MIN,MAX + 1), k = MAX - MIN + 1)

    for v in test_values:
        q.enqueue(v)

    while q:
        n.append(q.dequeue())

    assert n == test_values

if __name__ == '__main__':
    test()
    print ("All tests passed")
