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
from queue import Queue

# Constants
black = "black"
red = "red"
Null = object()

class RbtNode(BstNode):
    def __init__(T,key,color=black,right=None,left=None,parent=None):
        super().__init__(key,right,left,parent=None)
        T.color = color

    def _print(T):
        super()._print()
        print("Color = " + str(T.color))
        print()

# A Nil node is always black and we don't care about the value of the key 
# (which has been chosen to be -1)
class NilNode(RbtNode):
    def __init__(T,right=None,left=None,parent=None):
        super().__init__(-1,black,right,left,parent)

class Rbt(Bst):
    # Only one Nil sentinel is available. This saves us an inredible amount of
    # space for "big" trees
    def __init__(T):
        #T.sentinel = NilNode()
        #T.root = RbtNode(key=key,color=black,right=T.sentinel,left=T.sentinel)
        #T.sentinel.right = T.sentinel.left = T.sentinel.parent = T.root
        #T.nodes = 1
        #T.id = T
        T.sentinel = NilNode()
        T.root = None
        T.sentinel.right = T.sentinel.left = T.sentinel.parent = T.root
        T.nodes = 1
        T.id = T

    def _set_root_null(T,root):
        if root is Null:
            return T.root
        else:
            return root

    # In the rotations only the beta son node (x.r or y.l) is exchanged between
    # x and y. Complexities for both rotations is O(1)
    def rotate_left(T,root=None):
        x = super()._set_root(root)
        y = x.right

        if y.left is not T.sentinel:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is T.sentinel:
            T.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(T,root=None):
        y = super()._set_root(root)
        x = y.left

        if x.right is not T.sentinel:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is T.sentinel:
            T.root = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def insert(T,key,root=None):
        y = T.sentinel
        x = super()._set_root(root)
        z = RbtNode(key=key,color=black)

        # Find the correct position for z, just like in the BST insert method.
        while y is not T.sentinel:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
            assert y is x.parent

        z.parent = y

        if y is T.sentinel:
            assert T.root is None
            T.root = z
        # Fixup z position in relation to its parent y.
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = z.right = T.sentinel
        z.color = red
        T.insert_fixup(z)

    def insert_fixup(T,z):
        pass

    # Black height of Rbt is black height of root node
    # Leaf nodes have black height 0.
    # The recursive way seems much simpler here.
    # This function also checks if the bh propriety is valid for the input tree 
    # by returning a boolean
    def bh(T,root=Null,compare=False):
        root = T._set_root_null(root)
        v = 0

        # No root: black height is 0 (base case)
        if root is None or root is T.sentinel:
            if compare:
                return True
            else:
                return 0
        else:
            # Increase black height if current node is black and it's not a
            # Leaf (a Nil node).
            if root.color is black and root is not T.sentinel:
                v = 1
            else:
                v = 0

            if compare:
                # Two numbers which correspond to left and
                # right local heights. If these two numbers correspond it means
                # that it's a valid RBT.
                # Assert black height propriety.
                return v + T.bh(root.left) == v + T.bh(root.right)
            else:
                return v + T.bh(root.left)

    def is_rbt(T,root=None):
        x = super()._set_root(root)

        # An empty RBT is a valid RBT.
        if x is None:
            return True

        # Root must be black
        if x.color is not black:
            return False

        # For each node y, bh(y) must be the same for every simple path from y 
        # to the leaves.
        #
        # Hack: since the root is connected to all the other nodes of the tree,
        # this propriety can be checked for the root only. We also know that 
        # the black height of the root is the same for every path.
        if not T.bh(compare=True):
            return False

        # For each red node z, z.left and z.right must be black nodes.

        # It's an RBT if all the checks pass.
        return True

def test(verbose=False):
    #x = Rbt(1)
    x = Rbt()

    #assert x.root.left is not None and x.root.right is not None

    #assert x.h() <= 2 * log2(x.nodes + 1)

    x._print()
    #print(x.bh())

    assert x.is_rbt()

    #x.rotate_left()
    #x.rotate_right()

if __name__ == '__main__':
    TESTS = 100

    test()
    print("All tests passed")
