#!/usr/bin/env python3

#
# heap_sort.py
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

class HeapBase():

    def __init__(B,length):
        B.length = length
        B.heap_size = 0
        B.array = list()

    def _print(B):
        print("Heap data:")
        print("==========")
        print("Heap length: " + str(B.length))
        print("Heap size: " + str(B.heap_size))
        print("Heap array: " + str(B.array))
        print()

    def parent(B,index):
        return math.floor((index-1)/2)

    def left(B,index):
        return (2*index) + 1

    def right(B,index):
        return (2*index) + 2

    def exchange(B,l,r):
        # Direct method:
        # B.array[l], B.array[r] = B.array[r], B.array[l]
        tmp = B.array[l]
        B.array[l] = B.array[r]
        B.array[r] = tmp

class Heap(HeapBase):

    def heap_sort(H):
        H.build_heap()
        for i in range(H.length - 1, 0, -1):
            H.exchange(0,i)
            H.heap_size -= 1
            H.heapify(0)

class MaxHeap(Heap):

    def is_max_heap(H,root_index=0):
        for i in range(root_index,H.heap_size):
            l = H.left(i)
            r = H.right(i)
            if l < H.heap_size:
                if H.array[l] > H.array[i]:
                    return False
            if r < H.heap_size:
                if H.array[r] > H.array[i]:
                    return False

        return True

    # Maintain the heap property by "sifting" (yes, "sifting")
    # the current element down the tree.
    def heapify(H,root_index):
        l = H.left(root_index)
        r = H.right(root_index)

        # Get the largest element between root, left and right.
        if l < H.heap_size and H.array[l] > H.array[root_index]:
            largest = l
        else:
            largest = root_index
        if r < H.heap_size and H.array[r] > H.array[largest]:
            largest = r

        # If largest element is not in the root position,
        # fix the heap recursively.
        if largest != root_index:
            H.exchange(root_index,largest)
            # Run on the index where the old root is now (i.e: where the 
            # "largest" element was before.
            H.heapify(largest)

    def build_heap(H):
        H.heap_size = H.length

        # Leaves are already max heaps since they are 1 node heaps.
        # We can skip them and check the internal nodes instead.
        for i in range(math.floor((H.length-1)/2), -1, -1):
            H.heapify(i)
            assert H.is_max_heap(i)

class MinHeap(Heap):

    def is_min_heap(H,root_index=0):
        for i in range(root_index,H.heap_size):
            l = H.left(i)
            r = H.right(i)
            if l < H.heap_size:
                if H.array[l] < H.array[i]:
                    return False
            if r < H.heap_size:
                if H.array[r] < H.array[i]:
                    return False

        return True


    def heapify(H,root_index):
        l = H.left(root_index)
        r = H.right(root_index)

        if l < H.heap_size and H.array[l] < H.array[root_index]:
            smallest = l
        else:
            smallest = root_index
        if r < H.heap_size and H.array[r] < H.array[smallest]:
            smallest = r

        if smallest != root_index:
            H.exchange(root_index,smallest)
            H.heapify(smallest)

    def build_heap(H):
        H.heap_size = H.length

        for i in range(math.floor((H.length-1)/2), -1, -1):
            H.heapify(i)
            assert H.is_min_heap(i)

def heapify_test():
    mx = MaxHeap(10)
    mx.array = [16,4,10,14,7,9,3,2,8,1]
    mx.heapify(2)
    mx._print()

    assert mx.is_max_heap(2)

def build_heap_test():
    mx = MaxHeap(10)
    mx.array = [4,1,3,2,16,9,10,14,8,7]
    mx.build_heap()
    mx._print()

    assert mx.is_max_heap()

def heap_sort_test():
    mx = MaxHeap(9)
    mx.array = [4,6,1,9,0,43,8,5,54]
    mx.heap_sort()
    mx._print()

    assert mx.is_max_heap()

def test():
    mx = MaxHeap(4)
    mn = MinHeap(4)

    mx.array = [2,1,4,5]
    mn.array = [2,1,4,5]

    mx.heap_sort()
    mn.heap_sort()

    mx._print()
    mn._print()

if __name__ == '__main__':
    heapify_test()
    build_heap_test()
    heap_sort_test()
    test()
    print("All test passed")
