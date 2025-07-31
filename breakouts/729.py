class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#! Problem 1: Is symmetric Tree
"""
if we reach end of tree
    return true 

we check if both 

"""
def check_halves(left_side, right_side):
    if root.left is None and root.right is None:
        return True
    
    if left_side.val != right_side.val:
        return False
    
    return check_halves(left_side.left,left_side.right)
    return check_halves(right_side.left,right_side.right)

def is_symmetric(root):
    
    return check_halves(root.left,root.right)





#Problem 2

def binary_tree_paths (root):
    lst = []
    if root:
        binary_tree_paths_helper(root, "", lst)
    return lst


# Preorder
def binary_tree_paths_helper(root, str_path, lst):
    # Check if the root has any children
    if root.right or root.left:
        # Take care of the root, add root to the string to be put in the final list
        str_path = str_path + str(root.val)

        # Take care of left, add
        # if theres a left child
        if root.left:
            # call the function with the new string
            binary_tree_paths_helper(root.left, str_path + "->", lst)


        # Take care of right
        if root.right:
            # call the function with the new string
            binary_tree_paths_helper(root.right, str_path + "->", lst)
        return lst.append(str_path + str(root.val))
        
    # Handle leaf node case
    return lst.append(str_path + str(root.val))

test_tree1 = TreeNode(4)
test_tree2 = TreeNode(4, TreeNode(5), TreeNode(6))
test_tree3 = None

# print(binary_tree_paths(test_tree1))
print(binary_tree_paths(test_tree2))
# print(binary_tree_paths(test_tree4))


#Problem 3
# preorder
def min_diff_in_bst_helper(root, min_val):
    
    # Taking care of initial root
        #left root value - root value

        
    
        min_diff_in_bst(root.left, min_val)
        min_val = min(min_val,root.val )
        min_diff_in_bst(root.right, min_val)



def increasing_bst(root):
	pass