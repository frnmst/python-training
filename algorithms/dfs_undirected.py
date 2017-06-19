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

from undirected_graph import UndirectedGraph
from dfs import DfsGraph

white = "white"
gray = "gray"
black = "black"

class DfsUndirectedGraph(UndirectedGraph,DfsGraph):
    def dfs_visit(G,u):
        found = False
        G.time += 1
        u.discover = G.time
        u.color = gray
        for v in G.get_vertex_id_list_from_key_list(G.Adj[u.key]):
            if v.color is white:
                v.parent = u
                G.dfs_visit(v)
            else:
                # If it's not the undirected back edge (part of the tree)
                if u.parent is not v:
                    # If it's the quivalent of a back edge.
                    if v.discover < u.discover:
                        # Cycle found
                        print("Cycle found on edge ",end="")
                        print (u.key + " - " + v.key)
                        return
        u.color = black
        G.time += 1
        u.finish = G.time


def test():
    # Define vertices at instantiation.
    G = DfsUndirectedGraph(['Milano','Torino','Venexia','Mantova','Ferrara','Bologna','Ravenna','Rovigo'])
    assert G.add_edge('Milano','Venexia')
    assert G.add_edge('Torino','Venexia')
    assert G.add_edge('Venexia','Mantova')
    assert G.add_edge('Mantova','Ferrara')
    assert G.add_edge('Ferrara','Bologna')
    assert G.add_edge('Bologna','Ravenna')
    assert G.add_edge('Ravenna','Rovigo')
    assert G.add_edge('Rovigo','Ferrara')

    G.dfs()

    # print()
    # print()
    #G._print_vertices()

def test_two():
    G = DfsUndirectedGraph(['Milano','Torino','Venexia','Mantova'])
    assert G.add_edge('Milano','Venexia')
    assert G.add_edge('Torino','Venexia')
    assert G.add_edge('Venexia','Mantova')

    G.dfs()

    G._print_vertices()

if __name__ == '__main__':
    test()
    #test_two()
    print("All tests passed")
