# Unit 2 Discussion: Stacks and Queues

## Overview
This project implemented two fundamental linear data structures in Python: a Stack (LIFO) and a Queue (FIFO). The program demonstrated operation behavior, edge-case safety and practical application scenarios.

## Implementation Details

### Stack Implementation
- Utilized a standard Python `list` as the internal storage structure.
- Implemented `push()` using `append()` to add items to the top.
- Implemented `pop()` and `peek()` with built-in empty-stack checking to prevent index errors.
- Verified LIFO behavior using a browser navigation history scenario.

### Queue Implementation
- Utilized `collections.deque` for $O(1)$ performance on double-ended operations.
- Implemented `enqueue()` using `append()` and `dequeue()` using `popleft()`.
- Implemented `front()` with empty-queue protection to inspect the head element safely.
- Verified FIFO behavior using an IT support ticket processing scenario.

### Edge Cases Handled
- Popping or dequeuing from empty structures returns `None` and displays explicit error notices without crashing the program.
- Peeking or accessing the front of empty structures safely notifies the caller.
- Single-item insertion and removal cycles were tested to verify proper transition back to empty status (`is_empty() == True`).

## Execution Instructions
Run the script directly using Python 3:
```bash
python unit2_stacks_queues.py