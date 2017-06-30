#!/usr/bin/env python3

#
# topological_sort.py
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
import string

from stack import Stack
from dfs import DfsGraph

white = "white"
gray = "gray"
black = "black"

class TopologicalSortGraph(DfsGraph):
    def __init__(G,list_of_vertices_keys):
        super().__init__(list_of_vertices_keys)
        G.topological = Stack()

    def topological_sort(G):
        G.dfs()

    def dfs_visit(G,u):
        super().dfs_visit(u)
        G.topological.push(u)

    def _print_topological_list(G):
        while not G.topological.is_empty():
            print(str(G.topological.pop().key) + " -> ",end="")
        print("-|")


def test():
    # From exercise 22.4-1, Cormen et alia book.
    # Rsult confirmed by paper test.
    list_of_vertices = []
    start_vertex = 'm'
    for l in string.ascii_lowercase:
        if ord(l) >= ord(start_vertex):
            list_of_vertices.append(l)

    G = TopologicalSortGraph(list_of_vertices)

    assert G.add_edge('m','q')
    assert G.add_edge('m','r')
    assert G.add_edge('m','x')
    assert G.add_edge('n','o')
    assert G.add_edge('n','q')
    assert G.add_edge('n','u')
    assert G.add_edge('o','r')
    assert G.add_edge('o','s')
    assert G.add_edge('o','v')
    assert G.add_edge('p','o')
    assert G.add_edge('p','s')
    assert G.add_edge('p','z')
    assert G.add_edge('q','t')
    assert G.add_edge('r','u')
    assert G.add_edge('r','y')
    assert G.add_edge('s','r')
    assert G.add_edge('u','t')
    assert G.add_edge('v','w')
    assert G.add_edge('v','x')
    assert G.add_edge('w','z')
    assert G.add_edge('y','v')

    G.topological_sort()

    for v in G.V:
        assert v.color is black

    G._print_vertices()

    G._print_topological_list()

if __name__ == '__main__':
    test()
    print("All tests passed")
