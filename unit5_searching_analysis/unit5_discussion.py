"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks elements sequentially from index 0 to len(lst) - 1.
    # Time Complexity: O(n) linear time.
    # Explanation: In the worst-case scenario (item is at the end or missing),
    # the algorithm must perform n comparisons for a list of size n.
    for index in range(len(lst)):
        if lst[index] == target:
            return index  # Target found, return index immediately
    return -1  # Target not in list


def binary_search(lst, target):
    """
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Binary search operates using a divide-and-conquer strategy on sorted lists.
    # Time Complexity: O(log n) logarithmic time.
    # Explanation: With each iteration, the midpoint is evaluated and half of the
    # remaining search space is eliminated, exponentially reducing search time.
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2  # Find integer midpoint

        if lst[mid] == target:
            return mid  # Target located at midpoint
        elif lst[mid] < target:
            low = mid + 1  # Target is in the right half; eliminate left half
        else:
            high = mid - 1  # Target is in the left half; eliminate right half

    return -1  # Target not found in search space


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET TEST
    # ===============================
    # Testing both algorithms on a small sorted list (10 elements).
    print("\n=== SMALL DATASET TEST ===")
    small_dataset = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_existing = 70
    target_missing = 45

    print(f"Dataset: {small_dataset}")

    # Searching for an existing value
    ls_idx = linear_search(small_dataset, target_existing)
    bs_idx = binary_search(small_dataset, target_existing)
    print(f"Search for existing key ({target_existing}):")
    print(f"  Linear Search Index: {ls_idx}")
    print(f"  Binary Search Index: {bs_idx}")

    # Searching for a missing value
    ls_missing = linear_search(small_dataset, target_missing)
    bs_missing = binary_search(small_dataset, target_missing)
    print(f"Search for missing key ({target_missing}):")
    print(f"  Linear Search Index: {ls_missing}")
    print(f"  Binary Search Index: {bs_missing}")

    # Explanation of results:
    # On small datasets (n=10), both algorithms return correct indices instantly.
    # Linear search checks elements sequentially, whereas binary search divides
    # the search interval in half at each step.

    # ===============================
    # LARGE DATASET TEST
    # ===============================
    # Testing performance scaling on a large sorted dataset (10,000,000 elements).
    print("\n=== LARGE DATASET TEST ===")
    large_dataset = list(range(0, 10000000))  # 10 million elements
    large_target = 9999999  # Worst-case scenario at the very end

    print(f"Dataset Size: {len(large_dataset):,} elements")
    print(f"Searching for target near end of list: {large_target:,}")

    # Linear search worst-case check
    ls_large_idx = linear_search(large_dataset, large_target)
    print(f"Linear Search Index: {ls_large_idx} (Requires ~10,000,000 checks)")

    # Binary search worst-case check
    bs_large_idx = binary_search(large_dataset, large_target)
    print(f"Binary Search Index: {bs_large_idx} (Requires max log2(10,000,000) ~24 checks)")

    # Performance comparison explanation:
    # For a dataset of 10 million elements, linear search requires up to 10 million
    # comparisons O(n). Binary search requires at most 24 comparisons O(log n),
    # demonstrating exponential performance gains as dataset size grows.

    # ===============================
    # EDGE CASE TESTS
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty List
    empty_list = []
    print(f"\n1. Empty List Search: {empty_list}")
    print(f"   Linear Search: {linear_search(empty_list, 10)}")
    print(f"   Binary Search: {binary_search(empty_list, 10)}")
    # Explanation: Handled safely by loop conditions without index errors; returns -1.

    # Edge Case 2: Single-Element List (Element Present)
    single_list = [42]
    print(f"\n2. Single-Element List Search (Target Present): {single_list}")
    print(f"   Linear Search for 42: {linear_search(single_list, 42)}")
    print(f"   Binary Search for 42: {binary_search(single_list, 42)}")

    # Edge Case 3: Single-Element List (Element Missing)
    print(f"\n3. Single-Element List Search (Target Missing): {single_list}")
    print(f"   Linear Search for 99: {linear_search(single_list, 99)}")
    print(f"   Binary Search for 99: {binary_search(single_list, 99)}")

    # Edge Case 4: Target at First Index (Index 0)
    first_elem_list = [5, 15, 25, 35, 45]
    print(f"\n4. Target at First Position: {first_elem_list}")
    print(f"   Linear Search for 5: {linear_search(first_elem_list, 5)} (Best-case O(1) for Linear)")
    print(f"   Binary Search for 5: {binary_search(first_elem_list, 5)}")

    # Edge Case 5: Target at Last Index
    print(f"\n5. Target at Last Position: {first_elem_list}")
    print(f"   Linear Search for 45: {linear_search(first_elem_list, 45)} (Worst-case O(n) for Linear)")
    print(f"   Binary Search for 45: {binary_search(first_elem_list, 45)}")


if __name__ == "__main__":
    main()