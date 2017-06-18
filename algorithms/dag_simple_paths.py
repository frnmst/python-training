#!/usr/bin/env python3

#
# dag_simple_paths.py
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

from dfs import DfsGraph,DfsVertex

white = "white"
gray = "gray"
black = "black"

# See http://courses.cs.tamu.edu/jarvi/2004/f689/assignment3.pdf for the
# complete explanation
class DagSimplePathsVertex(DfsVertex):
    def __init__(V,key):
        super().__init__(key)
        V.path_count = 0

    def _print(V):
        super()._print()
        print("Path count = " + str(V.path_count))
        print()

class DagSimplePathsGraph(DfsGraph):

    def __init__(G,list_of_vertices_keys):
        G.Adj = dict()
        for i in range(0,len(list_of_vertices_keys)):
            G.Adj[list_of_vertices_keys[i]] = list()

        G.number_of_vertices = len(list_of_vertices_keys)

        G.V = list()
        for i in range(0,len(list_of_vertices_keys)):
            G.V.append(DagSimplePathsVertex(list_of_vertices_keys[i]))

        G.id = G


    def dfs(G,s,t):
        G.prepare()
        G.dfs_visit(s,t)

    def dfs_visit(G,u,t):
        G.time += 1
        u.discover = G.time
        u.color = gray
        for v in G.get_vertex_id_list_from_key_list(G.Adj[u.key]):
            if v.color is white:
                # If there is a vertex (u,v) which is part of a path from s to
                # t, it means that the path from s to t exists.
                # No need to examine adjs because all path counts have already
                # been computed; infact this is the base case.
                if v is t:
                    # This case is only engaged once because of the color 
                    # check.
                    v.path_count += 1
                    v.color = black
                    G.time += 1
                    v.finish = G.time
                else:
                    v.path_count = 0
                    v.parent = u
                    G.dfs_visit(v,t)
            # Non-base case: add all adjacent path counts.
            u.path_count += v.path_count

        u.color = black
        G.time += 1
        u.finish = G.time


def test():
    list_of_vertices = []
    start_vertex = 'm'
    for l in string.ascii_lowercase:
        if ord(l) >= ord(start_vertex):
            list_of_vertices.append(l)

    # G must be a DAG in order for this to work.
    G = DagSimplePathsGraph(list_of_vertices)

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

    G.dfs(G.get_vertex_id_from_key('p'),G.get_vertex_id_from_key('v'))

    for v in G.V:
        print(v.path_count)

    print("Simple paths from p to v = ",end ="")
    for v in G.V:
        if v.key == 'p':
            print(v.path_count)

if __name__ == '__main__':
    test()
    print("All tests passed")
