#!/usr/bin/env python3

#
# recursive_class_method.py
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

class A:
    def __init__(self):
        self.s = 0

    def search(self,s=0):
        print(self.s)
        self.search(self.s + 1)
        # self.search(self.s + 1)

if __name__ == '__main__':
    a = A()
    a.search()
