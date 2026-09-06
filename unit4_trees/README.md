# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduced Binary Search Trees (BSTs) and recursive tree operations implemented in Python.

## Learning Objectives

- Built a functional Binary Search Tree.
- Inserted key values recursively maintaining BST constraints.
- Executed recursive search operations.
- Performed in-order traversal to retrieve sorted outputs.
- Evaluated BST performance and edge case behaviors.

## Implementation Summary (Past Tense)

- **Node & Tree Setup**: Constructed `Node` and `BST` classes to represent tree nodes with left and right pointers.
- **Recursive Insertion**: Implemented `insert` and `_insert_recursive` to recursively direct values smaller than the current node to the left child and larger values to the right child.
- **Search Routine**: Created `search` and `_search_recursive` to navigate down binary branches, halving the search space at each node.
- **In-Order Traversal**: Built `inorder` and `_inorder_recursive` following the Left-Root-Right pattern, verifying that elements were returned in sorted ascending order.
- **Edge Case Management**: Protected operations against empty tree searches (returning `False` and empty lists cleanly) and duplicate value insertions (retaining unique keys).

## Discussion Board Reflection

### 1. What concepts or skills did you learn while completing this assignment?
I strengthened my practical understanding of recursive tree algorithms, pointer manipulation in Python, and how spatial properties ($key_{left} < key_{root} < key_{right}$) simplify data lookups.

### 2. What challenges did you encounter, and how did you overcome them?
Managing base cases during recursive search and preventing duplicate node pollution was a challenge. I overcame this by explicitly checking for `node is None` at the top of recursive methods and adding a duplicate guard statement to return the unchanged node early when `value == node.value`.

### 3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
BSTs maintain order dynamically during insertion. Unlike an unsorted linear array or linked list requiring $O(n)$ time to search, a balanced BST eliminates half of the remaining candidates with each node comparison, achieving $O(\log n)$ efficiency. However, if keys are inserted in strictly sorted order, the tree degrades into a single branch (resembling a linked list), dropping efficiency back down to $O(n)$.