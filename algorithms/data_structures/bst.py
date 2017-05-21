#!/usr/bin/env python3

#
# bst.py
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
from stack import Stack
from queue import Queue

class BstNode:
    def __init__(T,key,right=None,left=None,parent=None):
        T.key = key
        T.right = right
        T.left = left
        T.parent = parent
        T.id = T

    def _print(T):
        print("Node data")
        print("=========")
        print("ID = " + str(T.id))
        print("Key = " + str(T.key))
        print("Right = " + str(T.right))
        print("Left = " + str(T.left))
        print("Parent = " + str(T.parent))
        print()

    def edit(T,key,right=None,left=None,parent=None):
        T.key = key
        T.right = right
        T.left = left
        T.parent = parent

# Using iterative functions we avoid the mess.

# insert, search, min, max, successor, predecessor can be used with subtrees. 
# That's why they are supplied with an extra root argument.

# min, max, successor, predecessor are defined on nodes, not keys.
class Bst:
    # Start with an empty BST:
    #   push in a node with a specified key as root
    # Attributes:
    #   root:   pointer to the root node
    #   nodes:  number of nodes currently in the tree
    #   id:     pointer to object itT
    def __init__(T,key):
        T.root = BstNode(key)
        T.nodes = 1
        T.id = T

    def _set_root(T,root):
        if root is None:
            return T.root
        else:
            return root

    def _print(T):
        print("Tree summary")
        print("=========")
        print("ID = " + str(T.id))
        print("root = " + str(T.root))
        print("Nodes = " + str(T.nodes))
        print()

    def insert(T,key,root=None):
        x = T._set_root(root)
        y = None
        z = BstNode(key)
        # Find correct position for node z.
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                assert z.key >= x.key
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

    def search(T,key,root=None):
        x = T._set_root(root)
        found = False
        while not found and x is not None:
            if key == x.key:
                found = True
            elif key < x.key:
                x = x.left
            else:
                x = x.right

        return x

    def min(T,root=None):
        x = T._set_root(root)
        while x.left is not None:
            x = x.left

        return x

    def max(T,root=None):
        x = T._set_root(root)
        while x.right is not None:
            x = x.right

        return x

    def successor(T,root=None):
        x = T._set_root(root)
        if x.right is not None:
            return T.min(x.right)
        y = x.parent
        while y is not None and x is y.right:
            x = y
            y = y.parent
        return y

    def predecessor(T,root=None):
        x = T._set_root(root)
        if x.left is not None:
            return T.max(x.left)
        y = x.parent
        while y is not None and x is y.left:
            x = y
            y = y.parent
        return y

    def preorder(T,root=None):
        x = T._set_root(root)
        s = Stack()
        s.push(x)
        while s:
            x = s.pop()
            x._print()
            if x.right is not None:
                s.push(x.right)
            if x.left is not None:
                s.push(x.left)

    # An alternative inorder version that iterates over the tree the same way 
    # the recirsive version does.
    def inorder(T,root=None):
        x = T._set_root(root)
        s = T.min(x)
        s._print()
        for i in range(1, T.nodes):
            prev = s.key
            s = T.successor(s)
            # assert prev == s.key - 1
            s._print()

    # Move v (and its descendants) in u's position
    # This can also be used for trivial operations
    def transplant(T,u,v,root=None):
        assert u is not None
        x = T._set_root(root)

        if u.parent is None:
            T.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else: # u is u.parent.right
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    # Runs in O(h)
    def delete(T,z):
        if z.left is None:
            T.transplant(z,z.right)
        elif z.right is None:
            T.transplant(z,z.left)
        else:
            assert z.right is not None and z.left is not None

            # y = T.min(z.right) # which is the same as the successor.
            y = T.successor(z)

            if y.parent is not z:
                T.transplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            T.transplant(z,y)
            y.left = z.left
            y.left.parent = y

        T.nodes -= 1

    # Use a slightly modified version of the inorder algorithm.
    def is_bst(T,root=None):
        x = T._set_root(root)
        s = T.min(x)
        for i in range(1, T.nodes):
            prev = s
            s = T.successor(s)
            if prev.key > s.key:
                return False

        return True

    # Compute the normal height.
    # See http://www.geeksforgeeks.org/iterative-method-to-find-height-of-binary-tree/
    def h(T,root=None):
        x = T._set_root(root)
        q = Queue()
        q.enqueue(x)
        height = 0
        found = False

        # Safety first.
        if x is None:
            return 0

        while not found:
            nodes = len(q)

            if nodes == 0:
                found = True
            else:
                height += 1

            while nodes > 0 and not found:
                n = q.dequeue()
                assert n is not None
                if n.left is not None:
                    q.enqueue(n.left)
                if n.right is not None:
                    q.enqueue(n.right)
                nodes -= 1

        return height


def test(verbose=False):

    t = None

    assert MAX >= MIN
    test_values = random.sample(range(MIN,MAX + 1), k = MAX - MIN + 1)

    for v in test_values:
        if t is None:
            t = Bst(v)
        else:
            t.insert(v)

    assert t.search(MAX).key == MAX
    assert t.search(MIN).key == MIN

    assert t.max().key == MAX
    assert t.min().key == MIN

    if MAX != MIN:
        assert t.successor(t.min()).key == MIN + 1
        assert t.predecessor(t.max()).key == MAX - 1

    if verbose:
        t.preorder()
        t.inorder()
        t._print()

    assert t.is_bst()

    print(t.h())

    for v in test_values:
        if verbose:
            print(v)
        t.delete(t.search(v))

    if verbose:
        t._print()

    assert t.nodes == 0 and t.root is None

def test_static():
    t = Bst(1)
    t.insert(0)
    t.insert(2)
    t.insert(3)
    t.insert(6)
    t.insert(8)
    t.insert(2)

    t.preorder()
    # t.inorder()

    t.transplant(t.search(0),t.search(8))
    print("After transplant")
    t.preorder()

# Check if height function computes correcly for the unbalanced case. Assume it
# works for every case.
def test_unbalanced():
    t = Bst(MIN)
    for k in range(MIN + 1, MAX + 1):
        t.insert(k)

    assert t.h() == MAX - MIN + 1

# Key range.
MIN = 1
MAX = 500

if __name__ == '__main__':
    # Since there are n keys which can be permutated, this leads to n! possible
    # BSTs. We don't know how the PRNG pick the numbers but most certainly 
    # there might be repetitions.
    # TESTS = math.factorial(MAX-MIN+1)
    TESTS = 100
    verbose = False

    print ("Executing " + str(TESTS) + " tests on keys between " + str(MIN) + " and " + str(MAX) + ".")
    for t in range(0,TESTS):
        test_unbalanced()
        test_static()
        test(verbose)
    print ("All tests passed")

