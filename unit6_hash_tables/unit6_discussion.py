"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # Python dictionaries act as hash tables under the hood. When a key is added,
    # Python hashes the key using a built-in hash function to map it directly
    # to a specific bucket index, allowing average O(1) time insertion.
    device_inventory = {}

    # Real-World Scenario: A network device inventory mapping Asset IDs (keys) to Device Names (values)
    device_inventory[1012] = "Router-Core-01"
    device_inventory[1048] = "Switch-Floor-02"
    device_inventory[1075] = "Firewall-Main"
    device_inventory[1103] = "Server-DB-01"
    device_inventory[1144] = "AP-Lobby"

    print("Initial Inventory State:")
    for asset_id, device_name in device_inventory.items():
        print(f"  Asset ID: {asset_id} -> Device Name: {device_name}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Dictionary lookups evaluate the key's hash value directly to locate the item's slot
    # in constant average time O(1), without scanning through other elements.
    lookup_id_1 = 1048
    lookup_id_2 = 1103

    device_1 = device_inventory[lookup_id_1]
    device_2 = device_inventory[lookup_id_2]

    print(f"Lookup Asset ID {lookup_id_1}: Found -> {device_1}")
    print(f"Lookup Asset ID {lookup_id_2}: Found -> {device_2}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    update_id = 1144
    print(f"Before Update (Asset ID {update_id}): {device_inventory[update_id]}")

    # Assigning a new value to an existing key hashes the key to locate the existing memory slot
    # and overwrites the stored value without creating duplicate keys.
    device_inventory[update_id] = "AP-Lobby-WiFi6"
    print(f"After Update  (Asset ID {update_id}): {device_inventory[update_id]}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    delete_id = 1075
    print(f"Inventory count before deletion: {len(device_inventory)}")
    print(f"Deleting Asset ID {delete_id} ({device_inventory[delete_id]})...")

    # Deleting a key-value pair removes the reference at the calculated hash index slot,
    # freeing up memory space and adjusting dictionary size.
    del device_inventory[delete_id]

    print(f"Inventory count after deletion: {len(device_inventory)}")
    print("Current Inventory:")
    for asset_id, device_name in device_inventory.items():
        print(f"  Asset ID: {asset_id} -> Device Name: {device_name}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Looking up a missing key safely
    # Direct access like device_inventory[9999] raises a KeyError. Using .get() allows graceful handling.
    missing_id = 9999
    retrieved_device = device_inventory.get(missing_id, "Device Not Found")
    print(f"Edge Case 1 - Safe lookup for missing Asset ID {missing_id}: {retrieved_device}")

    # Edge Case 2: Deleting a missing key safely
    # del device_inventory[9999] would crash the application. Using .pop(key, None) deletes safely if present.
    safe_deleted_value = device_inventory.pop(missing_id, "Asset ID not present - No action taken")
    print(f"Edge Case 2 - Safe deletion attempt for missing Asset ID {missing_id}: {safe_deleted_value}")

    # Edge Case 3: Updating or inserting on a missing key
    # Assigning to a missing key does not fail; Python automatically hashes the new key and inserts it.
    new_asset_id = 1200
    print(f"Edge Case 3 - Setting value for new key {new_asset_id}...")
    device_inventory[new_asset_id] = "Switch-Core-Backup"
    print(f"Updated Inventory State (Asset ID {new_asset_id} added): {device_inventory[new_asset_id]}")


if __name__ == "__main__":
    main()