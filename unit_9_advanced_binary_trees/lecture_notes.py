How does the structure of a BST make searching efficient?
It allows searching only the left subtree for all values.
It ensures that nodes are added in a balanced manner.
It allows you to decide whether to go left or right based on the value you're searching for, reducing the number of nodes to check.
It keeps all nodes at the same depth, making the search process uniform.



Given the root of a binary tree and an integer target_sum, return True if the tree has a root-to-leaf path such that adding up all the values along the path equals target_sum. A leaf is a node with no children.