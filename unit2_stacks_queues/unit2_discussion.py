"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Appending to the end of the list ensures the newest item sits at the top of the stack (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            print("Error: Cannot pop from an empty stack.")
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek inspects the top item (most recently added) without altering stack contents.
        if self.is_empty():
            print("Error: Cannot peek at an empty stack.")
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Appending to the right side places incoming items at the rear of the line (FIFO).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            print("Error: Cannot dequeue from an empty queue.")
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front returns the oldest item waiting in line without removing it from the queue.
        if self.is_empty():
            print("Error: Cannot view front of an empty queue.")
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")

    # 1. Create a Stack object
    browser_stack = Stack()

    # 2. Add at least 4 values to the stack
    print("Pushing pages onto browser history stack...")
    pages = ["google.com", "github.com", "umgc.edu", "zybooks.com"]
    for page in pages:
        browser_stack.push(page)
        print(f"Pushed: {page}")

    # 3 & 4. Improve print statements and demonstrate LIFO behavior
    print(f"\nCurrent Top Page (Peek): {browser_stack.peek()}")
    print("\nSimulating Back Button (Popping LIFO):")
    while not browser_stack.is_empty():
        popped_page = browser_stack.pop()
        print(f"Navigated back from: {popped_page}")

    # 5 & 6. Show popping and peeking on an empty stack
    print("\n-- Edge Cases: Empty Stack Operations --")
    print("Attempting to pop from an empty stack:")
    browser_stack.pop()
    print("Attempting to peek at an empty stack:")
    browser_stack.peek()

    # 7. Single-item stack edge case
    print("\n-- Edge Case: Single-Item Stack --")
    browser_stack.push("standalone_page.html")
    print(f"Pushed single item. Stack empty? {browser_stack.is_empty()}")
    popped_single = browser_stack.pop()
    print(f"Popped item: {popped_single}")
    print(f"Stack empty after removal? {browser_stack.is_empty()}")


    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")

    # 1. Create a Queue object
    ticket_queue = Queue()

    # 2. Add at least 4 values to the queue
    print("Enqueuing support desk tickets...")
    tickets = ["Ticket #101: Reset Password", "Ticket #102: Printer Error",
               "Ticket #103: VPN Failure", "Ticket #104: Software Install"]
    for ticket in tickets:
        ticket_queue.enqueue(ticket)
        print(f"Enqueued: {ticket}")

    # 3 & 4. Improve print statements and demonstrate FIFO behavior
    print(f"\nNext Ticket in Line (Front): {ticket_queue.front()}")
    print("\nProcessing Tickets in Arrival Order (Dequeuing FIFO):")
    while not ticket_queue.is_empty():
        processed = ticket_queue.dequeue()
        print(f"Processed: {processed}")

    # 5 & 6. Show dequeuing and viewing front on an empty queue
    print("\n-- Edge Cases: Empty Queue Operations --")
    print("Attempting to dequeue from an empty queue:")
    ticket_queue.dequeue()
    print("Attempting to view front of an empty queue:")
    ticket_queue.front()

    # 7. Single-item queue edge case
    print("\n-- Edge Case: Single-Item Queue --")
    ticket_queue.enqueue("Ticket #999: Urgent Fix")
    print(f"Enqueued single ticket. Queue empty? {ticket_queue.is_empty()}")
    dequeued_single = ticket_queue.dequeue()
    print(f"Dequeued ticket: {dequeued_single}")
    print(f"Queue empty after removal? {ticket_queue.is_empty()}")


if __name__ == "__main__":
    main()