# Unit 5 Discussion: Search Algorithms

## Overview
This project implemented and analyzed linear search and binary search algorithms in Python. Performance comparisons were evaluated across small datasets, large-scale datasets (10,000,000 elements), and various edge cases.

## Learning Objectives Achieved
- Implemented `linear_search` with sequential evaluation and $O(n)$ complexity.
- Implemented `binary_search` utilizing a divide-and-conquer approach with $O(\log n)$ complexity.
- Measured and compared execution efficiency across varying dataset sizes.
- Verified robust edge-case handling for edge conditions.

## Requirements Completed
1. Tested both search algorithms on a small dataset of 10 items for existing and missing target keys.
2. Executed comparative tests on a large dataset of 10,000,000 elements to demonstrate logarithmic scaling.
3. Evaluated edge cases including empty lists, single-element arrays, missing items, and target placement at extreme boundaries (first and last indices).
4. Documented algorithm complexities and performance trade-offs directly in code comments and terminal logs.
5. Modeled real-world applicability for sorted vs. unsorted dynamic data structures.

---

## Discussion Board Reflection

### 1. Concepts and Skills Learned
While completing this assignment, I reinforced fundamental algorithm analysis techniques and practical algorithm design in Python. I implemented linear and binary search algorithms from scratch and analyzed how time complexity ($O(n)$ vs. $O(\log n)$) impacts real-world program performance. I also gained experience structuring rigorous unit testing strategies for edge cases, ensuring robust error-free execution on boundary conditions like empty datasets.

### 2. Challenges Encountered and Overcome
Managing loop boundary conditions in binary search posed an initial logic challenge, specifically ensuring correct midpoint calculations (`(low + high) // 2`) and index pointer updates (`low = mid + 1` / `high = mid - 1`) to prevent infinite recursion loops or off-by-one errors. I resolved this by manually stepping through small sub-array boundary traces on paper before executing automated edge-case test suites.

### 3. Linear vs. Binary Search Trade-Offs
Binary search is optimal when performing frequent queries on static, pre-sorted datasets because its logarithmic runtime eliminates half the remaining search space with each iteration. However, sorting an unsorted dataset incurs an initial $O(n \log n)$ computational overhead. Linear search remains the preferred strategy for small lists, unsorted dynamic arrays where data items are frequently inserted/deleted, or linked lists that do not support $O(1)$ random index access.