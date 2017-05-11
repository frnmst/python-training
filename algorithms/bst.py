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

from stack import Stack

class BstNode:
    def __init__(self,key,right=None,left=None,parent=None):
        self.key = key
        self.right = right
        self.left = left
        self.parent = parent
        self.id = self

    def _print(self):
        print("Node data")
        print("=========")
        print("ID = " + str(self.id))
        print("Key = " + str(self.key))
        print("Right = " + str(self.right))
        print("Left = " + str(self.left))
        print("Parent = " + str(self.parent))
        print()

    def edit(self,key,right=None,left=None,parent=None):
        self.key = key
        self.right = right
        self.left = left
        self.parent = parent

# Using iterative functions we avoid the mess.

# insert, search, min, max, successor, predecessor can be used with subtrees. 
# That's why they are supplied with an extra root argument.

# min, max, successor, predecessor are defined on nodes, not keys.
class Bst:
    # Start with an empty BST:
    #   push in a node with a specified key as root
    def __init__(self,key):
        self.root = BstNode(key)

    def __set_root(self,root):
        if root is None:
            return self.root
        else:
            return root

    def delete():
        pass

    def insert(self,key,root=None):
        x = self.__set_root(root)
        y = None
        z = BstNode(key)
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self,key,root=None):
        x = self.__set_root(root)
        found = False
        while not found and x is not None:
            if key == x.key:
                found = True
            elif key < x.key:
                x = x.left
            else:
                x = x.right

        return x

    def min(self,root=None):
        x = self.__set_root(root)
        while x.left is not None:
            x = x.left

        return x

    def max(self,root=None):
        x = self.__set_root(root)
        while x.right is not None:
            x = x.right

        return x

    def successor(self,root=None):
        x = self.__set_root(root)
        if x.right is not None:
            return self.min(x.right)
        y = x.parent
        while y is not None and x is y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self,root=None):
        x = self.__set_root(root)
        if x.left is not None:
            return self.max(x.left)
        y = x.parent
        while y is not None and x is y.left:
            x = y
            y = y.parent
        return y

    def preorder(self,root=None):
        x = self.__set_root(root)
        s = Stack()
        s.push(x)
        while s:
            x = s.pop()
            x._print()
            if x.right is not None:
                s.push(x.right)
            if x.left is not None:
                s.push(x.left)

def test():
    MIN = 2
    MAX = 5

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

    t.preorder()
    t.inorder()

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

if __name__ == '__main__':
    TESTS = 1
    for t in range(0,TESTS):
        test_static()
        #test()
    print ("All tests passed")
