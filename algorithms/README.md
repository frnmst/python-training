## Source

From the CLRS book

## Class diagrams

- Lables represents classes
- The `^` symbol means that the pointing class inherits from the
  pointed class.
- Incidental edges means that two or more classes inherit from the
  same class.
- Spaces between incidental edges means that is just a crossing
  for space reasons: the classes involved do not inherit from the same 
  superclass.

```

           +------+
           | list |                           +-------+
           +------+                           | Graph |
              ^                               +-------+
              |                                   ^     \
     _________|_________                          |     ^
    |                   |                         |     |    
    |                   |                         |     |
+-------+           +-------+               +----------+| \
| Stack |           | Queue |<------------- | BfsGraph ||  \
+-------+           +-------+               +----------+|   \
    ^                   ^                               |    \
    |_____________<___  |  ___<___________              |     |                           
    |                   |                 |   +----------+ +-----------------+
    |___________________|             ____|___| DfsGraph | | UndirectedGraph |________
               ^                     |    |   +----------+ +-----------------+        |
               |                     ^    ^         ^                                 ^
               |                     |    |         |_____________________            |
             +-----+                 |    |         |                     |           |
             | Bst |                 |  +-------------------+ +------------------+    |
             +-----+                 |  | DfsIterativeGraph | | DfsEdgeTypeGraph |    |
                ^                    |  +-------------------+ +------------------+    |
                |                    |\                                  ^            |
    ____________|________________    | \                                 |            |
   |                  |          |   |  \              +-------------------------+    |
   |                  |          |   |   \             | DfsEdgeTypeGraphNoTimes |    |
   |                  |          |   |    \            +-------------------------+    |
+-------------+  +---------+  +-----+|   +----------------------+                    /
| BstSameKeys |  | BstSort |  | Rbt ||   | TopologicalSortGraph |                   /
+-------------+  +---------+  +-----+|   +----------------------+                  /
                         ____________|____________________________                /
                        |            |                            |              /
                   +----------+      +---------------------+ +--------------------+
                   | SccGraph |      | DagSimplePathsGraph | | DfsUndirectedGraph |
                   +----------+      +---------------------+ +--------------------+
                        |
                        |
                        |
              +--------------------+
              | SccComponentsGraph |
              +--------------------+

~°~°~°~°


  +----------+
  | HeapSort |
  +----------+


~°~°~°~°


   +-----------------+
   | DisjointSetList |
   +-----------------+
            ^
            |
            |
+-------------------------+
| DisjointSetListWeighted |
+-------------------------+


~°~°~°~°


+-----------------+
| DisjointSetTree |
+-----------------+


```

## Class descriptions and problems.

- `Stack` and `Queue` classes are very basic as they use python's `list` class
   with very few modifications.

- To avoid recursion in some methods, the `Bst` class imports the previous 
  classes. Since the `Rbt` class is a subclass of `Bst`. We need to apply the 
  DRY (Don't repeat yourself) criteria: in the Bst constructor I added
  the `sentinel` attribute which is always set to `None`. Then, in some 
  methods, I changed the value of the terminating condition from `None` to 
  `T.sentinel`. This enables us to import the code directly and to use it as 
  part of the `Rbt` class methods.

- The `TestTree` class compares the BST and RBT implementations under 
  two different conditions.

- The `HeapSort` class is a very simple implementation of both min and max 
  heaps with the sorting algorithm. The underlying data structure 
  corresponding to the array is the Python `list` class.

- The `DisjointSetList` is the most basic and worst performing
  implementation of disjoint sets. The `DisjointSetListWeighted` adds 
  the `len` attribute to the set. The set with the smallest length 
  gets appended to the largest one. This saves us a lot of iterations
  through the list thus enables to have a more efficient implementation. 
  *Sidenote:
  both these implementations have a huge problem which has been solved by 
  returning the sets: In the `DisjointSetListWeighted` we need
  to return the largest set, because it wouldn't work by just reassigning the 
  pointer of the smallest set to the pointer of the bigger one. This is caused 
  by the fact that the scope is local.*

```python
'''
The text of this exercise was adapted from: "Introduction to algorithms, Third 
edition", 21.2-5

"Is it possible to modify the DisjointSetListWeighted class in order to
have only the len and tail attributes in the set object and having the same 
number of attributes for the list object?"

Set attributes:
    tail        # pointer to the representative list object

List attributes:
    prev        # pointer to previous element
    set         # pointer to the set object
'''

def FindSet(S):
    return S.tail

def Union(S1,S2):
    if S2.len < S1.len:
        tail = S2.tail
        head = S2.tail
        while head.prev is not S2:
            head.set = S1
            head = head.prev

        # Assert head is the first element of S2
        head.prev = S1.tail

        S1.tail = tail

    else:
        assert S2.len >= S1.len
        <same as then but change S1 to S2 and vice-versa>
        
```

- If you run the `DisjointSetsTest` benchmark class you will be reported of the 
  running time of the three implementations. There is a HUGE improvement by 
  appending the shorter list to the longer list, while a smaller improvement in 
  using the tree implementation with the two heuristics. All the tests have 
  been done under the same conditions (progressive union operation).

- The `Graph` class implements a very basic graph structure. Applications are 
  available in the `BfsGraph` and `DfsGraph` classes.

- The `BfsGraph` class implements the breadth first class algorithm.

- The `DfsGraph` class implements the depth first class algorithm. Each 
  iteration in the `for` loop of the `dfs` method corresponds to building a DFS 
  tree. At the end the DFS forest is built. This means that if a Graph G has n 
  *isolated* vertices, n trees will be discovered.

- The `DfsIterativeGraph` implements the DFS algorithm using a stack insteead 
  of the recursion. The main outer loop enables the algorithm to reach all 
  vertices, including the isolated ones. The discovery time is registered
  when a vertex is popped out of the stack, while the parent attribute is 
  recorded while scanning the adjacency list of the current vertex. The most 
  complicated part is the correct recording of the finishing times. We have 
  infact two cases, *based on speculation because they have not been proven*:
  - Base case: a vertex has been examined (color is gray) and has no adjacent 
    vertices. In this case we record the finishing time and we set its color to 
    black. We will call this kind of vertex a "leaf" vertex.
  - If a vertex has adjacent vertices, we have to wait that all these other 
    vertices reach the base case. To do this, when a leaf vertex is fully 
    discovered (color black) we also check that its parent has all adjacent 
    vertices fully discovered. If that is the case we record the finishing time 
    of the parent. All this is done recursively by climbing up the DFS tree, 
    thanks to the parent attribute. This is an alterative way to trace back the
    discovery if the graph.
  The first case is achieved by examining the length of the adjacency list of 
  the vertex. If it's zero we know that there are no adjacent verices. In the 
  second case the algorithm climbs up the DFS tree untill there are parent 
  vertices.

  As said previously the recording odf the finishing time in that manner is
  pure speculation. Although it seems to work using simple examples there is
  no mathematical demonstration around it.

- The `DfsEdgeTypeGraph` classifies all edges of a graph under the following 
  categories:
  - Tree edge (*T*): belongs to a BF tree.
  - Back edge (*B*): given an edge `(u,v)` u is an ancestor of v. This means 
    that v has been discovered before u.
  - Forward edge (*F*): given an edge `(u,v)` v is an ancestor of u. This means 
    that u has been discovered before v.
  - Cross edge (*C*): An edge wich is none of the previous classifications.
    These edges can go between vertices of a same BF tree or two different 
    BF trees.
  To do the actual classification the parenthesis property theorem, and similar
  have been used, so the discovery and finish attributes of each vertex have 
  been used.

- The `DfsEdgeTypeGraphNoTimes` does the same classification of `DfsEdgeTypeGraph`,
  but instead of using the former attributes for the *B* and *F* type edges, it 
  simply checks if a vertex is an ancestor of the other. This is done by 
  traversing the BF tree in the right manner using the parent attributes. This 
  version can also tell if a cross vertex is between two different BF trees or 
  not. *Warning: this algorithm has not been proven to be right (although it 
  seems so)*.

- The `TopologicalSortGraph` class implements the topological sorting algorithm 
  on top of DFS. To store the sorted vertices, a stack is used instead of a 
  list, since the vertices need to be added on the head of the list. So a stack 
  seemed better in this case. The test function runs topological sort on the 
  graph in figure `22.8` for the exercise `22.4-1` in the CLRS book.
  The result of this test has been confirmed working correcly on pen and 
  paper. 

- The `DagSimplePathsGraph` class counts the number of simple paths from a 
  source vertex `s` to a destination vertex `t` in a directed acyclic graph 
  (dag). Each vertex has an attribute called `path_count` which represent the
  number of simple paths from that vertex to `t`. All detailed explanations
  are available at this link:
  http://courses.cs.tamu.edu/jarvi/2004/f689/assignment3.pdf

- The `UndirectedGraph` implements an undirected graph on top of the directed 
  graph class. To obtain an undirected edge, we need to have two directed edges
  `(u,v)` and `(v,u)` which will represent the undirected edge `(u,v)` (or 
  `(v,u)` which are the same). This means that all atomic operations, like:
  add edge, exists edge, delete edge, are done for both edges.

- The `DfsUndirectedGraph` implements the DFS algorithm on an undirected graph.
  The `dfs` method prints a message if at least one cycle is
  detected, none otherwise. According to various sources, including Wikipedia,
  to have a running time of O(V) for cycle detection under the former 
  conditions, if a gray vertex is found during the search it means that
  a cycle is present. Since at most n - 1 edges can be part of the DF tree
  (given the previous condition of the gray vertices) it means that the 
  algorithm takes O(V). We know that an already discovered vertex is not 
  white. We then need to check that that the adjacent vertex is not connected
  via the "undirected back edge" (each edge is composed by two direct edges).
  We do that by checking the parent field of the current vertex (`u.parent is 
  not v`). We then check the discovery time of both verices to know if v is an 
  ancestor of u. If that is the case we found a cycle.
  Due to iomplementation choices the code presented in this class takes more 
  time than O(V). *This implementation needs anyhow to be verified.*

- The `SccGraph` class implements an algorithm to copute the strongly connected 
  components of a graph. This algorithm runs DFS twice, first on the input graph, then on
  its transposed. In the second case, vertices in the main `for` loop are 
  examined according to the finishing time attribute of each vertex. Once this 
  second run has completed, each resulting DF tree corresponds to a SCC 
  (Strongly Connected Component). This algorithm is similar to the 
  Kosaraju algorithm. To print each tree we examine each vertex and we access 
  its parent attribute until we find the *parent* (the vertex who's parent 
  attribute is NIL). We place the vertex in a list which is part of a set of 
  lists. Each list represents a SCC. Vertices belonging to the *parent*
  vertex are placed in the same list. Finally we remove all empty lists,
  and we obtain all SCCs of the input graph. *Although this implementation 
  has given the same results on paper, for the example on the CLRS, it needs 
  anyhow to be verified.*

- The `SccComponentsGraph` class adds the feature of creating the Graph of the 
  strongly connected components (Gscc), instead of only printing them like  
  in the `SccGraph` class. The vertices of Gscc (Gscc.V) are the SCC. Edges in
  Gscc are created if they connect different SCCs. This is achieved by looking
  at the adjacency list of the original graph: if there is an edge `(u,v)` in 
  G, where `u` belongs to SCC `C` and v to SCC `C'` then the edge `(C,C')` is 
  added in Gscc.

```python
'''
The text of this exercise was adapted from: "Introduction to algorithms, Third
edition", 23.2-2

"The graph G=(V,E) is represented using an adjacency matrix. Write an
implementation of Prim's algorithm that runs in O(V^2) time."

G.M is the edge matrix.

Edge weight values are encoded directly in the matrix.

Each vertex has a key attribute representing the priority in the priority
queue Q. The smaller the value, the sooner the vertex is extracted from Q.

In the adjacency list version w(u,v) is the weight function.
'''

def edge_exists(G,u_index,v_index):
    return G.M[u_index][v_index] is not Inf

def mst_prim_matrix(G,r):
    for u in G.V: # O(V)
        u.key = Inf
        u.parent = None
    r.key = 0
    Q = Priority_queue(G.V)
    while not Q.is_empty(): # O(V)
        u = Q.extract_min()
        i = v.index
        for j in range(0,G.M.size): # O(V)
            if G.edge_exists(i,j):
                if v.belongs_to_q and G.M[i][j] < v.key:
                    v.parent = u
                    v.key = G.M[i][j]
        

# The adjacency list version
def mst_prim(G,w,r):
    for u in G.V: # O(V)
        u.key = Inf
        u.parent = None
    r.key = 0
    Q = Priority_queue(G.V)
    while not Q.is_empty(): # O(V)
        u = Q.extract_min()
        for v in G.Adj[u]:
           if v.belongs_to_q and w(u,v) < v.key:
              v.parent = u
              v.key = w(u,v)
```

```
Problem: Given a G=(V,E), undirected, with positive real weights, find an MST 
T of G so that T minimizes the product of the weight of all the edges. Can this 
be done directly, or by changing the weights of each edge so that they are the 
logarithms of the original weights? Does this technique works for both MST
algorithms?

We will use:
- sum(x0...xn) as the sum of n numbers
- prod(x0...xn) as the product of n numbers
- log(x) as the logarithm of some base of the number x.
- min(xi,xj) as the minmum of a sequence of numbers
- w(u,v) as the weight function of the edge (u,v)
- n->m as a numeric interval for the function that follows it
- WEi as the weight of the edge i

We know that the result of any MST algorithm, such as Kruskal's and Prim's
must minimize the sum of the weight of m edges, where m is a subset of E:
min(1->m:sum(w(u,v))

If we use logarithms we get:
min(1->m:sum(log(w(u,v))

By hypothesis we must obtain:
min(1->m:prod(w(u,v))

Suppose that:
min(1->m:prod(w(u,v)) == min(1->m:sum(log(w(u,v))
which means that both members get to the same MST
(also because all w(u,v) > 0)

then:
min(WE0*WE1*...*WEm) == min(log(WE0)+log(WE1)+...+log(WEm))

By the product property of the logarithms:
log(a*b) = log(a) + log(b), that is an identity:
min(WE0*WE1*...*WEm) == min(log(WE0*WE1*...*WEm)).

Let's call x=WE0*WE1*...*WEm, then:
min(x) == min(log(x))

The log function increases if x increases and x > 0.

This means that there is only a shift of log if we consider the
weights > base_of_the_logarithm. For example if we have
base_of_the_logarithm == 2:

log(2) = 1
log(1) = 0
log(< 1) = < 0
...

Just to be sure I would take base_of_the_logarithm = min(w(u,v)) - 1.

Under this condition all the previous should work for both MST algorithms.
```

## License

python-training/algorithms (c) 2017 by Franco Masotti 
<franco.masotti@student.unife.it>

To the extent possible under law, the person who associated CC0 with
python-training/algorithms has waived all copyright and related or
neighboring rights to python-training/algorithms. This software is
distributed without any warranty.

You should have received a copy of the CC0 legalcode along with this
software.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.


