"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.
    """
    # Create a copy of the list to avoid mutating the original input
    arr = lst.copy()
    n = len(arr)

    # Outer loop for each pass through the list
    for i in range(n):
        swapped = False
        # Inner loop compares adjacent elements up to the unsorted portion boundary
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Optimization: If no elements were swapped during a pass, the list is already sorted
        if not swapped:
            break

    return arr


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    i = j = 0

    # Compare values from both lists and build the merged list in ascending order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left or right sub-lists
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.
    """
    # Base case: lists of length 0 or 1 are already sorted
    if len(lst) <= 1:
        return lst

    # Divide step: find the midpoint and split the list into left and right halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Conquer step: recursively sort both sub-lists
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine step: merge the sorted sub-lists together
    return merge(left_sorted, right_sorted)


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    dataset_1 = [87, 12, 45, 99, 23, 56, 1, 34]
    print(f"Original Dataset #1: {dataset_1}")

    bubble_res_1 = bubble_sort(dataset_1)
    print(f"Bubble Sort Result:  {bubble_res_1}")

    merge_res_1 = merge_sort(dataset_1)
    print(f"Merge Sort Result:   {merge_res_1}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    dataset_2 = [500, 120, 850, 310, 420, 150, 990, 270, 600]
    print(f"Original Dataset #2: {dataset_2}")

    bubble_res_2 = bubble_sort(dataset_2)
    print(f"Bubble Sort Result:  {bubble_res_2}")

    merge_res_2 = merge_sort(dataset_2)
    print(f"Merge Sort Result:   {merge_res_2}")

    print("\nComparison Summary:")
    print("- Both algorithms successfully sorted Datasets #1 and #2 in ascending order.")
    print("- Bubble Sort operates in O(n^2) worst/average time using nested loops.")
    print("- Merge Sort operates in O(n log n) time by splitting datasets recursively.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    edge_cases = {
        "Empty List": [],
        "Single Element List": [42],
        "Already Sorted List": [10, 20, 30, 40, 50],
        "Reverse-Sorted List": [90, 70, 50, 30, 10],
        "List with Duplicates": [15, 5, 15, 2, 5, 15]
    }

    for label, test_list in edge_cases.items():
        print(f"\nTest Case: {label}")
        print(f"  Input:          {test_list}")
        print(f"  Bubble Sort:    {bubble_sort(test_list)}")
        print(f"  Merge Sort:     {merge_sort(test_list)}")

    print("\nEdge Case Behavior Analysis:")
    print("1. Empty & Single-Element Lists: Both algorithms return the list intact immediately without error.")
    print("2. Already Sorted List: Bubble Sort exits after 1 pass (O(n) best-case); Merge Sort still splits/merges in O(n log n).")
    print("3. Reverse-Sorted List: Triggers maximum swaps in Bubble Sort (O(n^2) worst-case). Merge Sort handles it predictably in O(n log n).")
    print("4. Duplicate Values: Both algorithms retain stability, keeping identical elements in their original relative order.")


if __name__ == "__main__":
    main()