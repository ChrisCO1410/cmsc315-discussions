# Unit 3 Discussion: List Operations

## Overview
This project evaluated list operations in Python, specifically testing element insertion, deletion and sequential searching. The program analyzed how array-based list shifting impacts performance across different positions.

## Implementation Details

### List Operations
- Implemented `insert_at()` using Python's built-in `.insert()`, documenting how element shifting creates $O(N)$ time complexity when inserting at the beginning or middle of an array-backed list.
- Implemented `delete_at()` with explicit boundary validation (`index < 0` or `index >= len(lst)`). Returning `None` and printing an error prevented unexpected `IndexError` exceptions.
- Implemented `search_value()` using a linear search loop that checks entries sequentially from index 0 through `len(lst) - 1`, returning `-1` when items are not present.

### Edge Cases Handled
- Tested deletion using out-of-bounds indices to confirm clean error logging.
- Executed deletion attempts on an empty list to verify boundary safety.
- Searched inside an empty list to ensure linear search returns `-1` without throwing runtime errors.

## Execution Instructions
Run the script directly using Python 3:
```bash
python unit3_discussion.py