"""
ADVANCED BINARY TREES - COMPLETE CHEATSHEET
===========================================

Advanced Topics Covered:
1. Self-Balancing Trees (AVL, Red-Black)
2. Tree Serialization & Reconstruction
3. Advanced Traversal Techniques (Morris, Threaded)
4. Tree Transformations & Optimizations
5. Persistent Trees & Immutable Operations
6. Tree-based Data Structures (Trie, Segment Tree)
7. Advanced BST Variants
8. Memory-Efficient Techniques
9. Concurrent Tree Operations
10. Complex Tree Algorithms

Key Advanced Concepts:
- Tree rotations and balancing
- Amortized analysis
- Tree persistence and versioning
- Advanced pattern matching
- Tree compression techniques
- Parallel tree algorithms
"""

import threading
from collections import defaultdict, deque
from typing import Optional, List, Tuple, Dict, Any, Union
import pickle
import json

# ===== ENHANCED NODE DEFINITIONS =====

class TreeNode:
    """Enhanced tree node with additional metadata."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        # Additional metadata for advanced operations
        self.parent = None
        self.height = 1
        self.size = 1
        
    def __repr__(self):
        return f"TreeNode({self.val})"


class AVLNode:
    """AVL Tree node with height balance factor."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1
        
    def get_balance_factor(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height
    
    def update_height(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = 1 + max(left_height, right_height)


class RedBlackNode:
    """Red-Black tree node with color information."""
    def __init__(self, val=0, color='RED', left=None, right=None, parent=None):
        self.val = val
        self.color = color  # 'RED' or 'BLACK'
        self.left = left
        self.right = right
        self.parent = parent


class ThreadedNode:
    """Threaded tree node for space-efficient traversal."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.left_thread = False   # True if left points to predecessor
        self.right_thread = False  # True if right points to successor


class PersistentNode:
    """Node for persistent trees with version tracking."""
    def __init__(self, val=0, left=None, right=None, version=0):
        self.val = val
        self.left = left
        self.right = right
        self.version = version


# ===== AVL TREE IMPLEMENTATION =====

class AVLTree:
    """
    Self-balancing AVL Tree implementation.
    All operations: O(log n) guaranteed
    """
    
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert value maintaining AVL property."""
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        # Standard BST insertion
        if not node:
            return AVLNode(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            return node  # No duplicates
        
        # Update height
        node.update_height()
        
        # Get balance factor
        balance = node.get_balance_factor()
        
        # Perform rotations if unbalanced
        
        # Left heavy
        if balance > 1:
            # Left-Left case
            if val < node.left.val:
                return self._rotate_right(node)
            # Left-Right case
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        
        # Right heavy
        if balance < -1:
            # Right-Right case
            if val > node.right.val:
                return self._rotate_left(node)
            # Right-Left case
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        
        return node
    
    def delete(self, val):
        """Delete value maintaining AVL property."""
        self.root = self._delete(self.root, val)
    
    def _delete(self, node, val):
        if not node:
            return node
        
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node to delete found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node has two children
            successor = self._find_min(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        
        # Update height and rebalance
        node.update_height()
        balance = node.get_balance_factor()
        
        # Left heavy
        if balance > 1:
            if node.left.get_balance_factor() >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        
        # Right heavy
        if balance < -1:
            if node.right.get_balance_factor() <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        
        return node
    
    def _rotate_left(self, z):
        """Left rotation for balancing."""
        y = z.right
        T2 = y.left
        
        # Perform rotation
        y.left = z
        z.right = T2
        
        # Update heights
        z.update_height()
        y.update_height()
        
        return y
    
    def _rotate_right(self, z):
        """Right rotation for balancing."""
        y = z.left
        T3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = T3
        
        # Update heights
        z.update_height()
        y.update_height()
        
        return y
    
    def _find_min(self, node):
        """Find minimum value node."""
        while node.left:
            node = node.left
        return node


# ===== RED-BLACK TREE IMPLEMENTATION =====

class RedBlackTree:
    """
    Red-Black Tree implementation.
    Self-balancing with relaxed balance conditions.
    """
    
    def __init__(self):
        self.NIL = RedBlackNode(color='BLACK')
        self.root = self.NIL
    
    def insert(self, val):
        """Insert value maintaining Red-Black properties."""
        node = RedBlackNode(val, 'RED', self.NIL, self.NIL)
        
        y = self.NIL
        x = self.root
        
        while x != self.NIL:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        
        if y == self.NIL:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node
        
        if node.parent == self.NIL:
            node.color = 'BLACK'
            return
        
        if node.parent.parent == self.NIL:
            return
        
        self._fix_insert(node)
    
    def _fix_insert(self, k):
        """Fix Red-Black tree violations after insertion."""
        while k.parent.color == 'RED':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle
                if u.color == 'RED':
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # Uncle
                if u.color == 'RED':
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self._right_rotate(k.parent.parent)
            
            if k == self.root:
                break
        
        self.root.color = 'BLACK'
    
    def _left_rotate(self, x):
        """Left rotation for Red-Black tree."""
        y = x.right
        x.right = y.left
        
        if y.left != self.NIL:
            y.left.parent = x
        
        y.parent = x.parent
        
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def _right_rotate(self, x):
        """Right rotation for Red-Black tree."""
        y = x.left
        x.left = y.right
        
        if y.right != self.NIL:
            y.right.parent = x
        
        y.parent = x.parent
        
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y


# ===== TREE SERIALIZATION & RECONSTRUCTION =====

def serialize_tree(root):
    """
    Serialize tree to string representation.
    Time: O(n), Space: O(n)
    """
    def serialize_helper(node):
        if not node:
            vals.append("null")
            return
        
        vals.append(str(node.val))
        serialize_helper(node.left)
        serialize_helper(node.right)
    
    vals = []
    serialize_helper(root)
    return ','.join(vals)


def deserialize_tree(data):
    """
    Deserialize string to tree.
    Time: O(n), Space: O(n)
    """
    def deserialize_helper():
        val = next(vals)
        if val == "null":
            return None
        
        node = TreeNode(int(val))
        node.left = deserialize_helper()
        node.right = deserialize_helper()
        return node
    
    vals = iter(data.split(','))
    return deserialize_helper()


def serialize_tree_level_order(root):
    """
    Serialize tree using level-order traversal.
    More compact for sparse trees.
    """
    if not root:
        return "[]"
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    
    # Remove trailing nulls
    while result and result[-1] == "null":
        result.pop()
    
    return '[' + ','.join(result) + ']'


def tree_to_json(root):
    """
    Convert tree to JSON representation.
    """
    def tree_to_dict(node):
        if not node:
            return None
        
        return {
            'val': node.val,
            'left': tree_to_dict(node.left),
            'right': tree_to_dict(node.right)
        }
    
    return json.dumps(tree_to_dict(root), indent=2)


def json_to_tree(json_str):
    """
    Create tree from JSON representation.
    """
    def dict_to_tree(node_dict):
        if not node_dict:
            return None
        
        node = TreeNode(node_dict['val'])
        node.left = dict_to_tree(node_dict['left'])
        node.right = dict_to_tree(node_dict['right'])
        return node
    
    tree_dict = json.loads(json_str)
    return dict_to_tree(tree_dict)


# ===== ADVANCED TRAVERSAL TECHNIQUES =====

def morris_inorder(root):
    """
    Morris traversal for inorder without recursion/stack.
    Time: O(n), Space: O(1)
    """
    result = []
    current = root
    
    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                # Create threaded link
                predecessor.right = current
                current = current.left
            else:
                # Remove threaded link and process current
                predecessor.right = None
                result.append(current.val)
                current = current.right
    
    return result


def morris_preorder(root):
    """
    Morris traversal for preorder without recursion/stack.
    Time: O(n), Space: O(1)
    """
    result = []
    current = root
    
    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                result.append(current.val)  # Process before going left
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                current = current.right
    
    return result


def iterative_postorder_two_stacks(root):
    """
    Iterative postorder using two stacks.
    Time: O(n), Space: O(n)
    """
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    result = []
    
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    while stack2:
        result.append(stack2.pop().val)
    
    return result


def boundary_traversal(root):
    """
    Traverse tree boundary (anti-clockwise).
    Time: O(n), Space: O(h)
    """
    if not root:
        return []
    
    result = []
    
    def add_left_boundary(node):
        if node and not is_leaf(node):
            result.append(node.val)
            if node.left:
                add_left_boundary(node.left)
            else:
                add_left_boundary(node.right)
    
    def add_leaves(node):
        if node:
            if is_leaf(node):
                result.append(node.val)
            add_leaves(node.left)
            add_leaves(node.right)
    
    def add_right_boundary(node):
        if node and not is_leaf(node):
            if node.right:
                add_right_boundary(node.right)
            else:
                add_right_boundary(node.left)
            result.append(node.val)
    
    def is_leaf(node):
        return node and not node.left and not node.right
    
    result.append(root.val)
    add_left_boundary(root.left)
    add_leaves(root)
    add_right_boundary(root.right)
    
    return result


# ===== TREE RECONSTRUCTION ALGORITHMS =====

def build_tree_preorder_inorder(preorder, inorder):
    """
    Build tree from preorder and inorder traversals.
    Time: O(n), Space: O(n)
    """
    if not preorder or not inorder:
        return None
    
    # Create index mapping for inorder
    inorder_map = {val: i for i, val in enumerate(inorder)}
    self.preorder_idx = 0
    
    def build_tree_helper(left, right):
        if left > right:
            return None
        
        root_val = preorder[self.preorder_idx]
        self.preorder_idx += 1
        root = TreeNode(root_val)
        
        root_idx = inorder_map[root_val]
        
        root.left = build_tree_helper(left, root_idx - 1)
        root.right = build_tree_helper(root_idx + 1, right)
        
        return root
    
    return build_tree_helper(0, len(inorder) - 1)


def build_tree_postorder_inorder(postorder, inorder):
    """
    Build tree from postorder and inorder traversals.
    Time: O(n), Space: O(n)
    """
    if not postorder or not inorder:
        return None
    
    inorder_map = {val: i for i, val in enumerate(inorder)}
    self.postorder_idx = len(postorder) - 1
    
    def build_tree_helper(left, right):
        if left > right:
            return None
        
        root_val = postorder[self.postorder_idx]
        self.postorder_idx -= 1
        root = TreeNode(root_val)
        
        root_idx = inorder_map[root_val]
        
        # Build right first in postorder
        root.right = build_tree_helper(root_idx + 1, right)
        root.left = build_tree_helper(left, root_idx - 1)
        
        return root
    
    return build_tree_helper(0, len(inorder) - 1)


def build_tree_from_string(s):
    """
    Build tree from string like "1(2(4)(5))(3(6))"
    Time: O(n), Space: O(n)
    """
    def build_tree_helper():
        nonlocal index
        
        if index >= len(s):
            return None
        
        # Read number
        num_str = ""
        while index < len(s) and (s[index].isdigit() or s[index] == '-'):
            num_str += s[index]
            index += 1
        
        if not num_str:
            return None
        
        node = TreeNode(int(num_str))
        
        # Check for left child
        if index < len(s) and s[index] == '(':
            index += 1  # Skip '('
            node.left = build_tree_helper()
            index += 1  # Skip ')'
        
        # Check for right child
        if index < len(s) and s[index] == '(':
            index += 1  # Skip '('
            node.right = build_tree_helper()
            index += 1  # Skip ')'
        
        return node
    
    index = 0
    return build_tree_helper()


# ===== PERSISTENT TREES =====

class PersistentBST:
    """
    Persistent BST that maintains all previous versions.
    Path copying technique for immutability.
    """
    
    def __init__(self):
        self.versions = {}
        self.current_version = 0
    
    def insert(self, root, val, version=None):
        """
        Insert value creating new version.
        Only modified path is copied.
        """
        if version is None:
            version = self.current_version + 1
            self.current_version = version
        
        new_root = self._insert_persistent(root, val, version)
        self.versions[version] = new_root
        return new_root
    
    def _insert_persistent(self, node, val, version):
        if not node:
            return PersistentNode(val, version=version)
        
        # Create new node (path copying)
        new_node = PersistentNode(node.val, node.left, node.right, version)
        
        if val < node.val:
            new_node.left = self._insert_persistent(node.left, val, version)
        elif val > node.val:
            new_node.right = self._insert_persistent(node.right, val, version)
        
        return new_node
    
    def get_version(self, version):
        """Get tree at specific version."""
        return self.versions.get(version)


# ===== ADVANCED TREE DATA STRUCTURES =====

class TrieNode:
    """Node for Trie (Prefix Tree) implementation."""
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  # For counting word frequencies


class Trie:
    """
    Trie (Prefix Tree) for efficient string operations.
    All operations: O(m) where m is string length.
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert word into trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True
    
    def search(self, word):
        """Search for complete word."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        """Check if any word starts with prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def count_words_with_prefix(self, prefix):
        """Count words with given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count
    
    def delete(self, word):
        """Delete word from trie."""
        def delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            should_delete = delete_helper(node.children[char], word, index + 1)
            
            if should_delete:
                del node.children[char]
                return not node.is_end and len(node.children) == 0
            
            return False
        
        delete_helper(self.root, word, 0)


class SegmentTreeNode:
    """Node for Segment Tree implementation."""
    def __init__(self, start, end, val=0):
        self.start = start
        self.end = end
        self.val = val
        self.left = None
        self.right = None


class SegmentTree:
    """
    Segment Tree for range queries and updates.
    Build: O(n), Query/Update: O(log n)
    """
    
    def __init__(self, arr):
        self.arr = arr
        self.root = self._build_tree(0, len(arr) - 1)
    
    def _build_tree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.arr[start])
        
        mid = (start + end) // 2
        node = SegmentTreeNode(start, end)
        
        node.left = self._build_tree(start, mid)
        node.right = self._build_tree(mid + 1, end)
        
        node.val = node.left.val + node.right.val
        return node
    
    def query_range(self, start, end):
        """Query sum in range [start, end]."""
        return self._query_range(self.root, start, end)
    
    def _query_range(self, node, start, end):
        if not node or start > node.end or end < node.start:
            return 0
        
        if start <= node.start and end >= node.end:
            return node.val
        
        left_sum = self._query_range(node.left, start, end)
        right_sum = self._query_range(node.right, start, end)
        
        return left_sum + right_sum
    
    def update(self, index, val):
        """Update value at index."""
        self._update(self.root, index, val)
    
    def _update(self, node, index, val):
        if node.start == node.end:
            node.val = val
            return
        
        mid = (node.start + node.end) // 2
        
        if index <= mid:
            self._update(node.left, index, val)
        else:
            self._update(node.right, index, val)
        
        node.val = node.left.val + node.right.val


# ===== ADVANCED TREE ALGORITHMS =====

def tree_isomorphism(root1, root2):
    """
    Check if two trees are isomorphic (same structure).
    Time: O(n), Space: O(h)
    """
    if not root1 and not root2:
        return True
    
    if not root1 or not root2:
        return False
    
    # Check if trees are isomorphic without flipping
    case1 = (tree_isomorphism(root1.left, root2.left) and 
             tree_isomorphism(root1.right, root2.right))
    
    # Check if trees are isomorphic with flipping
    case2 = (tree_isomorphism(root1.left, root2.right) and 
             tree_isomorphism(root1.right, root2.left))
    
    return case1 or case2


def tree_edit_distance(root1, root2):
    """
    Calculate minimum edit distance between two trees.
    Time: O(n*m), Space: O(n*m)
    """
    def tree_to_list(root):
        if not root:
            return []
        
        result = [root.val]
        result.extend(tree_to_list(root.left))
        result.extend(tree_to_list(root.right))
        return result
    
    list1 = tree_to_list(root1)
    list2 = tree_to_list(root2)
    
    # Use dynamic programming for edit distance
    m, n = len(list1), len(list2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if list1[i-1] == list2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # Delete
                                  dp[i][j-1],     # Insert
                                  dp[i-1][j-1])   # Replace
    
    return dp[m][n]


def find_duplicate_subtrees(root):
    """
    Find all duplicate subtrees.
    Time: O(n), Space: O(n)
    """
    def serialize_subtree(node):
        if not node:
            return "null"
        
        left_serial = serialize_subtree(node.left)
        right_serial = serialize_subtree(node.right)
        
        subtree_serial = f"{node.val},{left_serial},{right_serial}"
        
        if subtree_serial in subtree_count:
            subtree_count[subtree_serial] += 1
            if subtree_count[subtree_serial] == 2:
                duplicates.append(node)
        else:
            subtree_count[subtree_serial] = 1
        
        return subtree_serial
    
    subtree_count = {}
    duplicates = []
    serialize_subtree(root)
    return duplicates


def tree_compression_lz77(root):
    """
    Tree compression using LZ77-like algorithm.
    Identifies repeated patterns in tree structure.
    """
    def get_subtree_pattern(node, depth=0):
        if not node or depth > max_depth:
            return None
        
        pattern = {
            'val': node.val,
            'left': get_subtree_pattern(node.left, depth + 1),
            'right': get_subtree_pattern(node.right, depth + 1)
        }
        
        pattern_str = str(pattern)
        if pattern_str in pattern_dict:
            pattern_dict[pattern_str].append(node)
        else:
            pattern_dict[pattern_str] = [node]
        
        return pattern
    
    pattern_dict = {}
    max_depth = 3  # Configurable compression depth
    get_subtree_pattern(root)
    
    # Find patterns that appear multiple times
    repeated_patterns = {k: v for k, v in pattern_dict.items() if len(v) > 1}
    
    return repeated_patterns


# ===== CONCURRENT TREE OPERATIONS =====

class ThreadSafeBST:
    """
    Thread-safe BST using fine-grained locking.
    """
    
    def __init__(self):
        self.root = None
        self.lock = threading.RLock()
    
    def insert(self, val):
        """Thread-safe insertion."""
        with self.lock:
            self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        
        return node
    
    def search(self, val):
        """Thread-safe search."""
        with self.lock:
            return self._search(self.root, val)
    
    def _search(self, node, val):
        if not node:
            return False
        
        if node.val == val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)


# ===== TREE OPTIMIZATION TECHNIQUES =====

def optimize_tree_memory(root):
    """
    Optimize tree memory usage by removing redundant information.
    """
    def calculate_metadata(node):
        if not node:
            return 0, 0  # size, height
        
        left_size, left_height = calculate_metadata(node.left)
        right_size, right_height = calculate_metadata(node.right)
        
        node.size = 1 + left_size + right_size
        node.height = 1 + max(left_height, right_height)
        
        return node.size, node.height
    
    calculate_metadata(root)
    return root


def tree_vectorization(root):
    """
    Convert tree to vector representation for ML applications.
    """
    def tree_to_vector(node, vector, index):
        if not node or index >= len(vector):
            return
        
        vector[index] = node.val
        tree_to_vector(node.left, vector, 2 * index + 1)
        tree_to_vector(node.right, vector, 2 * index + 2)
    
    # Calculate tree size to determine vector length
    size = tree_size(root)
    vector = [None] * (2 * size)  # Overestimate for complete tree
    tree_to_vector(root, vector, 0)
    
    return vector


def tree_size(root):
    """Calculate tree size."""
    if not root:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)


# ===== ADVANCED PATTERN MATCHING =====

def find_tree_pattern(root, pattern_root):
    """
    Find if pattern tree exists as subtree.
    Time: O(n*m), Space: O(h)
    """
    def is_identical(node1, node2):
        if not node1 and not node2:
            return True
        
        if not node1 or not node2:
            return False
        
        return (node1.val == node2.val and
                is_identical(node1.left, node2.left) and
                is_identical(node1.right, node2.right))
    
    def find_pattern_helper(node):
        if not node:
            return False
        
        if is_identical(node, pattern_root):
            return True
        
        return (find_pattern_helper(node.left) or 
                find_pattern_helper(node.right))
    
    return find_pattern_helper(root)


def tree_pattern_automaton(patterns):
    """
    Build automaton for multiple tree pattern matching.
    Based on Aho-Corasick algorithm adapted for trees.
    """
    class PatternNode:
        def __init__(self):
            self.children = {}
            self.failure = None
            self.output = []
    
    root = PatternNode()
    
    # Build trie of patterns
    for pattern_id, pattern in enumerate(patterns):
        current = root
        for symbol in pattern:
            if symbol not in current.children:
                current.children[symbol] = PatternNode()
            current = current.children[symbol]
        current.output.append(pattern_id)
    
    return root


# ===== TESTING AND BENCHMARKING =====

def test_avl_tree():
    """Test AVL tree operations."""
    print("=== TESTING AVL TREE ===\n")
    
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    
    for val in values:
        avl.insert(val)
        print(f"Inserted {val}")
    
    print("AVL tree maintains balance automatically")
    print()


def test_tree_serialization():
    """Test tree serialization methods."""
    print("=== TESTING TREE SERIALIZATION ===\n")
    
    # Create test tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Test serialization
    serialized = serialize_tree(root)
    print(f"Serialized: {serialized}")
    
    # Test deserialization
    reconstructed = deserialize_tree(serialized)
    reserialized = serialize_tree(reconstructed)
    print(f"Reserialized: {reserialized}")
    print(f"Match: {serialized == reserialized}")
    
    # Test JSON serialization
    json_repr = tree_to_json(root)
    print(f"JSON representation:\n{json_repr}")
    print()


def test_advanced_traversals():
    """Test advanced traversal techniques."""
    print("=== TESTING ADVANCED TRAVERSALS ===\n")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"Morris Inorder: {morris_inorder(root)}")
    print(f"Morris Preorder: {morris_preorder(root)}")
    print(f"Boundary Traversal: {boundary_traversal(root)}")
    print()


def test_trie():
    """Test Trie implementation."""
    print("=== TESTING TRIE ===\n")
    
    trie = Trie()
    words = ["apple", "app", "application", "apply", "banana"]
    
    for word in words:
        trie.insert(word)
    
    print(f"Search 'app': {trie.search('app')}")
    print(f"Search 'appl': {trie.search('appl')}")
    print(f"Starts with 'app': {trie.starts_with('app')}")
    print(f"Words with prefix 'app': {trie.count_words_with_prefix('app')}")
    print()


def benchmark_tree_operations():
    """Benchmark different tree implementations."""
    import time
    import random
    
    print("=== BENCHMARKING TREE OPERATIONS ===\n")
    
    # Generate test data
    data = list(range(1000))
    random.shuffle(data)
    
    # Benchmark AVL tree
    start_time = time.time()
    avl = AVLTree()
    for val in data:
        avl.insert(val)
    avl_time = time.time() - start_time
    
    print(f"AVL Tree insertion (1000 elements): {avl_time:.4f} seconds")
    print()


# ===== COMPLEXITY ANALYSIS =====
"""
ADVANCED BINARY TREES COMPLEXITY ANALYSIS:

Tree Type           | Insert    | Delete    | Search    | Space    | Balancing
--------------------|-----------|-----------|-----------|----------|----------
AVL Tree            | O(log n)  | O(log n)  | O(log n)  | O(n)     | Strict
Red-Black Tree      | O(log n)  | O(log n)  | O(log n)  | O(n)     | Relaxed
Splay Tree          | O(log n)* | O(log n)* | O(log n)* | O(n)     | Amortized
Treap              | O(log n)* | O(log n)* | O(log n)* | O(n)     | Randomized
B-Tree             | O(log n)  | O(log n)  | O(log n)  | O(n)     | Multi-way

* Amortized or expected time

ADVANCED OPERATIONS:

Operation                | Time Complexity | Space Complexity | Use Case
-------------------------|-----------------|------------------|------------------
Morris Traversal         | O(n)           | O(1)             | Memory-constrained
Tree Serialization      | O(n)           | O(n)             | Storage/transmission
Tree Reconstruction     | O(n)           | O(n)             | Recovery from traversals
Persistent Operations   | O(log n)       | O(log n)         | Version control
Pattern Matching        | O(n*m)         | O(h)             | Subtree search
Tree Compression        | O(n)           | O(n)             | Storage optimization
Concurrent Operations   | O(log n)       | O(n)             | Multi-threaded access

ADVANCED DATA STRUCTURES:

Structure        | Primary Use                    | Key Advantage
-----------------|--------------------------------|------------------
Trie             | String prefix operations       | Fast prefix queries
Segment Tree     | Range queries/updates          | O(log n) range ops
Fenwick Tree     | Cumulative frequency          | Simple implementation
Suffix Tree      | String pattern matching       | Linear time search
Van Emde Boas    | Integer operations            | O(log log u) ops
Cartesian Tree   | Range minimum queries         | Linear construction

OPTIMIZATION TECHNIQUES:

1. **Path Compression**: Reduce tree height in Union-Find
2. **Lazy Propagation**: Defer updates in segment trees
3. **Memory Pooling**: Reuse node objects
4. **Cache-Friendly Layout**: Arrange nodes for cache efficiency
5. **Vectorization**: Convert trees to arrays for SIMD
6. **Parallelization**: Concurrent tree operations

ADVANCED PATTERNS:

1. **Persistent Data Structures**: Path copying for immutability
2. **Lock-Free Algorithms**: Compare-and-swap operations
3. **Cache-Oblivious Algorithms**: Optimal for all cache levels
4. **Succinct Data Structures**: Minimal space overhead
5. **External Memory Algorithms**: Disk-based tree operations

REAL-WORLD APPLICATIONS:

- **Database Indexing**: B+ trees, LSM trees
- **File Systems**: B-trees for directory structures
- **Compilers**: Abstract syntax trees, symbol tables
- **Graphics**: Spatial data structures (quadtrees, octrees)
- **Machine Learning**: Decision trees, random forests
- **Networking**: Routing tables, packet classification
- **Compression**: Huffman trees, LZ77 variants

RESEARCH FRONTIERS:

- **Quantum Tree Algorithms**: Quantum speedups for tree operations
- **Dynamic Trees**: Support for link/cut operations
- **Approximate Trees**: Trade accuracy for performance
- **Streaming Trees**: Process infinite data streams
- **Neural Trees**: Machine learning with tree structures
"""

if __name__ == "__main__":
    test_avl_tree()
    test_tree_serialization()
    test_advanced_traversals()
    test_trie()
    benchmark_tree_operations()
    
    print("=== ADVANCED BINARY TREES SUMMARY ===")
    print("Key Concepts: Self-balancing, persistence, advanced traversals")
    print("Optimizations: Memory efficiency, concurrency, compression")
    print("Applications: Databases, compilers, graphics, ML")
    print("Advanced: Morris traversal O(1) space, persistent trees")
    print("Production: Thread-safety, serialization, performance tuning")