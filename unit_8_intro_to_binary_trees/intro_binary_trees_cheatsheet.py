"""
INTRODUCTION TO BINARY TREES - COMPLETE CHEATSHEET
==================================================

What is a Binary Tree?
A hierarchical data structure where each node has at most two children:
- Left child
- Right child

Tree Terminology:
- Root: Top node of the tree
- Parent: Node that has children
- Child: Node connected below another node
- Leaf: Node with no children
- Sibling: Nodes with the same parent
- Ancestor: Any node on the path from root to current node
- Descendant: Any node reachable from current node
- Subtree: Tree formed by a node and all its descendants
- Height: Longest path from node to leaf
- Depth/Level: Distance from root to node
- Size: Total number of nodes in tree

Types of Binary Trees:
1. Full Binary Tree: Every node has 0 or 2 children
2. Complete Binary Tree: All levels filled except possibly last (filled left to right)
3. Perfect Binary Tree: All internal nodes have 2 children, all leaves at same level
4. Binary Search Tree (BST): Left subtree < node < right subtree
5. Balanced Tree: Height difference between subtrees ≤ 1

When to Use Binary Trees:
✓ Hierarchical data representation
✓ Fast searching (BST: O(log n))
✓ Expression parsing
✓ Decision making systems
✓ File system structures
"""

from collections import deque
from typing import Optional, List, Any

# ===== BASIC NODE DEFINITION =====

class TreeNode:
    """Basic binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"
    
    def __str__(self):
        return str(self.val)


# ===== TREE CREATION UTILITIES =====

def create_tree_from_list(arr):
    """
    Create binary tree from list (level-order).
    None represents missing nodes.
    
    Example: [1, 2, 3, None, 4] creates:
        1
       / \
      2   3
       \
        4
    """
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        node = queue.popleft()
        
        # Add left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root


def create_bst_from_sorted_list(arr):
    """
    Create balanced BST from sorted array.
    Time: O(n), Space: O(log n)
    """
    def build_bst(left, right):
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        root = TreeNode(arr[mid])
        root.left = build_bst(left, mid - 1)
        root.right = build_bst(mid + 1, right)
        return root
    
    return build_bst(0, len(arr) - 1)


# ===== TREE TRAVERSALS =====

def inorder_traversal(root):
    """
    Inorder: Left → Root → Right
    For BST: gives sorted order
    Time: O(n), Space: O(h) where h is height
    """
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)   # Visit left
            result.append(node.val)  # Visit root
            inorder(node.right)  # Visit right
    
    inorder(root)
    return result


def preorder_traversal(root):
    """
    Preorder: Root → Left → Right
    Used for: copying tree, prefix expressions
    Time: O(n), Space: O(h)
    """
    result = []
    
    def preorder(node):
        if node:
            result.append(node.val)  # Visit root
            preorder(node.left)      # Visit left
            preorder(node.right)     # Visit right
    
    preorder(root)
    return result


def postorder_traversal(root):
    """
    Postorder: Left → Right → Root
    Used for: deleting tree, postfix expressions
    Time: O(n), Space: O(h)
    """
    result = []
    
    def postorder(node):
        if node:
            postorder(node.left)     # Visit left
            postorder(node.right)    # Visit right
            result.append(node.val)  # Visit root
    
    postorder(root)
    return result


def level_order_traversal(root):
    """
    Level Order: Visit nodes level by level (BFS)
    Time: O(n), Space: O(w) where w is max width
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


def level_order_by_levels(root):
    """
    Level order traversal grouped by levels.
    Returns list of lists.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


# ===== ITERATIVE TRAVERSALS =====

def inorder_iterative(root):
    """Iterative inorder traversal using stack."""
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process current node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result


def preorder_iterative(root):
    """Iterative preorder traversal using stack."""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first, then left (stack is LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


def postorder_iterative(root):
    """Iterative postorder traversal using two stacks."""
    if not root:
        return []
    
    result = []
    stack1 = [root]
    stack2 = []
    
    # First stack for traversal, second for result order
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    # Pop from second stack to get postorder
    while stack2:
        result.append(stack2.pop().val)
    
    return result


# ===== BASIC TREE PROPERTIES =====

def tree_height(root):
    """
    Calculate height of tree.
    Height = longest path from root to leaf
    Time: O(n), Space: O(h)
    """
    if not root:
        return -1  # Height of empty tree is -1
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return 1 + max(left_height, right_height)


def tree_size(root):
    """
    Count total number of nodes.
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    return 1 + tree_size(root.left) + tree_size(root.right)


def tree_depth(root, target):
    """
    Find depth of target node.
    Depth = distance from root to node
    Time: O(n), Space: O(h)
    """
    def find_depth(node, target, depth):
        if not node:
            return -1
        
        if node.val == target:
            return depth
        
        # Search in left subtree
        left_depth = find_depth(node.left, target, depth + 1)
        if left_depth != -1:
            return left_depth
        
        # Search in right subtree
        return find_depth(node.right, target, depth + 1)
    
    return find_depth(root, target, 0)


def count_leaves(root):
    """
    Count number of leaf nodes.
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1  # This is a leaf
    
    return count_leaves(root.left) + count_leaves(root.right)


def tree_sum(root):
    """
    Calculate sum of all node values.
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    return root.val + tree_sum(root.left) + tree_sum(root.right)


def tree_max(root):
    """
    Find maximum value in tree.
    Time: O(n), Space: O(h)
    """
    if not root:
        return float('-inf')
    
    left_max = tree_max(root.left)
    right_max = tree_max(root.right)
    
    return max(root.val, left_max, right_max)


def tree_min(root):
    """
    Find minimum value in tree.
    Time: O(n), Space: O(h)
    """
    if not root:
        return float('inf')
    
    left_min = tree_min(root.left)
    right_min = tree_min(root.right)
    
    return min(root.val, left_min, right_min)


# ===== TREE VALIDATION =====

def is_same_tree(p, q):
    """
    Check if two trees are identical.
    Time: O(n), Space: O(h)
    """
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))


def is_symmetric(root):
    """
    Check if tree is symmetric (mirror of itself).
    Time: O(n), Space: O(h)
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    if not root:
        return True
    
    return is_mirror(root.left, root.right)


def is_valid_bst(root):
    """
    Check if tree is a valid Binary Search Tree.
    Time: O(n), Space: O(h)
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))


def is_balanced(root):
    """
    Check if tree is height-balanced.
    Balanced: height difference between subtrees ≤ 1
    Time: O(n), Space: O(h)
    """
    def check_balance(node):
        if not node:
            return True, 0
        
        left_balanced, left_height = check_balance(node.left)
        if not left_balanced:
            return False, 0
        
        right_balanced, right_height = check_balance(node.right)
        if not right_balanced:
            return False, 0
        
        balanced = abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)
        
        return balanced, height
    
    balanced, _ = check_balance(root)
    return balanced


# ===== TREE SEARCH OPERATIONS =====

def search_tree(root, target):
    """
    Search for value in tree (any binary tree).
    Time: O(n), Space: O(h)
    """
    if not root:
        return False
    
    if root.val == target:
        return True
    
    return search_tree(root.left, target) or search_tree(root.right, target)


def search_bst(root, target):
    """
    Search in Binary Search Tree (optimized).
    Time: O(h), Space: O(h) - O(log n) for balanced
    """
    if not root:
        return False
    
    if root.val == target:
        return True
    elif target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)


def find_path(root, target):
    """
    Find path from root to target node.
    Returns list of nodes in path.
    Time: O(n), Space: O(h)
    """
    def find_path_helper(node, target, path):
        if not node:
            return False
        
        path.append(node.val)
        
        if node.val == target:
            return True
        
        if (find_path_helper(node.left, target, path) or 
            find_path_helper(node.right, target, path)):
            return True
        
        path.pop()  # Backtrack
        return False
    
    path = []
    find_path_helper(root, target, path)
    return path


# ===== BST OPERATIONS =====

def insert_bst(root, val):
    """
    Insert value into BST.
    Time: O(h), Space: O(h)
    """
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_bst(root.left, val)
    elif val > root.val:
        root.right = insert_bst(root.right, val)
    # If val == root.val, don't insert (no duplicates)
    
    return root


def delete_bst(root, val):
    """
    Delete value from BST.
    Time: O(h), Space: O(h)
    """
    if not root:
        return None
    
    if val < root.val:
        root.left = delete_bst(root.left, val)
    elif val > root.val:
        root.right = delete_bst(root.right, val)
    else:
        # Node to delete found
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # Node has two children: find inorder successor
            successor = find_min_bst(root.right)
            root.val = successor.val
            root.right = delete_bst(root.right, successor.val)
    
    return root


def find_min_bst(root):
    """
    Find minimum value node in BST.
    Time: O(h), Space: O(1)
    """
    while root.left:
        root = root.left
    return root


def find_max_bst(root):
    """
    Find maximum value node in BST.
    Time: O(h), Space: O(1)
    """
    while root.right:
        root = root.right
    return root


# ===== TREE MODIFICATION =====

def invert_tree(root):
    """
    Invert/mirror a binary tree.
    Time: O(n), Space: O(h)
    """
    if not root:
        return None
    
    # Swap left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root


def flatten_tree(root):
    """
    Flatten tree to linked list (preorder).
    Time: O(n), Space: O(h)
    """
    def flatten_helper(node):
        if not node:
            return None
        
        left_tail = flatten_helper(node.left)
        right_tail = flatten_helper(node.right)
        
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        
        return right_tail or left_tail or node
    
    flatten_helper(root)
    return root


# ===== TREE COMPARISON AND ANALYSIS =====

def lowest_common_ancestor(root, p, q):
    """
    Find LCA of two nodes in binary tree.
    Time: O(n), Space: O(h)
    """
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left or right


def diameter_of_tree(root):
    """
    Find diameter of tree (longest path between any two nodes).
    Time: O(n), Space: O(h)
    """
    def diameter_helper(node):
        if not node:
            return 0, 0  # height, diameter
        
        left_height, left_diameter = diameter_helper(node.left)
        right_height, right_diameter = diameter_helper(node.right)
        
        current_height = 1 + max(left_height, right_height)
        current_diameter = max(
            left_diameter,
            right_diameter,
            left_height + right_height
        )
        
        return current_height, current_diameter
    
    _, diameter = diameter_helper(root)
    return diameter


# ===== TREE VISUALIZATION =====

def print_tree_pretty(root, level=0, prefix="Root: "):
    """
    Pretty print tree structure.
    """
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left:
                print_tree_pretty(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree_pretty(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


def tree_to_string(root):
    """
    Convert tree to string representation.
    """
    if not root:
        return "Empty Tree"
    
    def build_string(node, level=0):
        if not node:
            return ""
        
        result = "  " * level + str(node.val) + "\n"
        if node.left or node.right:
            result += build_string(node.left, level + 1)
            result += build_string(node.right, level + 1)
        
        return result
    
    return build_string(root)


# ===== TREE CONVERSION =====

def tree_to_list_levelorder(root):
    """
    Convert tree to list (level order with None for missing nodes).
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result


def bst_to_sorted_list(root):
    """
    Convert BST to sorted list (inorder traversal).
    """
    return inorder_traversal(root)


# ===== UTILITY FUNCTIONS =====

def tree_paths(root):
    """
    Find all root-to-leaf paths.
    Time: O(n), Space: O(h)
    """
    def find_paths(node, current_path, all_paths):
        if not node:
            return
        
        current_path.append(node.val)
        
        # If leaf node, add path to result
        if not node.left and not node.right:
            all_paths.append(current_path[:])  # Copy path
        else:
            find_paths(node.left, current_path, all_paths)
            find_paths(node.right, current_path, all_paths)
        
        current_path.pop()  # Backtrack
    
    paths = []
    find_paths(root, [], paths)
    return paths


def has_path_sum(root, target_sum):
    """
    Check if tree has root-to-leaf path with given sum.
    Time: O(n), Space: O(h)
    """
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == target_sum
    
    remaining_sum = target_sum - root.val
    return (has_path_sum(root.left, remaining_sum) or 
            has_path_sum(root.right, remaining_sum))


# ===== TEST FUNCTIONS =====

def test_tree_creation():
    """Test tree creation methods."""
    print("=== TESTING TREE CREATION ===\n")
    
    # Create tree from list
    arr = [1, 2, 3, None, 4, 5, 6]
    root = create_tree_from_list(arr)
    print(f"Tree from list {arr}:")
    print_tree_pretty(root)
    print()
    
    # Create BST from sorted array
    sorted_arr = [1, 2, 3, 4, 5, 6, 7]
    bst = create_bst_from_sorted_list(sorted_arr)
    print(f"BST from sorted array {sorted_arr}:")
    print_tree_pretty(bst)
    print()


def test_traversals():
    """Test tree traversal methods."""
    print("=== TESTING TRAVERSALS ===\n")
    
    # Create sample tree:    1
    #                      /   \
    #                     2     3
    #                    / \
    #                   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Tree structure:")
    print_tree_pretty(root)
    
    print(f"Inorder (Left-Root-Right): {inorder_traversal(root)}")
    print(f"Preorder (Root-Left-Right): {preorder_traversal(root)}")
    print(f"Postorder (Left-Right-Root): {postorder_traversal(root)}")
    print(f"Level order: {level_order_traversal(root)}")
    print(f"Level order by levels: {level_order_by_levels(root)}")
    print()


def test_tree_properties():
    """Test tree property calculations."""
    print("=== TESTING TREE PROPERTIES ===\n")
    
    root = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    
    print("Tree:")
    print_tree_pretty(root)
    
    print(f"Height: {tree_height(root)}")
    print(f"Size: {tree_size(root)}")
    print(f"Sum: {tree_sum(root)}")
    print(f"Max value: {tree_max(root)}")
    print(f"Min value: {tree_min(root)}")
    print(f"Number of leaves: {count_leaves(root)}")
    print(f"Is balanced: {is_balanced(root)}")
    print(f"Depth of node 5: {tree_depth(root, 5)}")
    print()


def test_bst_operations():
    """Test BST operations."""
    print("=== TESTING BST OPERATIONS ===\n")
    
    # Create BST
    bst = None
    values = [5, 3, 7, 2, 4, 6, 8]
    
    for val in values:
        bst = insert_bst(bst, val)
    
    print(f"BST after inserting {values}:")
    print_tree_pretty(bst)
    
    print(f"Inorder (should be sorted): {inorder_traversal(bst)}")
    print(f"Is valid BST: {is_valid_bst(bst)}")
    print(f"Search for 4: {search_bst(bst, 4)}")
    print(f"Search for 9: {search_bst(bst, 9)}")
    
    # Delete a node
    bst = delete_bst(bst, 3)
    print(f"After deleting 3: {inorder_traversal(bst)}")
    print()


def create_sample_trees():
    """Create various sample trees for testing."""
    print("=== SAMPLE TREES ===\n")
    
    # Perfect binary tree
    perfect = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    print("Perfect Binary Tree:")
    print_tree_pretty(perfect)
    
    # Complete binary tree
    complete = create_tree_from_list([1, 2, 3, 4, 5, 6])
    print("Complete Binary Tree:")
    print_tree_pretty(complete)
    
    # Unbalanced tree
    unbalanced = TreeNode(1)
    unbalanced.left = TreeNode(2)
    unbalanced.left.left = TreeNode(3)
    unbalanced.left.left.left = TreeNode(4)
    print("Unbalanced Tree:")
    print_tree_pretty(unbalanced)


# ===== COMPLEXITY REFERENCE =====
"""
BINARY TREE OPERATIONS COMPLEXITY:

Operation               | Average    | Worst Case | Space
------------------------|------------|------------|-------
Search (BST)           | O(log n)   | O(n)       | O(h)
Insert (BST)           | O(log n)   | O(n)       | O(h)
Delete (BST)           | O(log n)   | O(n)       | O(h)
Search (General)       | O(n)       | O(n)       | O(h)
Traversal              | O(n)       | O(n)       | O(h)
Height Calculation     | O(n)       | O(n)       | O(h)
Size Calculation       | O(n)       | O(n)       | O(h)

Where:
- n = number of nodes
- h = height of tree
- For balanced BST: h = O(log n)
- For unbalanced tree: h = O(n)

TREE TYPES COMPARISON:

Type                | Properties                           | Use Cases
--------------------|--------------------------------------|------------------
Binary Tree         | Each node ≤ 2 children             | General hierarchy
BST                 | Left < Root < Right                 | Searching, sorting
Complete Tree       | All levels full except last        | Heaps, priority queues
Full Tree           | Every node has 0 or 2 children     | Expression trees
Perfect Tree        | All leaves at same level           | Complete structures
Balanced Tree       | Height difference ≤ 1              | Optimal performance

TRAVERSAL CHARACTERISTICS:

Traversal   | Order           | Use Cases                    | Recursive | Iterative
------------|-----------------|------------------------------|-----------|----------
Inorder     | Left-Root-Right | BST sorted output           | Easy      | Medium
Preorder    | Root-Left-Right | Tree copying, prefix expr    | Easy      | Easy
Postorder   | Left-Right-Root | Tree deletion, postfix expr  | Easy      | Hard
Level Order | Level by level  | Tree printing, serialization| Medium    | Easy

COMMON PATTERNS:

1. **Recursive Template**: Base case + recursive calls on left/right
2. **Two-pointer**: Compare nodes in symmetric operations
3. **DFS with Path**: Track path from root to current node
4. **BFS with Queue**: Level-order processing
5. **Bottom-up**: Process children before parent (postorder)
6. **Top-down**: Process parent before children (preorder)

INTERVIEW TIPS:

1. **Always check for null**: Handle empty tree/node cases
2. **Understand tree properties**: BST vs general binary tree
3. **Choose right traversal**: Match traversal to problem requirements
4. **Consider iterative solutions**: For better space complexity
5. **Draw examples**: Visualize small trees to understand logic
6. **Think recursively**: Most tree problems have elegant recursive solutions

COMMON MISTAKES:

- Forgetting null checks
- Confusing left/right in traversals
- Not handling single-node trees
- Mixing up BST and general tree properties
- Incorrect base cases in recursion
"""

if __name__ == "__main__":
    test_tree_creation()
    test_traversals()
    test_tree_properties()
    test_bst_operations()
    create_sample_trees()
    
    print("=== BINARY TREES SUMMARY ===")
    print("Key Concepts: Nodes, traversals, BST properties")
    print("Common Operations: Insert, delete, search, traverse")
    print("Important: Always check for null nodes!")
    print("BST Advantage: O(log n) operations when balanced")
    print("Practice: Tree traversals and recursive thinking")