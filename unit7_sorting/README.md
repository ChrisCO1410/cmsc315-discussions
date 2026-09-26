# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment evaluated and implemented two primary sorting algorithms in Python: **Bubble Sort** and **Merge Sort**. Both algorithms were analyzed based on structural approach, algorithmic complexity, stability, and handling of edge cases.

## Learning Objectives

- Implemented Bubble Sort using iterative nested loops.
- Implemented Merge Sort using a recursive divide-and-conquer strategy.
- Analyzed the performance differences between $O(n^2)$ and $O(n \log n)$ time complexities.
- Conducted edge case testing across multiple datasets.

## Implementation Details

1. **Bubble Sort (`bubble_sort`)**:
    - Created a copy of the input list to prevent unexpected side effects.
    - Used nested loops to compare adjacent elements and swapped out-of-order pairs.
    - Added an early exit flag (`swapped`) to optimize performance for nearly sorted data.

2. **Merge Sort (`merge_sort` & `merge`)**:
    - Implemented a recursive base case to return sub-lists of length 0 or 1.
    - Computed midpoints to divide datasets into equal halves.
    - Designed a merge helper function to combine sorted sub-lists into a consolidated array while preserving relative element order (stability).

3. **Testing & Validation**:
    - Validated both algorithms on primary datasets of varying sizes.
    - Tested edge cases including empty arrays, single-element arrays, pre-sorted lists, reverse-sorted lists, and lists containing duplicate keys.

---

## Reflection Essay

While completing this assignment, I reinforced core computational concepts surrounding iterative comparison sorts and recursive divide-and-conquer paradigms. Implementing Merge Sort deepened my practical understanding of stack frame management during recursive calls and the mechanics of rebuilding sorted arrays through pointer adjustments during the merge phase.

A notable challenge arose when configuring the merge helper function to maintain algorithm stability. Ensuring that elements from the left partition were chosen when values were equal ($\le$) was critical to guaranteeing that identical keys preserved their original relative positioning—a strict requirement for streaming platform metadata sorting.

Comparing the algorithms highlights clear performance trade-offs. Bubble Sort operates with $O(1)$ auxiliary space complexity but suffers from an inefficient $O(n^2)$ average and worst-case time complexity, making it impractical for large datasets. In contrast, Merge Sort guarantees a predictable $O(n \log n)$ time performance across all cases, though it requires $O(n)$ auxiliary memory space for temporary array storage. Merge Sort is the ideal choice for large, dynamic datasets such as streaming platform user ratings, whereas Bubble Sort is limited to educational contexts or minor, nearly sorted inputs.