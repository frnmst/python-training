#!/usr/bin/env python3

#
# scc.py
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

from dfs import DfsGraph

white = "white"
gray = "gray"
black = "black"

class SccGraph(DfsGraph):
    def transpose(G):
        # We need an intermediate structure otherwise we would not obtain
        # the transposed graph if done directly. Note that this alters the
        # edge set of the input graph, it doesn't create a new set.
        edge_list = []
        for u in G.V:
            for v in G.get_vertex_id_list_from_key_list(G.Adj[u.key]):
                assert G.remove_edge(u.key,v.key)
                edge_list.append(v)
                edge_list.append(u)

        # Iterator, courtesy of StackOverflow.
        # https://stackoverflow.com/a/21752713
        for u,v in zip(edge_list[::2],edge_list[1::2]):
            assert G.add_edge(u.key,v.key)

    # Return a list of keys corresponding to the vertices.
    def sort_vertex_list_by_dsc_finishing_times(G):
        return sorted(G.V, key=lambda v: v.finish, reverse=True)

    # Run DFS by iterating on the vertices in the specified order.
    def dfs_transposed(G,sorted_vertex_list):
        G.prepare()
        for u in sorted_vertex_list:
            if u.color is white:
                G.dfs_visit(u)

    def prepare_components_list(G):
        components = dict()
        for v in G.V:
            components[v.key] = list()

        return components

    # Remove empty sets.
    def purge_components_list(G,components):
        # Make a backup to avoid an iteration problem
        backup = dict(components)
        for v in backup:
            if backup[v] == []:
                del components[v]

        return components

    def get_components(G):
        components = G.prepare_components_list()
        for v in G.V:
            start = v
            w = v
            while w is not None:
                    # This is never None and always points to start's main
                    # parent or itself.
                    prev = w
                    w = w.parent
            # Put the current vertex in the parent set.
            components[prev.key].append(start.key)

        return G.purge_components_list(components)

    def _print_scc(G,sccs):
        print("Number of SCC = " + str(len(sccs)))
        for component in sccs:
            print (sccs[component])

    def scc(G):
        G.dfs()
        G.transpose()
        G._print_vertices()
        G.dfs_transposed(G.sort_vertex_list_by_dsc_finishing_times())
        return G.get_components()

def test():
    list_of_vertices = []
    end_vertex = 'h'
    for l in string.ascii_lowercase:
        if ord(l) <= ord(end_vertex):
            list_of_vertices.append(l)

    G = SccGraph(list_of_vertices)
    assert G.add_edge('a','b')
    assert G.add_edge('b','c')
    assert G.add_edge('b','e')
    assert G.add_edge('b','f')
    assert G.add_edge('c','d')
    assert G.add_edge('c','g')
    assert G.add_edge('d','c')
    assert G.add_edge('d','h')
    assert G.add_edge('e','a')
    assert G.add_edge('e','f')
    assert G.add_edge('f','g')
    assert G.add_edge('g','f')
    assert G.add_edge('g','h')
    assert G.add_edge('h','h')

    G._print_scc(G.scc())

if __name__ == '__main__':
    test()
    print("All tests passed")
