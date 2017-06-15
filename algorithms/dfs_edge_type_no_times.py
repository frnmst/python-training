#!/usr/bin/env python3

#
# dfs_edge_type.py
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

from dfs_edge_type import DfsEdgeTypeGraph

white = "white"
gray = "gray"
black = "black"

# An alternative way of getting the edge types without using the discovery and 
# finishing times.
class DfsEdgeTypeGraphNoTimes(DfsEdgeTypeGraph):

    # Is x an ancestor of y ?
    def is_ancestor(G,x,y):
        # Climb up the tree.
        while x is not None:
            if x is y:
                return True
            x = x.parent

        return False

    def is_forward_edge(G,u,v):
        return G.is_ancestor(v,u)

    def is_back_edge(G,u,v):
        # Loop edge is a back edge, according to the definition.
        if u is v:
            return True
        else:
            return G.is_ancestor(u,v)

    def is_cross_edge(G,u,v):
        # Check if cross edge is between different trees or not.
        x = u
        y = v
        while x.parent is not None:
            x = x.parent

        while y.parent is not None:
            y = y.parent

        # If all three are false then it's true that it's a cross tree
        is_cross = not (G.is_tree_edge(u,v) or G.is_forward_edge(u,v) \
            or G.is_back_edge(u,v))

        if is_cross:
            if x is y:
                print ("\tBelongs to same BFS tree:")
            else:
                print ("\tDoes NOT belong to same BFS tree:")

        return is_cross

def test():
    G = DfsEdgeTypeGraphNoTimes(['s','t','u','v','w','x','y','z'])
    assert G.add_edge('s','w')
    assert G.add_edge('s','z')
    assert G.add_edge('t','u')
    assert G.add_edge('t','v')
    assert G.add_edge('u','t')
    assert G.add_edge('u','v')
    assert G.add_edge('v','s')
    assert G.add_edge('v','w')
    assert G.add_edge('w','x')
    assert G.add_edge('x','z')
    assert G.add_edge('y','x')
    assert G.add_edge('z','w')
    assert G.add_edge('z','y')


    G.dfs()

    for v in G.V:
        assert v.color is black

    G._print_vertices()

    G.classify_edges()

if __name__ == '__main__':
    test()
    print("All tests passed")
