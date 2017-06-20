#!/usr/bin/env python3

#
# undirected_graph.py
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

from graph import Graph

class UndirectedGraph(Graph):
    def edge_exists(G,key_from,key_to):
        return super().edge_exists(key_from,key_to) and super().edge_exists(key_to,key_from)

    def add_edge(G,key_from,key_to):
        # Self loops are not allowed in an undirected graph.
        if key_from == key_to:
            return False
        else:
            return super().add_edge(key_from,key_to) and super().add_edge(key_to,key_from)

    def remove_edge(G,key_from,key_to):
        return super().remove_edge(key_from,key_to) and super().remove_edge(key_to,key_from)

def test():
    G = UndirectedGraph(['Ferrara','Bologna','Ravenna','Rovigo'])
    assert G.add_edge('Ferrara','Bologna')
    assert G.add_edge('Bologna','Ravenna')
    assert G.add_edge('Ferrara','Rovigo')

    assert not G.add_edge('Ferrara','Bologna')

    assert G.edge_exists('Ferrara','Bologna')
    assert G.edge_exists('Bologna','Ravenna')
    assert G.edge_exists('Ferrara','Rovigo')

    assert G.edge_exists('Bologna','Ferrara')
    assert G.edge_exists('Ravenna','Bologna')
    assert G.edge_exists('Rovigo','Ferrara')

    assert G.remove_edge('Ferrara','Rovigo')

    G._print()

    assert not G.edge_exists('Ferrara','Rovigo')
    assert not G.edge_exists('Rovigo','Ferrara')

if __name__ == '__main__':
    test()
    print("All tests passed")
