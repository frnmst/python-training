## Source

From the Cormen et alia book

## Class diagrams

```

           +------+
           | list |                           +-------+
           +------+                           | Graph |
              ^                               +-------+
              |                                   ^     \
     _________|_________                          |     ^
    |                   |                         |     |    
    |                   |                         |     |
+-------+           +-------+               +----------+|
| Stack |           | Queue |<------------- | BfsGraph ||
+-------+           +-------+               +----------+|
    ^                   ^                               |
    |                   |                               /
    |                   |                   +----------+
    |___________________|                   | DfsGraph |
               ^                            +----------+
               |
               |
             +-----+
             | Bst |
             +-----+
                ^
                |
    ____________|________________
   |                  |          |
   |                  |          |
   |                  |          |
+-------------+  +---------+  +-----+
| BstSameKeys |  | BstSort |  | Rbt |
+-------------+  +---------+  +-----+


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

#### Explanation

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

```

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


FindSet(S):
    return S.tail

Union(S1,S2):
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

## License

python-training/algorithms (c) 2017 by Franco Masotti 
<franco.masotti@student.unife.it>

To the extent possible under law, the person who associated CC0 with
python-training/algorithms has waived all copyright and related or
neighboring rights to python-training/algorithms. This software is
distributed without any warranty.

You should have received a copy of the CC0 legalcode along with this
software.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.


