class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

# Problem 1: Build a Binary Tree I (Example Tree)
def build_example_tree():
    return TreeNode(4,
        TreeNode(2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(5)
    )

# Problem 2: 3-Node Sum I (exactly 3 nodes)
def check_tree(root):
    if root and root.left and root.right:
        return root.val == root.left.val + root.right.val
    return False

# Problem 3: 3-Node Sum II (at most 3 nodes)
def check_tree1(root):
    if root is None:
        return False
    total = 0
    if root.left:
        total += root.left.val
    if root.right:
        total += root.right.val
    return root.val == total

# Problem 4: Find Leftmost Node I (recursive)
def left_most(root):
    if not root:
        return None
    if not root.left:
        return root.val
    return left_most(root.left)

# Problem 5: Find Leftmost Node II (iterative)
def left_most_iterative(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.val

# Problem 6: In-order Traversal
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Problem 7: Binary Tree Size
def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

# Problem 8: Binary Tree Find
def find(root, value):
    if not root:
        return False
    if root.val == value:
        return True
    return find(root.left, value) or find(root.right, value)

# Problem 9: Binary Search Tree Find
def find_bst(root, value):
    if not root:
        return False
    if root.val == value:
        return True
    elif value < root.val:
        return find_bst(root.left, value)
    else:
        return find_bst(root.right, value)

# Problem 10: BST Descending Leaves
def descending_leaves(root):
    if not root:
        return []

    leaves = []
    
    def dfs(node):
        if not node:
            return
        if not node.left and not node.right:
            leaves.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return sorted(leaves, reverse=True)


# Example usage
if __name__ == "__main__":
    tree = build_example_tree()
    print("check_tree:", check_tree(tree))
    print("check_tree1:", check_tree1(tree))
    print("left_most (recursive):", left_most(tree))
    print("left_most (iterative):", left_most_iterative(tree))
    print("inorder_traversal:", inorder_traversal(tree))
    print("size:", size(tree))
    print("find 5:", find(tree, 5))
    print("find 10:", find(tree, 10))
    print("find_bst 5:", find_bst(tree, 5))
    print("find_bst 10:", find_bst(tree, 10))
    print("descending_leaves:", descending_leaves(tree))
