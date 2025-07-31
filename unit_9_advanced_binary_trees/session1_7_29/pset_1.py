class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Problem 1: Is Symmetric Tree
def is_symmetric(root):
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))
    return is_mirror(root, root)

# Problem 2: Root-to-Leaf Paths
def binary_tree_paths(root):
    paths = []

    def dfs(node, path):
        if not node:
            return
        path += str(node.val)
        if not node.left and not node.right:
            paths.append(path)
        else:
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)

    dfs(root, "")
    return paths

# Problem 3: Minimum Difference in BST
def min_diff_in_bst(root):
    prev = [None]
    min_diff = [float('inf')]

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        if prev[0] is not None:
            min_diff[0] = min(min_diff[0], node.val - prev[0])
        prev[0] = node.val
        inorder(node.right)

    inorder(root)
    return min_diff[0]

# Problem 4: Increasing Order Search Tree
def increasing_bst(root):
    dummy = TreeNode()
    curr = dummy

    def inorder(node):
        nonlocal curr
        if not node:
            return
        inorder(node.left)
        curr.right = TreeNode(node.val)
        curr = curr.right
        inorder(node.right)

    inorder(root)
    return dummy.right

# Problem 5: Equal Tree Split
def can_split(root):
    total = [0]

    def get_total(node):
        if not node:
            return 0
        left = get_total(node.left)
        right = get_total(node.right)
        total[0] += node.val
        return node.val + left + right

    get_total(root)

    found = [False]

    def dfs(node):
        if not node or found[0]:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        subtotal = node.val + left + right
        if subtotal * 2 == total[0]:
            found[0] = True
        return subtotal

    dfs(root)
    return found[0]


# Example usage
if __name__ == "__main__":
    # Example symmetric tree
    symmetric_tree = TreeNode(1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(2, TreeNode(4), TreeNode(3))
    )
    print("Is Symmetric:", is_symmetric(symmetric_tree))  # True

    # Tree for binary paths and min diff
    tree = TreeNode(1,
        TreeNode(2, TreeNode(5)),
        TreeNode(3)
    )
    print("Root-to-Leaf Paths:", binary_tree_paths(tree))  # ["1->2->5", "1->3"]

    bst = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    print("Min Diff in BST:", min_diff_in_bst(bst))  # Expected: 1

    new_tree = increasing_bst(bst)
    print("Increasing Order BST:")
    curr = new_tree
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.right
    print("None")

    split_tree = TreeNode(5,
        TreeNode(10),
        TreeNode(10, TreeNode(2), TreeNode(3))
    )
    print("Can Split:", can_split(split_tree))  # True

