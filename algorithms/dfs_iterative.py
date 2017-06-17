#!/usr/bin/env python3

#
# dfs_iterative.py
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

from stack import Stack
from dfs import DfsGraph,DfsVertex

white = "white"
gray = "gray"
black = "black"

class DfsIterativeGraph(DfsGraph):

    def all_explored(G,u):
        for v in G.get_vertex_id_list_from_key_list(G.Adj[u.key]):
            if v.color is not black:
                return False
        return True

    def dfs(G):
        G.prepare()
        s = Stack()

        # Reach all vertices including isolated ones.
        # We can easily compute all attributes of a vertex except the finishing 
        # time.
        for u in G.V:
            # Pass through new verteices only once
            if u.color is white:
                s.push(u)
                while not s.is_empty():
                    w = s.pop()
                    adjs_to_visit = True
                    if w.color is white:
                        G.time += 1
                        w.discover = G.time
                        w.color = gray
                        for v in G.get_vertex_id_list_from_key_list(G.Adj[w.key]):
                            v.parent = w
                            s.push(v)

                    # ====================================
                    # The purely conjectural part follows.
                    #=====================================

                    # If the vertex has been examined and if it's a "leaf"
                    # (no adjacent vertices) then set it to be black and
                    # we record the finishing time.
                    # This is the base case.
                    if w.color is gray:
                        if len(G.get_vertex_id_list_from_key_list(G.Adj[w.key])) == 0:
                            G.time += 1
                            w.finish = G.time
                            w.color = black
                            # To apply the base case to the non-leaf vertices
                            # we need to be sure that all the adjacent vertices 
                            # of the non-leaf node have been fully discovered.
                            # Since we don't have a method to trace back the
                            # calls we will use the parent attribute of the
                            # leaf vertex.
                            #
                            # Do all this by climing up the graph.
                            while w.parent is not None:
                                # if w is last examined, which is translated as:
                                # if w.parent.Adjs are all black
                                if G.all_explored(w.parent):
                                    w.parent.color = black
                                    G.time += 1
                                    w.parent.finish = G.time
                                # Climb up the tree.
                                w = w.parent

def test():
    # Define vertices at instantiation.
    G = DfsIterativeGraph(['Ferrara','Bologna','Cona','Ravenna','Rovigo','Piacenza','Venexia'])
    #assert G.add_edge('Ferrara','Bologna')
    assert G.add_edge('Bologna','Ravenna')
    assert G.add_edge('Ferrara','Rovigo')
    assert G.add_edge('Piacenza','Venexia')
    assert G.add_edge('Ferrara','Piacenza')
    assert G.add_edge('Rovigo','Bologna')
    assert G.add_edge('Venexia','Cona')
    assert G.add_edge('Venexia','Rovigo')

    #assert not G.add_edge('Ferrara','Bologna')

    #assert G.edge_exists('Ferrara','Bologna')
    assert G.edge_exists('Bologna','Ravenna')
    assert G.edge_exists('Ferrara','Rovigo')

    G.dfs()

    for v in G.V:
        assert v.color is black

    G._print_vertices()

if __name__ == '__main__':
    test()
    print("All tests passed")
