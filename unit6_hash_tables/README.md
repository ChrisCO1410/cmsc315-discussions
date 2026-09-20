# Unit 6 Discussion: Search Algorithms & Hash Tables

## Overview

This assignment examined Python dictionaries as hash tables, demonstrating key-value storage, $O(1)$ lookup operations, updates, safe deletions, and edge case handling.

## Learning Objectives

- Implemented key-value pair insertions
- Utilized dictionary lookups for efficient data retrieval
- Updated stored values using direct key indexing
- Safely removed entries using built-in methods
- Evaluated hashing mechanisms and collision handling concepts

## Implementation Summary

A network device inventory lookup tool was modeled to demonstrate hash table functionality in a practical system setting.

- **Insertion**: Populated a dictionary with initial network asset IDs mapped to device names.
- **Lookup**: Retrieved specific device names directly using asset ID keys in $O(1)$ average time.
- **Update**: Replaced an outdated access point device name with an upgraded model name by assigning a new value to an existing key.
- **Deletion**: Used `del` and safe `.pop()` calls to remove decommissioned hardware entries.
- **Edge Cases**: Demonstrated handling missing keys using `.get()` and safe deletions using `.pop(key, default)` to prevent runtime `KeyError` exceptions.

## Reflection Essay

Completing this assignment reinforced how Python dictionaries leverage internal hash functions to map arbitrary key objects to specific memory buckets. This design enables average $O(1)$ time complexity for key insertions, lookups, and deletions because the program calculates the target memory index directly rather than scanning sequentially through stored items.

The main challenge encountered during implementation was handling missing keys safely without crashing the execution context. Directly accessing or removing an unindexed key triggers a `KeyError`. This was resolved by using defensive access patterns like `.get()` with default return strings and `.pop(key, default)` for deletions.

Hash tables maintain high performance by converting keys into numeric indices via hashing. However, when two distinct keys yield identical bucket locations, a collision occurs. Systems resolve collisions through open addressing or separate chaining. If a hash table becomes overcrowded or experiences excessive collisions, performance degrades from optimal $O(1)$ time toward linear $O(n)$ time as lookup operations fall back to searching collision lists.