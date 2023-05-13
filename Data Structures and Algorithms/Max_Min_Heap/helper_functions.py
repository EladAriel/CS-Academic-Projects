# -*- coding: utf-8 -*-
"""
This module contains helper functions for working with a binary tree or a heap data structure.
"""
# Import library
import math

def parent(i):
    """
    Args:
        i (int): Index of the node.

    Returns: 
        int: The position of the parent for node i.
    """
    return math.floor((i - 1) / 2)

def leftChild(i):
    """
    Args:
        i (int): Index of the node.

    Returns: 
        int: The position of the left child for node i.
    """
    return 2 * i + 1

def rightChild(i):
    """
    Args:
        i (int): Index of the node.

    Returns:
        int: The position of the right child for node i.
    """
    return 2 * i + 2

def isLeaf(A, i):
    """
    Args:
        A (list): An array representing the binary tree.
        i (int): Index of the node.

    Returns:
        bool: True if the passed node is a leaf node.
    """
    return i >= len(A) // 2

def node_level(i):
    """
    Args:
        i (int): Index of the node.

    Returns:
        int: The level of the node in the tree.
    """
    return int(math.floor(math.log2(i + 1)))

def exchange(A, first_pos, second_pos):
    """
    Exchange between two nodes of the heap.

    Args:
        A (list): An array representing the max-min heap.
        first_pos (int): The position of the first node.
        second_pos (int): The position of the second node.
    """
    A[first_pos], A[second_pos] = A[second_pos], A[first_pos]

def get_max_child(A, i, n):
    """
    Given a binary tree represented by a array A and an index i,
    return the index of the maximum child or grandchild of node i.

    Args:
        A (list): An array representing the binary tree.
        i (int): Index of the node for which to find the maximum child or grandchild.
        n (int): The length of the heap.

    Returns:
        int: Index of the maximum child or grandchild of node i.
    """
    # Check if i is a valid index
    if i >= n:
        return None
    # Calculate indices of left and right children of node i
    left_child = leftChild(i)
    right_child = rightChild(i)
    # Initialize max_idx as i
    max_idx = i
    # Check if left child is larger than max_val
    if left_child < n:
        left_idx = get_max_child(A, left_child, n)
        if A[left_idx] > A[max_idx]:
            max_idx = left_idx
    # Check if right child is larger than max_val
    if right_child < n:
        right_idx = get_max_child(A, right_child, n)
        if A[right_idx] > A[max_idx]:
            max_idx = right_idx
    return max_idx

def get_min_child(A, i, n):
    """
    Given a binary tree represented by a list A and an index i,
    return the index of the minimum child or grandchild of node i.

    Args:
        A (list): An array representing the binary tree.
        i (int): Index of the node for which to find the minimum child or grandchild.
        n (int): The length of the heap.

    Returns:
        int: Index of the minimum child or grandchild of node i.
    """
    # Check if i is a valid index
    if i >= n:
        return None
    # Calculate indices of left and right children of node i
    left_child = leftChild(i)
    right_child = rightChild(i)
    # Initialize min_idx as i
    min_idx = i
    # Check if left child is smaller than min_val
    if left_child < n:
        left_idx = get_min_child(A, left_child, n)
        if A[left_idx] < A[min_idx]:
            min_idx = left_idx
    # Check if right child is smaller than min_val
    if right_child < n:
        right_idx = get_min_child(A, right_child, n)
        if A[right_idx] < A[min_idx]:
            min_idx = right_idx
    return min_idx

def isGrandchild(A, child_idx, i, n):
    """
    Determines if a given node index is a grandchild of a 
    specified node index in a binary tree.

    Args:
        A (list):  An array representing the binary tree.
        child_idx (int): Index of the node to check if it is a grandchild.
        i (int): Index of the node to check if it is the grandparent.
        n (int): The length of the heap.

    Returns:
        bool: True if child_idx is a grandchild of i, False otherwise.
    """
    grandparent_idx = parent(parent(child_idx))
    if grandparent_idx < n and grandparent_idx == i:        
        return True
    return False

def even_level_up(A, i):
    """
    Recursively moves a node i up the max-min heap until it is in the correct position.
    Assumes that the node's key is greater than its grandparent's key, if it has one.

    Args:
        A (list): An array representing a max-min heap.
        i (int): The index of the node to be moved up the heap.
    """
    # Calculate the index of the grandparent node
    grandparent_idx = parent(parent(i))
    # Check that the grandparent node exists and that the node is greater than its grandparent
    if grandparent_idx >= 0 and A[i] > A[grandparent_idx]:
        # Swap the node with its grandparent
        exchange(A, i, grandparent_idx)
        # Recursively call the function with the index of the grandparent node
        even_level_up(A, i=grandparent_idx)

def odd_level_up(A, i):
    """
    Recursively moves a node i up the max-min heap until it is in the correct position.
    Assumes that the node's key is smaller than its grandparent's key, if it has one.

    Args:
        A (list): An array representing a max-min heap.
        i (int): The index of the node to be moved up the heap.
    """
    # Calculate the index of the grandparent node
    grandparent_idx = parent(parent(i))
    # Check that the grandparent node exists and that the node is less than its grandparent
    if grandparent_idx >= 0 and A[i] < A[grandparent_idx]:
        # Swap the node with its grandparent
        exchange(A, i, grandparent_idx)
        # Recursively call the function with the index of the grandparent node
        odd_level_up(A, i=grandparent_idx)