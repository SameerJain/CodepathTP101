class TreeNode:
    def __init__(self, key, val=None, left=None, right=None):
        self.key = key
        self.val = val if val is not None else key
        self.left = left
        self.right = right

# Problem 1: Is Uni-valued
def is_univalued(root):
    if not root:
        return True
    if root.left and root.left.val != root.val:
        return False
    if root.right and root.right.val != root.val:
        return False
    return is_univalued(root.left) and is_univalued(root.right)

# Problem 2: Binary Tree Height
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# Problem 3: BST Insert
def insert(root, key, value):
    if root is None:
        return TreeNode(key, value)
    if key < root.key:
        root.left = insert(root.left, key, value)
    elif key > root.key:
        root.right = insert(root.right, key, value)
    else:
        root.val = value  # update existing
    return root

# Problem 4: BST Remove
def remove_bst(root, key):
    if not root:
        return None

    if key < root.key:
        root.left = remove_bst(root.left, key)
    elif key > root.key:
        root.right = remove_bst(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # Find inorder successor
            succ = root.right
            while succ.left:
                succ = succ.left
            # Replace value and key
            root.key, root.val = succ.key, succ.val
            # Remove successor
            root.right = remove_bst(root.right, succ.key)
    return root

# Problem 5: BST In-order Successor
def inorder_successor(root, current):
    successor = None
    while root:
        if current.key < root.key:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor

# Problem 6: Merge Binary Trees
def merge_trees(root1, root2):
    if not root1 and not root2:
        return None
    if not root1:
        return root2
    if not root2:
        return root1
    merged = TreeNode(root1.key, root1.val + root2.val)
    merged.left = merge_trees(root1.left, root2.left)
    merged.right = merge_trees(root1.right, root2.right)
    return merged


# Example usage
if __name__ == "__main__":
    # Sample tree for testing
    root = TreeNode(10, "Root",
        TreeNode(5, "Left",
            TreeNode(1, "Left.Left"),
            TreeNode(6, "Left.Right")),
        TreeNode(15, "Right",
            TreeNode(13, "Right.Left"),
            TreeNode(16, "Right.Right"))
    )

    print("Is Univalued:", is_univalued(root))  # False
    print("Tree Height:", height(root))  # 3

    root = insert(root, 9, "Inserted Node")
    print("After Insert (9):", inorder_successor(root, TreeNode(6)).key)  # Successor of 6 is 9

    root = remove_bst(root, 10)
    print("After Remove (10):", root.key)  # Root should be replaced

    successor = inorder_successor(root, TreeNode(5))
    print("Inorder Successor of 5:", successor.key if successor else None)

    # Merge example trees
    t1 = TreeNode(1, 1, TreeNode(3, 3, TreeNode(5, 5)), TreeNode(2, 2))
    t2 = TreeNode(2, 2, TreeNode(1, 1, None, TreeNode(4, 4)), TreeNode(3, 3, None, TreeNode(7, 7)))
    merged = merge_trees(t1, t2)
    print("Merged Root Value:", merged.val)  # Should be 3
