#!/usr/bin/env python3

#
# dfs.py
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

from graph import Vertex,Graph

white = "white"
gray = "gray"
black = "black"

# Use key attribute as unique id to speed things up.
#
# We also use keys directly instead of the Vertex objects directly since the 
# user will interact with keys rather than
#
# Indirected graphs are a subclass of directed graphs.
class DfsVertex(Vertex):
    def __init__(V,key):
        super().__init__(key)
        V.color = black
        V.parent = None
        V.discover = 0
        V.finish = 0

    def _print(V):
        super()._print()
        print("Color = " + str(V.color))
        print("Parent = " + str(V.parent))
        if V.parent is not None:
            print("Parent key = " + str(V.parent.key))
        print("Discover = " + str(V.discover))
        print("Finish = " + str(V.finish))
        print()

class DfsGraph(Graph):
    def __init__(G,list_of_vertices_keys):
        G.Adj = dict()
        for i in range(0,len(list_of_vertices_keys)):
            G.Adj[list_of_vertices_keys[i]] = list()

        G.number_of_vertices = len(list_of_vertices_keys)

        G.V = list()
        for i in range(0,len(list_of_vertices_keys)):
            G.V.append(DfsVertex(list_of_vertices_keys[i]))

        G.id = G

    # Global class variable.
    time = 0
    def dfs(G):
        for u in G.V:
            u.color = white
            u.parent = None
        G.time = 0
        # T(n) = O(V + E)
        #
        # O(V) for this loop.
        for u in G.V:
            # Each iteration here builds a tree
            # Visit each vertex only once.
            if u.color is white:
                G.dfs_visit(u)

    def dfs_visit(G,u):
        G.time += 1
        u.discover = G.time
        u.color = gray
        # Look all Adj lists once.
        # This means that it will be O(E).
        for v in G.get_vertex_id_list_from_key_list(G.Adj[u.key]):
            if v.color is white:
                v.parent = u
                G.dfs_visit(v)
        u.color = black
        G.time += 1
        u.finish = G.time


def test():
    # Define vertices at instantiation.
    G = DfsGraph(['Ferrara','Bologna','Ravenna','Rovigo','Venexia'])
    assert G.add_edge('Ferrara','Bologna')
    assert G.add_edge('Bologna','Ravenna')
    assert G.add_edge('Ferrara','Rovigo')

    assert not G.add_edge('Ferrara','Bologna')

    assert G.edge_exists('Ferrara','Bologna')
    assert G.edge_exists('Bologna','Ravenna')
    assert G.edge_exists('Ferrara','Rovigo')

    G.dfs()

    for v in G.V:
        assert v.color is black

    # Since it seems that the keys is the dictionary are scanned
    # in order of input, we can assert certain facts like the v.d
    # and v.f times, which have been computed on paper.
    assert G.get_vertex_id_from_key('Ferrara').discover == 1
    assert G.get_vertex_id_from_key('Ferrara').finish == 8

    assert G.get_vertex_id_from_key('Bologna').discover == 2
    assert G.get_vertex_id_from_key('Bologna').finish == 5

    assert G.get_vertex_id_from_key('Ravenna').discover == 3
    assert G.get_vertex_id_from_key('Ravenna').finish == 4

    assert G.get_vertex_id_from_key('Rovigo').discover == 6
    assert G.get_vertex_id_from_key('Rovigo').finish == 7

    assert G.get_vertex_id_from_key('Venexia').discover == 9
    assert G.get_vertex_id_from_key('Venexia').finish == 10

    G._print_vertices()

if __name__ == '__main__':
    test()
    print("All tests passed")
