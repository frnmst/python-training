#!/usr/bin/env python3

#
# bfs.py
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
from queue import Queue

Inf = math.inf
white = "white"
gray = "gray"
black = "black"

# Use key attribute as unique id to speed things up.
#
# We also use keys directly instead of the Vertex objects directly since the 
# user will interact with keys rather than
#
# Indirected graphs are a subclass of directed graphs.
class BfsVertex(Vertex):
    def __init__(V,key):
        super().__init__(key)
        V.color = black
        V.distance = Inf
        V.parent = None

    def _print(V):
        super()._print()
        print("Color = " + str(V.color))
        print("Distance = " + str(V.distance))
        print("Parent = " + str(V.parent))
        print()

class BfsGraph(Graph):
    def __init__(G,list_of_vertices_keys):
        G.Adj = dict()
        for i in range(0,len(list_of_vertices_keys)):
            G.Adj[list_of_vertices_keys[i]] = list()

        G.number_of_vertices = len(list_of_vertices_keys)

        G.V = list()
        for i in range(0,len(list_of_vertices_keys)):
            # Change Vertex to BfsVertex.
            G.V.append(BfsVertex(list_of_vertices_keys[i]))

        G.id = G

    def Bfs(G,s):
        for u in G.V:
            if u is not s:
                u.color = white
                u.distance = Inf
                u.parent = None
        s.color = gray
        s.distance = 0
        s.parent = None
        Q = Queue()
        Q.enqueue(s)
        while not Q.is_empty():
            u = Q.dequeue()
            for v in G.get_vertex_id_list_from_key_list(G.Adj[u.key]):
                if v.color is white:
                    v.color = gray
                    v.distance = u.distance + 1
                    v.parent = u
                    Q.enqueue(v)
            u.color = black

    # Print from s to v thatnks to recursion.
    def _print_path(G,s,v):
        if v is s:
            s._print()
        elif v.parent is None:
            print("No path from s to v")
        else:
            G._print_path(s,v.parent)
            v._print()

def test():
    # Define vertices at instantiation.
    G = BfsGraph(['Ferrara','Bologna','Ravenna','Rovigo','Venexia'])
    assert G.add_edge('Ferrara','Bologna')
    assert G.add_edge('Bologna','Ravenna')
    assert G.add_edge('Ferrara','Rovigo')

    assert not G.add_edge('Ferrara','Bologna')

    assert G.edge_exists('Ferrara','Bologna')
    assert G.edge_exists('Bologna','Ravenna')
    assert G.edge_exists('Ferrara','Rovigo')

    G.Bfs(G.get_vertex_id_from_key('Ferrara'))

    for v in G.V:
        if v is not G.get_vertex_id_from_key('Venexia'):
            assert v.color is black

    assert G.get_vertex_id_from_key('Venexia').distance is Inf

    assert G.get_vertex_id_from_key('Bologna').parent \
        is G.get_vertex_id_from_key('Ferrara')
    assert G.get_vertex_id_from_key('Ravenna').parent \
        is G.get_vertex_id_from_key('Bologna')
    assert G.get_vertex_id_from_key('Rovigo').parent \
        is G.get_vertex_id_from_key('Ferrara')

    G._print_vertices()
    print("--Path--")
    G._print_path(G.get_vertex_id_from_key('Ferrara'),G.get_vertex_id_from_key('Ravenna'))

if __name__ == '__main__':
    test()
    print("All tests passed")
