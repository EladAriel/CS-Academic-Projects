# -*- coding: utf-8 -*-
"""
This module provides the implementation of a Max-Min Heap data structure.

A Max-Min Heap is a complete binary tree that satisfies both the max-heap property and the min-heap property. 
In other words, for every non-leaf node `i` in the heap, the key stored at `i` is greater than or equal to the keys 
stored at its children if `i` is even, and less than or equal to the keys stored at its children if `i` is odd. 
The root of the heap always stores the maximum key, and the minimum key can be found either at the root or at the 
level immediately below the root.

This implementation provides the `Max_Min_Heap` class, which allows the following operations:
- `max_min_heapify()`: Maintains the max-min heap property of the binary tree rooted at node i.
- `build_max_min_heap()`:Builds a max-min heap from the input array A.
- `heap_extract_max()`: Extracts the maximum node from a max-min heap.
- `heap_extract_min()`: Extracts the minimum node from a max-min heap.
- `heap_insert()`: Inserts a new node with the given key into the max-min heap.
- `heap_delete()`: Deletes the node at index i from the max-min heap.
- `heap_sort()`: Sorts an input array in ascending order. 

The `Max_Min_Heap` class is implemented using a list to store the keys in the heap.
"""
# Import library
import math
from io import StringIO
from helper_functions import *

class Max_Min_Heap:
    def __init__(self, heap):
        """
        Constructor to initialize the max-min heap with a given array.
        
        Args:
            A (list): An array of numbers to be converted to a max-min heap.
        """
        self.heap = heap

    def even_level_down_heapify(self, A, i, n):
        """
        Recursively restores the min-max heap property for a node i and its descendants,
        assuming the node i is at an even level in the heap and may be larger than one
        or more of its grandchildren.
    
        Args:
            A (list): An array representing the binary tree.
            i (int): The index of the node to restore the min-max heap property for.
            n (int): The length of the heap.
        """
        # Check if node i is not a leaf
        if not isLeaf(A, i):
            # Find the index of the largest child or grandchild of node i
            max_idx = get_max_child(A, i, n)
            # Check if max_idx is a grandchild of node i
            if isGrandchild(A, max_idx, i, n):
                # If largest grandchild are greater than node i, swap their values
                if A[max_idx] > A[i]:
                    exchange(A, max_idx, i)
                    # If the largest grandchild is smaller than their parent, swap their values
                    parent_max_idx = parent(max_idx)
                    if A[max_idx] < A[parent_max_idx]:
                        exchange(A, max_idx, parent_max_idx)
                    # Recursively call max_min_heapify(A, i, n)
                    self.max_min_heapify(A, max_idx, n)
            # If max_idx is not a grandchild of node i, check if it is greater than node i
            elif A[max_idx] > A[i]:
                exchange(A, max_idx, i)

    def odd_level_down_heapify(self, A, i, n):
        """
        Recursively restores the min-max heap property for a node i and its descendants,
        assuming the node i is at an odd level in the heap and may be smaller than one
        or more of its grandchildren.
    
        Args:
            A (list): An array representing the binary tree.
            i (int): The index of the node to restore the min-max heap property for.
            n (int): The length of the heap.
        """
        # Check if node i is not a leaf
        if not isLeaf(A, i):
            # Find the index of the smallest child or grandchild of node i
            min_idx = get_min_child(A, i, n)
            # Check if min_idx is a grandchild of node i
            if isGrandchild(A, min_idx, i, n):
                # If smallest grandchild are smaller than node i, swap their values
                if A[min_idx] < A[i]:
                    exchange(A, min_idx, i)
                    # If the smallest grandchild is greater than their parent, swap their values
                    parent_min_idx = parent(min_idx)
                    if A[min_idx] > A[parent_min_idx]:
                        exchange(A, min_idx, parent_min_idx)
                    # Recursively call max_min_heapify(A, i, n)
                    self.max_min_heapify(A, min_idx, n)
            # If min_idx is not grandchild of node i, check if it is greater than node i
            elif A[min_idx] < A[i]:
                exchange(A, min_idx, i)

    def max_min_heapify(self, A, i, n):
        """
        Maintains the max-min heap property of the binary tree rooted at node i.
    
        Args:
            A (list): An array representing the binary tree.
            i (int): Index of the node to start heapifying from.
        """
        # If the node in even level use even level heapify, else use odd level heapify
        if node_level(i) % 2 == 0:
            self.even_level_down_heapify(A, i, n)
        else:
            self.odd_level_down_heapify(A, i, n)
    
    def build_max_min_heap(self):
        """
        Builds a max-min heap from the input array A.
    
        Returns:
            None: The input array A is modified in place to form a valid max-min heap.
        """
        # Get heap size
        heap_size = len(self.heap)
        # Loop over internal nodes of the heap, starting from the middle and working backwards
        for i in range(heap_size // 2, -1, -1):
            self.max_min_heapify(self.heap, i, len(self.heap))
  
    def heap_extract_max(self):
        """
        Extracts the maximum node from a max-min heap represented as an array.
    
        Returns:
            The maximum node in the heap, or None if the heap is empty.
        """
        # Check if array is empty
        if len(self.heap) < 1:
            return "Heap underflow"
        # The maximum node in max-min heap is at the root
        max_node = self.heap[0]
        # Swap the maximum node with the last element of the heap
        self.heap[0] = self.heap[-1]
        # Remove the last element from the heap
        self.heap.pop(-1)
        # Call max_min_heapify(A, i, n) for i=0 to restore the max-min heap property
        self.max_min_heapify(self.heap, i=0, n=len(self.heap))
        return max_node
    
    def heap_extract_min(self):
        """
        Extracts the minimum node from a max-min heap represented as an array.

        Returns:
            The minimum node in the heap, or None if the heap is empty.
        """
        # Check if array is empty
        if len(self.heap) < 1:
            return "Heap underflow"
        # The minimum node in max-min heap is one of the two children of the root
        left_child_idx = 1
        right_child_idx = 2
        min_idx = 0
        if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[min_idx]:
            min_idx = left_child_idx
        if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[min_idx]:
            min_idx = right_child_idx
        # Define the minimum node as new variable
        min_node = self.heap[min_idx]
        # Swap the maximum node with the last element of the heap
        self.heap[min_idx] = self.heap[-1]
        # Remove the last element from the heap
        self.heap.pop(-1)
        # Call max_min_heapify(A, i, n) for i=min_node_idx to restore the max-min heap property
        self.max_min_heapify(self.heap, i=min_idx, n=len(self.heap))
        return min_node
    
    def heap_increase_key(self, i, key):
        """
        Increase the value of the key at index i in a max-min heap to the given value
        and adjust the heap accordingly.
    
        Args:
            i (int): The index of the value to be increased in the heap.
            key (int): The new value of the key.
        """
        # If i is not the root
        if i != 0:
            # Replace the value at index i with the new key
            self.heap[i] = key
            # Check if the node is on an even or odd level and swap with parent if necessary
            if node_level(i) % 2 == 0: # even level
                if self.heap[i] < self.heap[parent(i)]: # node is smaller than parent, swap
                    exchange(self.heap, i, parent(i))
                    odd_level_up(self.heap, parent(i))
                else:
                    even_level_up(self.heap, i) # node is larger or equal to parent, check even level
            else:  # odd level
                if self.heap[i] > self.heap[parent(i)]: # node is larger than parent, swap
                    exchange(self.heap, i, parent(i))
                    even_level_up(self.heap, parent(i))
                else:
                    odd_level_up(self.heap, i) # node is smaller or equal to parent, check odd level

    def heap_insert(self, key):
        """
         Inserts a new node with the given key into the max-min heap represented by the array A.
        
         Args:
             key (int): The key value of the new node to be inserted into the heap.
        """
        # Insert the new node at end of the max-min heap
        self.heap.append(key)
        # Assign the index of the value to be increased in the heap.
        i = len(self.heap) -1
        # Adjust the heap by moving the new node to its correct position
        self.heap_increase_key(i, key)
    
    def heap_delete(self, i):
        """
        Deletes the node at index i from the max-min heap A.
    
        Args:
            i (int): The index of the node to be deleted from the heap.
        """
        # Check if i is a valid index
        if i >= len(self.heap):
            return None
        # If the node is on even level and greater than lase node or on odd level and smaller than last node
        if (node_level(i) % 2 == 0 and self.heap[i] > self.heap[-1]) or (node_level(i) % 2 == 1 and self.heap[i] < self.heap[-1]):
            # Replace node i with the last node in the heap
            self.heap[i] = self.heap[-1]
            # Restore the min-heap property using max_min_heapify
            self.max_min_heapify(self.heap, i, len(self.heap))
        else:
            # Otherwise, increase the key of the node to be deleted to the value of the last element
            self.heap_increase_key(i, A[-1])
        # Remove the last element from the heap
        self.heap.pop()
    
    def heap_sort(self):
        """
        Sorts an input array in ascending order.
        """
        # Build a max-min heap from the input array
        self.build_max_min_heap()
        # Traverse the internal nodes of the heap in reverse order
        # starting from the second-to-last level
        for i in range(len(self.heap) - 1, 0, -1):
            # Swap the root node with the i-th node
            exchange(self.heap, 0, i)
            # Call max-min heapify on the new root node to restore the max-min heap property
            self.max_min_heapify(self.heap, i=0, n=i)

    def __repr__(self):
        """
        Return a string representation of the heap.
        """
        return str(self.heap)
    
    def __len__(self):
        """
        Return the number of elements in the heap.
        """
        return len(self.heap)