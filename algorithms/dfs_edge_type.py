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

from dfs import DfsGraph

white = "white"
gray = "gray"
black = "black"

class DfsEdgeTypeGraph(DfsGraph):

    def is_tree_edge(G,u,v):
        return v.parent is u

    # Using the difinitions:

    # u is a descendant of v
    def is_back_edge(G,u,v):
        return u.discover > v.discover and u.finish < v.finish

    # v is a descendant of u
    def is_forward_edge(G,u,v):
        return v.discover > u.discover and v.finish < u.finish

    # u times and v times unrelated
    # A cross edge connects different connected components
    def is_cross_edge(G,u,v):
        return u is v or (not G.is_forward_edge(u,v) and not G.is_back_edge(u,v))
        #return u.discover > v.discover

    def classify_edges(G):
        # What type of edge is (u,v)?
        for u in G.V:
            for v in G.get_vertex_id_list_from_key_list(G.Adj[u.key]):
                if G.is_tree_edge(u,v):
                    print ("Tree edge ",end="")
                elif G.is_back_edge(u,v):
                    print ("Back edge ",end="")
                elif G.is_forward_edge(u,v):
                    print ("Forward edge ",end="")
                elif G.is_cross_edge(u,v):
                    print ("Cross edge ",end="")

                print(str(u.key) + " -> " + str(v.key))

def test():
    G = DfsEdgeTypeGraph(['s','t','u','v','w','x','y','z'])
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
