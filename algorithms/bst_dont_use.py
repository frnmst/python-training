#!/usr/bin/env python3

#
# bst_dont_use.py
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

class BstNode:
    def __init__(self,key,right=None,left=None,parent=None):
        self.key = key
        self.right = right
        self.left = left
        self.parent = parent

    def _print(self):
        print("Node data")
        print("=========")
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

# As suggested by
# https://stackoverflow.com/questions/5555449/using-self-xxxx-as-default-parameter-python
Null = object()

class Bst:
    # Start with an empty BST:
    #   push in a node with a specified key as root
    def __init__(self,key):
        self.root = BstNode(key)

    def delete():
        pass

    def insert(self,key):
        z = BstNode(key)
        y = None
        x = self.root
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

    def search(self,key,root=Null):
        if root is Null:
            root = self.root
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(key,root.left)
        else:
            return self.search(key,root.right)


    def min(self,root=Null):
        if root is Null:
            root = self.root
        if root.left is not None:
            return self.min(root.left)
        else:
            return root

    def max(self,root=Null):
        if root is Null:
            root = self.root
        if root.right is not None:
            return self.max(root.right)
        else:
            return root


    def successor(self,root=self.root):
        if root is Null:
            root = self.root
        if root.right is not None:
            return self.max(root)

    def predecessor(self,root=Null):
        pass

    # Natively working but less elegant interface
    #def inorder(self,root=self.root):
    #    if root is not None:
    #        self.inorder(root.left)
    #        root._print()
    #        self.inorder(root.right)

    def inorder(self,root=Null):
        if root is Null:
            root = self.root
        if root is not None:
            self.inorder(root.left)
            root._print()
            self.inorder(root.right)

    def preorder(self,root=Null):
        if root is Null:
            root = self.root
        if root is not None:
            root._print()
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root=Null):
        if root is Null:
            root = self.root
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            root._print()

def test():
    t = Bst(1)
    #t.root._print()
    t.insert(2)
    t.insert(0)
    #t.root.right._print()
    #t.root._print()
    '''
    # t.inorder(t.root)
    print("inorder")
    t.inorder()
    print("preorder")
    t.preorder()
    print("postorder")
    t.postorder()

    t.search(2)._print()
    '''
    t.min()._print()
    t.max()._print()

if __name__ == '__main__':
    test()
