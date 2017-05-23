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
        T.sentinel = NilNode()
        T.root = T.sentinel
        T.root.parent = T.root.left = T.root.right = T.sentinel
        # T.sentinel.left = T.sentinel.right = T.sentinel.parent = None
        T.nodes = 0
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
        # Put beta in the correct place.
        x.right = y.left

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
        y.left = x.right

        if x.right is not T.sentinel:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is T.sentinel:
            T.root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def insert(T,key,root=None):
        y = T.sentinel
        x = super()._set_root(root)
        z = RbtNode(key=key,color=black)

        T.nodes += 1

        # Find the correct position for z, just like in the BST insert method.
        while x is not T.sentinel:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
            # assert y is x.parent

        z.parent = y

        if y is T.sentinel:
            T.root = z
        # Fixup z position in relation to its parent y which means connect the
        # parent to the new node appropriately.
        elif z.key < y.key:
            y.left = z
        else:
            assert z.key >= y.key
            y.right = z

        z.left = T.sentinel
        z.right = T.sentinel
        # At this point z's children are "dangling"
        z.color = red

        assert T.properties(1,T.root) and T.properties(3,T.root) \
            and T.properties(5,T.root)

        T.insert_fixup(z)

    def insert_fixup(T,z):
        while z.parent.color is red:

            assert z.color is red
            if z.parent is T.root:
                assert z.parent.color is black
            elif z is T.root:
                assert z.parent is T.sentinel

            if z.parent is z.parent.parent.left:
                # y is always z's uncle.
                y = z.parent.parent.right
                if y.color is red:
                    z.parent.color = black
                    y.color = black
                    z.parent.parent.color = red
                    z = z.parent.parent
                # Book notation is messy. It seems an elif: while in reality
                # is an else: if:
                else:
                    if z is z.parent.right:
                        z = z.parent
                        T.rotate_left(z)
                    z.parent.color = black
                    z.parent.parent.color = red
                    T.rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color is red:
                    z.parent.color = black
                    y.color = black
                    z.parent.parent.color = red
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        T.rotate_right(z)
                    z.parent.color = black
                    z.parent.parent.color = red
                    T.rotate_left(z.parent.parent)
        T.root.color = black

    def search(T,key,root=None):
        x = T._set_root(root)
        found = False
        while not found and x is not T.sentinel:
            if key == x.key:
                found = True
            elif key < x.key:
                x = x.left
            else:
                x = x.right

        return x

    # Return height (ie. the height corresponding to the longest path from the
    # root to (is most distant leaf).
    def h(T,root=Null):
        root = T._set_root_null(root)
        v = 0

        if root is T.sentinel:
                return 0
        else:
            return 1 + max(T.h(root.left),T.h(root.right))

    # Black height of Rbt is black height of root node
    # Leaf nodes have black height 0.
    # The recursive way seems much simpler here.
    # This function also checks if the bh propriety is valid for the input tree 
    # by returning a boolean
    def bh(T,root=Null,compare=False):
        root = T._set_root_null(root)
        v = 0

        # No root: black height is 0 (base case)
        #if root is None or root is T.sentinel:
        if root is T.sentinel:
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

    # RBT property checker.
    def properties(T,id,root):
        # Safety first
        # An empty RBT is a valid RBT.
        # I made up this propriety.
        # Property 6
        #
        # If it's an empty RBT, it's a valid RBT.
        if id == 6:
            if root is None:
                return True

        # No need to check for property 1 (each noide is either red or 
        # black) and property 3 (each leaf is black (it must be a NilNode)).
        elif id == 1 or id == 3:
            return True

        # Property 2
        # Root must be black
        elif id == 2:
            if root.color is not black:
                return False

        # Property 5
        # For each node y, bh(y) must be the same for every simple path from y 
        # to the leaves.
        #
        # Hack: since the root is connected to all the other nodes of the tree,
        # this propriety can be checked for the root only. We also know that 
        # the black height of the root is the same for every path.
        #
        # Propriety 4
        #
        # For each red node z, z.left and z.right must be black nodes.
        elif id == 4 or id == 5:
            if not T.bh(compare=True):
                return False

        return True

    # Add each boolean result to know if all the properties are true
    def is_rbt(T,root=None):
        total_properties = 6
        x = super()._set_root(root)
        properties = range(1,total_properties + 1)
        s = 0
        for p in properties:
            s += T.properties(p,x)

        if s == total_properties:
            return True
        else:
            return False

def test(verbose=False):
    x = Rbt()

    #assert x.h() <= 2 * log2(x.nodes + 1)

    for k in range(MIN, MAX + 1):
        x.insert(k)
        #print(k)

    assert x.is_rbt()

    x._print()

    assert x.h() >= x.bh()

    if x.nodes > 1:
        assert 2*(math.log2(x.nodes+1)) >= x.h() \
            and math.log2(x.nodes + 1) >= x.h() / 2 \
            and x.nodes >= 2 ** (x.h() / 2)

    assert x.search(MIN).key == MIN
    assert x.search(MAX).key == MAX

    # assert x.h() <= MAX - MIN + 1

# Key range.
MIN = 1
MAX = 5000

if __name__ == '__main__':
    TESTS = 100

    test()
    print("All tests passed")
