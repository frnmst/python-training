#!/usr/bin/env python3

#
# graph.py
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

# Use key attribute as unique id to speed things up.
#
# We also use keys directly instead of the Vertex objects directly since the 
# user will interact with keys rather than
#
# Undirected graphs are a subclass of directed graphs.
class Vertex:
    def __init__(V,key):
        V.key = key
        V.id = V

    def _print(V):
        print("Vertex data")
        print("=========")
        print("ID = " + str(V.id))
        print("Key = " + str(V.key))
        print()

class Graph:
    def __init__(G,list_of_vertices_keys):
        # List of keys.
        G.Adj = dict()
        for i in range(0,len(list_of_vertices_keys)):
            G.Adj[list_of_vertices_keys[i]] = list()

        G.number_of_vertices = len(list_of_vertices_keys)

        # List of vertices.
        G.V = list()
        for i in range(0,len(list_of_vertices_keys)):
            G.V.append(Vertex(list_of_vertices_keys[i]))

        G.id = G

    def _print(G):
        print("Graph data")
        print("=========")
        print("ID = " + str(G.id))
        print("Adjacency list= ")
        for u in G.Adj:
            G._print_vertex_list(u)
        print("Number of vertices = " + str(G.number_of_vertices))
        print("Vertices list= " + str(G.V))
        print()

    def _print_vertices(G):
        for v in G.V:
            v._print()

    def _print_vertex_list(G,key):
        assert key in G.Adj

        print("Adjacency list for " + str(key))
        print("===================" + ("=" * len(key)))

        for k in G.Adj[key]:
            print (str(k) + " , ", end="")
        print("\n<<< end")
        print()

    def get_vertex_id_from_key(G,key):
        #assert key in G.Adj

        for v in G.V:
            #print(v.key)
            if key == v.key:
                return v

        return None

    def get_vertex_id_list_from_key_list(G,key):
        vertex_list = list()

        for u in G.V:
            for k in key:
                if k == u.key:
                    vertex_list.append(u)

        return vertex_list

    # Define this method as private so that the add_edge
    # and remove_edge methods of this class are not in conflict
    # if called by a subclass.
    def __edge_exists(G,key_from,key_to):
        assert key_from in G.Adj
        assert key_to in G.Adj

        for k in G.Adj[key_from]:
            if k == key_to:
                return True

        return False

    def edge_exists(G,key_from,key_to):
        return G._Graph__edge_exists(key_from,key_to)

    def add_edge(G,key_from,key_to):
        if not G._Graph__edge_exists(key_from,key_to):
            G.Adj[key_from].append(key_to)
            return True
        else:
            return False

    def remove_edge(G,key_from,key_to):
        if G._Graph__edge_exists(key_from,key_to):
            for k in G.Adj[key_from]:
                if k == key_to:
                    G.Adj[key_from].remove(k)
                    return True
            return False
        else:
            return False

def test():
    # Define vertices at instantiation.
    G = Graph(['Ferrara','Bologna','Ravenna','Rovigo'])
    assert G.add_edge('Ferrara','Bologna')
    assert G.add_edge('Bologna','Ravenna')
    assert G.add_edge('Ferrara','Rovigo')

    assert not G.add_edge('Ferrara','Bologna')

    assert G.edge_exists('Ferrara','Bologna')
    assert G.edge_exists('Bologna','Ravenna')
    assert G.edge_exists('Ferrara','Rovigo')

    assert G.remove_edge('Ferrara','Bologna')

    G._print()

if __name__ == '__main__':
    test()
    print("All tests passed")
