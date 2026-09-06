"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:

  def __init__(self, value):
    # TODO (Student):
    # Store the node's value and initialize references
    # to the left and right child nodes.
    self.value = value
    self.left = None
    self.right = None


class BST:

  def __init__(self):
    # TODO (Student):
    # Initialize an empty Binary Search Tree.
    self.root = None

  def insert(self, value):
    """TODO (Student):

    Insert a value into the BST.

    Requirements:
    - Use the recursive helper method.
    - Add comments explaining why insertion depends on
      whether a value is smaller or larger than the
      current node.
    """
    # Insertion depends on comparing the new value to the current node's value.
    # By placing smaller values in the left subtree and larger values in the right
    # subtree, we maintain the fundamental BST ordering property required for fast lookups.
    self.root = self._insert_recursive(self.root, value)

  def _insert_recursive(self, node, value):
    """TODO (Student):

    Implement recursive BST insertion.

    Requirements:
    - Create a new node when a position is found.
    - Insert smaller values into the left subtree.
    - Insert larger values into the right subtree.
    - Return the updated node reference.
    """
    # Base Case: Found an empty slot, create and return a new Node
    if node is None:
      return Node(value)

    # Ignore exact duplicates to maintain unique set properties in the BST
    if value == node.value:
      return node

    # Recursive steps to traverse left or right
    if value < node.value:
      node.left = self._insert_recursive(node.left, value)
    else:
      node.right = self._insert_recursive(node.right, value)

    return node

  def search(self, value):
    """TODO (Student):

    Search for a value in the BST.

    Requirements:
    - Return True if found.
    - Return False if not found.
    - Add comments explaining why BST search is often
      more efficient than linear search.
    """
    # Searching a BST is significantly faster than a linear search on an unsorted list (O(n)).
    # Because the BST is ordered, each step down the tree compares the target value against
    # the current node and eliminates half of the remaining subtrees, achieving O(log n) efficiency.
    return self._search_recursive(self.root, value)

  def _search_recursive(self, node, value):
    """TODO (Student):

    Implement recursive BST search.
    """
    # Base cases: value not found (reached leaf child) or value matched
    if node is None:
      return False
    if node.value == value:
      return True

    # Recur down left or right subtree based on value comparison
    if value < node.value:
      return self._search_recursive(node.left, value)
    return self._search_recursive(node.right, value)

  def inorder(self):
    """TODO (Student):

    Return a list containing the values from an
    in-order traversal.
    """
    values = []
    self._inorder_recursive(self.root, values)
    return values

  def _inorder_recursive(self, node, values):
    """TODO (Student):

    Implement in-order traversal.

    Requirements:
    - Visit the left subtree.
    - Visit the current node.
    - Visit the right subtree.
    - Add comments explaining why this traversal
      produces sorted output in a BST.
    """
    # In-order traversal follows: Left Subtree -> Current Node -> Right Subtree.
    # Because all values in the left subtree are guaranteed to be smaller than the node,
    # and all values in the right subtree are larger, visiting them in this sequence
    # guarantees that elements are appended in strict ascending sorted order.
    if node is not None:
      self._inorder_recursive(node.left, values)
      values.append(node.value)
      self._inorder_recursive(node.right, values)


def main():
  print("=== UNIT 4: BINARY SEARCH TREES ===")

  # ===============================
  # TODO (Student): BUILD A TREE
  # ===============================
  #
  # Requirements:
  # 1. Create a BST object.
  # 2. Insert at least 7 values.
  # 3. Include values that go into both left
  #    and right subtrees.
  # 4. Display the values inserted.
  # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

  print("\n=== TREE CONSTRUCTION ===")
  # Application Scenario: Storing corporate Employee IDs
  # Inserting 1050 first places it as the root to allow balanced left and right branch distribution.
  employee_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1090]
  bst = BST()

  print(f"Inserting Employee IDs into BST: {employee_ids}")
  for emp_id in employee_ids:
    bst.insert(emp_id)

  # Efficiency note:
  # Each level of the BST acts like a decision point. At each node, we eliminate
  # an entire side of the tree, cutting down the remaining search items exponentially.

  # ===============================
  # TODO (Student): IN-ORDER TRAVERSAL
  # ===============================
  #
  # Requirements:
  # 1. Perform an in-order traversal.
  # 2. Display the traversal results.
  # 3. Use comments to explain why the traversal produces
  #    sorted output in a BST.

  print("\n=== IN-ORDER TRAVERSAL ===")
  sorted_values = bst.inorder()
  print(f"In-Order Traversal Result: {sorted_values}")
  # The output matches ascending numerical order because in-order traversal
  # exhaustively collects smaller left children before processing parent nodes and larger right children.

  # ===============================
  # TODO (Student): SEARCH TESTS
  # ===============================
  #
  # Requirements:
  # 1. Search for at least two values that exist.
  # 2. Search for at least two values that do not exist.
  # 3. Use comments to clearly explain the results.

  print("\n=== SEARCH TESTS ===")
  # Existing keys (1035 and 1090) traverse down left-right and right-right paths respectively.
  existing_keys = [1035, 1090]
  for key in existing_keys:
    found = bst.search(key)
    print(f"Searching for ID {key} (Expected: True): {found}")

  # Non-existing keys (9999 and 1000) hit None references during recursive search and safely return False.
  missing_keys = [9999, 1000]
  for key in missing_keys:
    found = bst.search(key)
    print(f"Searching for ID {key} (Expected: False): {found}")

  # ===============================
  # TODO (Student): EDGE CASES
  # ===============================
  #
  # Demonstrate at least one edge case.
  #
  # Example ideas:
  # - Traverse an empty tree
  # - Search an empty tree
  # - Insert duplicate values
  # - Create a tree with only one node
  #
  # Use comments to explain what happens and why.

  print("\n=== EDGE CASES ===")

  # Edge Case 1: Operating on an Empty Tree
  empty_tree = BST()
  print(f"Searching empty tree for 1050: {empty_tree.search(1050)}")
  print(f"In-order traversal on empty tree: {empty_tree.inorder()}")

  # Edge Case 2: Inserting Duplicate Values
  print(f"Attempting to re-insert existing root ID 1050 into active BST...")
  bst.insert(1050)
  print(f"In-order traversal after duplicate insert attempt: {bst.inorder()}")
  # Explanation: Duplicate checks in _insert_recursive prevent duplicate nodes
  # from corrupting tree size or creating redundant branches.


if __name__ == "__main__":
  main()