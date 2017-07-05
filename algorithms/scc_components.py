#!/usr/bin/env python3

#
# scc_components.py
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

import string

from copy import deepcopy
from scc import SccGraph

class SccComponentsGraph(SccGraph):

    # For each list in the sccs dictionary,
    # merge it into a sigle string.
    def get_scc_vertices(G,sccs):
        vertices = []

        for component in sccs:
            vertices.append(''.join(sccs[component]))

        return vertices

    # Given a vertex v of G, return the vertex component of Gscc.
    def get_scc_from_vertex(Gscc,v):
        for component in Gscc.V:
            if v.key in component.key:
                return component

    # The vertices of this grap are the SCCs.
    # Go through every SCC to find edges going from the current SCC to 
    # another scc.
    def assemble(Gscc,G):
        for component in Gscc.V:
            for ukey in component.key:
                for v in G.get_vertex_id_list_from_key_list(G.Adj[ukey]):
                    if v.key not in component.key:
                        Gscc.add_edge(component.key,Gscc.get_scc_from_vertex(v).key)

    def scc(G):
        G.dfs()

        # We won't need G transposed afterwards.
        Gt = deepcopy(G)

        Gt.transpose()
        Gt.dfs_transposed(Gt.sort_vertex_list_by_dsc_finishing_times())
        return Gt.get_components()

def test():
    list_of_vertices = []
    end_vertex = 'h'
    for l in string.ascii_lowercase:
        if ord(l) <= ord(end_vertex):
            list_of_vertices.append(l)

    G = SccComponentsGraph(list_of_vertices)
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

    # Get the SCCs
    Gscc = SccComponentsGraph(G.get_scc_vertices(G.scc()))
    Gscc.assemble(G)
    Gscc._print()

if __name__ == '__main__':
    test()
    print("All tests passed")
