## Source

From the Cormen et alia book

## Classes

### Data stuctures

- Stack
- Queue
- Bst
- BstSameKeys 
- BstSort
- Rbt
- Tree

#### Explanation

- `Stack` and `Queue` classes are very basic as they use python's `List` class
   with very few modifications.

- To avoid recursion in some methods, the `Bst` class imports the previous 
  classes. Since the `Rbt` class is a subclass of `Bst`. We need to apply the 
  DRY (Don't repeat yourself) criteria: in the Bst constructor I added
  the `sentinel` attribute which is always set to `None`. Then, in some 
  methods, I changed the value of the terminating condition from `None` to 
  `T.sentinel`. This enables us to import the code directly and to use it as 
  part of the `Rbt` class methods.

# Run n tests and check that the n lists returned are all equal to each other
# knowing that they have been generated randomly, they have the same size
# and the same unique keys. This means that the MAX - MIN + 1 numbers generated
# above are instered in the data structure randomly.

## License

python-training/algorithms (c) 2017 by Franco Masotti 
<franco.masotti@student.unife.it>

To the extent possible under law, the person who associated CC0 with
python-training/algorithms has waived all copyright and related or
neighboring rights to python-training/algorithms. This software is
distributed without any warranty.

You should have received a copy of the CC0 legalcode along with this
software.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.


