"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Inserting at index 0 shifts all existing elements one position to the right O(N).
    # Inserting in the middle shifts elements after index rightward O(N).
    # Appending to the end requires no shifting and runs in amortized O(1) time.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Index validation prevents runtime IndexError exceptions and unhandled crashes.
    if index < 0 or index >= len(lst):
        print(f"Error: Index {index} is out of bounds for list size {len(lst)}.")
        return None
    # Removing from index 0 shifts remaining elements leftward O(N).
    # Removing from the end requires no shifting O(1).
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Linear search checks elements sequentially from index 0 to len(lst)-1.
    # Best-case complexity is O(1) if value is at index 0; worst-case is O(N) if value is at the end or missing.
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")

    # 1. Create initial inventory list for a game store scenario
    inventory = ["PlayStation 5", "Xbox Series X", "Nintendo Switch"]
    print(f"Original Inventory: {inventory}")

    # 3 & 4. Test insertions at beginning, middle, and end
    print("\n1. Inserting at the beginning (index 0): 'Gaming PC'")
    insert_at(inventory, 0, "Gaming PC")
    print(f"Updated Inventory: {inventory}")

    print("\n2. Inserting in the middle (index 2): 'Steam Deck'")
    insert_at(inventory, 2, "Steam Deck")
    print(f"Updated Inventory: {inventory}")

    print("\n3. Inserting at the end (index len): 'VR Headset'")
    insert_at(inventory, len(inventory), "VR Headset")
    print(f"Updated Inventory: {inventory}")


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")

    # 1, 2, & 3. Demonstrate deletions from beginning, middle, and end
    print("Deleting from beginning (index 0):")
    removed_first = delete_at(inventory, 0)
    print(f"Removed item: {removed_first}")
    print(f"Updated Inventory: {inventory}")

    print("\nDeleting from middle (index 2):")
    removed_mid = delete_at(inventory, 2)
    print(f"Removed item: {removed_mid}")
    print(f"Updated Inventory: {inventory}")

    print("\nDeleting from end (last index):")
    removed_end = delete_at(inventory, len(inventory) - 1)
    print(f"Removed item: {removed_end}")
    print(f"Updated Inventory: {inventory}")


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")

    # 1. Search for existing value
    target_existing = "Steam Deck"
    idx_found = search_value(inventory, target_existing)
    print(f"Searching for existing item '{target_existing}'...")
    print(f"Result index: {idx_found}")

    # 2. Search for missing value
    target_missing = "PlayStation 5"
    idx_missing = search_value(inventory, target_missing)
    print(f"\nSearching for missing item '{target_missing}'...")
    print(f"Result index: {idx_missing}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge Case 1: Out of bounds deletion index
    print("1. Edge Case: Deleting with an out-of-bounds index (index 10)")
    invalid_del = delete_at(inventory, 10)
    print(f"Result: {invalid_del}")

    # Edge Case 2: Deleting from an empty list
    empty_lst = []
    print("\n2. Edge Case: Deleting from an empty list (index 0)")
    empty_del = delete_at(empty_lst, 0)
    print(f"Result: {empty_del}")

    # Edge Case 3: Searching inside an empty list
    print("\n3. Edge Case: Searching inside an empty list for 'Gaming PC'")
    empty_search = search_value(empty_lst, "Gaming PC")
    print(f"Result index: {empty_search}")


if __name__ == "__main__":
    main()