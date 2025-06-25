"""
LINKED LISTS BASICS - COMPLETE CHEATSHEET
==========================================

What are Linked Lists?
- Linear data structure where elements (nodes) are stored in sequence
- Each node contains data and reference(s) to next node(s)
- Dynamic size, elements not stored contiguously in memory

Types:
1. Singly Linked List - each node points to next
2. Doubly Linked List - each node has prev and next pointers
3. Circular Linked List - last node points back to first

When to Use:
- Frequent insertions/deletions at beginning
- Size varies significantly
- Don't need random access by index
- Implementing stacks, queues, graphs

Advantages:
- Dynamic size
- Efficient insertion/deletion at beginning O(1)
- Memory efficient (allocate as needed)

Disadvantages:
- No random access O(n) to find element
- Extra memory for pointers
- Poor cache locality
- Can't use binary search directly
"""

# ===== NODE DEFINITIONS =====

class ListNode:
    """Standard singly linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"


class DoublyListNode:
    """Doubly linked list node with prev and next pointers."""
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return f"DoublyListNode({self.val})"


# ===== BASIC OPERATIONS =====

def create_linked_list(arr):
    """Create linked list from array."""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head


def print_linked_list(head):
    """Print linked list in readable format."""
    result = []
    current = head
    
    while current:
        result.append(str(current.val))
        current = current.next
    
    return " -> ".join(result) + " -> None"


def get_length(head):
    """Get length of linked list."""
    length = 0
    current = head
    
    while current:
        length += 1
        current = current.next
    
    return length


def get_node_at_index(head, index):
    """Get node at specific index (0-based)."""
    current = head
    
    for i in range(index):
        if not current:
            return None
        current = current.next
    
    return current


# ===== INSERTION OPERATIONS =====

def insert_at_beginning(head, val):
    """Insert node at beginning. Time: O(1), Space: O(1)"""
    new_node = ListNode(val)
    new_node.next = head
    return new_node


def insert_at_end(head, val):
    """Insert node at end. Time: O(n), Space: O(1)"""
    new_node = ListNode(val)
    
    if not head:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    return head


def insert_at_index(head, index, val):
    """Insert node at specific index. Time: O(n), Space: O(1)"""
    if index == 0:
        return insert_at_beginning(head, val)
    
    new_node = ListNode(val)
    current = head
    
    # Go to node before insertion point
    for i in range(index - 1):
        if not current:
            return head  # Index out of bounds
        current = current.next
    
    if current:  # Valid position
        new_node.next = current.next
        current.next = new_node
    
    return head


def insert_after_node(node, val):
    """Insert node after given node. Time: O(1), Space: O(1)"""
    if not node:
        return
    
    new_node = ListNode(val)
    new_node.next = node.next
    node.next = new_node


# ===== DELETION OPERATIONS =====

def delete_at_beginning(head):
    """Delete first node. Time: O(1), Space: O(1)"""
    if not head:
        return None
    
    return head.next


def delete_at_end(head):
    """Delete last node. Time: O(n), Space: O(1)"""
    if not head:
        return None
    
    if not head.next:  # Only one node
        return None
    
    current = head
    while current.next.next:  # Stop at second to last
        current = current.next
    
    current.next = None
    return head


def delete_at_index(head, index):
    """Delete node at specific index. Time: O(n), Space: O(1)"""
    if not head or index < 0:
        return head
    
    if index == 0:
        return head.next
    
    current = head
    
    # Go to node before deletion point
    for i in range(index - 1):
        if not current or not current.next:
            return head  # Index out of bounds
        current = current.next
    
    if current.next:
        current.next = current.next.next
    
    return head


def delete_node_with_value(head, val):
    """Delete first node with given value. Time: O(n), Space: O(1)"""
    if not head:
        return None
    
    if head.val == val:
        return head.next
    
    current = head
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
            break
        current = current.next
    
    return head


def delete_node_direct(node):
    """Delete node when only given the node (not head). Time: O(1), Space: O(1)"""
    if not node or not node.next:
        return  # Can't delete last node this way
    
    # Copy next node's data to current node
    node.val = node.next.val
    node.next = node.next.next


# ===== SEARCHING AND TRAVERSAL =====

def search(head, val):
    """Search for value in linked list. Time: O(n), Space: O(1)"""
    current = head
    index = 0
    
    while current:
        if current.val == val:
            return index
        current = current.next
        index += 1
    
    return -1  # Not found


def get_middle(head):
    """Get middle node using slow/fast pointers. Time: O(n), Space: O(1)"""
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def get_nth_from_end(head, n):
    """Get nth node from end. Time: O(n), Space: O(1)"""
    if not head or n <= 0:
        return None
    
    # Move first pointer n steps ahead
    first = head
    for i in range(n):
        if not first:
            return None  # n is larger than list length
        first = first.next
    
    # Move both pointers until first reaches end
    second = head
    while first:
        first = first.next
        second = second.next
    
    return second


# ===== REVERSAL OPERATIONS =====

def reverse_iterative(head):
    """Reverse linked list iteratively. Time: O(n), Space: O(1)"""
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Store next
        current.next = prev       # Reverse link
        prev = current           # Move prev forward
        current = next_temp      # Move current forward
    
    return prev  # prev is new head


def reverse_recursive(head):
    """Reverse linked list recursively. Time: O(n), Space: O(n)"""
    if not head or not head.next:
        return head
    
    # Recursively reverse rest of list
    new_head = reverse_recursive(head.next)
    
    # Reverse current connection
    head.next.next = head
    head.next = None
    
    return new_head


def reverse_between(head, left, right):
    """Reverse nodes between positions left and right. Time: O(n), Space: O(1)"""
    if not head or left == right:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move to position before left
    for i in range(left - 1):
        prev = prev.next
    
    # Reverse the sublist
    current = prev.next
    for i in range(right - left):
        next_temp = current.next
        current.next = next_temp.next
        next_temp.next = prev.next
        prev.next = next_temp
    
    return dummy.next


# ===== CYCLE DETECTION =====

def has_cycle(head):
    """Detect if linked list has cycle using Floyd's algorithm. Time: O(n), Space: O(1)"""
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def find_cycle_start(head):
    """Find start of cycle in linked list. Time: O(n), Space: O(1)"""
    if not head or not head.next:
        return None
    
    # Phase 1: Detect cycle
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow


def cycle_length(head):
    """Find length of cycle if it exists. Time: O(n), Space: O(1)"""
    if not head or not head.next:
        return 0
    
    slow = fast = head
    
    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return 0  # No cycle
    
    # Count cycle length
    length = 1
    current = slow.next
    while current != slow:
        current = current.next
        length += 1
    
    return length


# ===== MERGING OPERATIONS =====

def merge_two_sorted(l1, l2):
    """Merge two sorted linked lists. Time: O(m+n), Space: O(1)"""
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Append remaining nodes
    current.next = l1 or l2
    
    return dummy.next


def merge_k_sorted(lists):
    """Merge k sorted linked lists using divide and conquer. Time: O(n log k), Space: O(log k)"""
    if not lists:
        return None
    
    while len(lists) > 1:
        merged_lists = []
        
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(merge_two_sorted(l1, l2))
        
        lists = merged_lists
    
    return lists[0]


# ===== INTERSECTION AND COMPARISON =====

def get_intersection(headA, headB):
    """Find intersection node of two linked lists. Time: O(m+n), Space: O(1)"""
    if not headA or not headB:
        return None
    
    pointerA, pointerB = headA, headB
    
    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA
    
    return pointerA


def is_palindrome(head):
    """Check if linked list is palindrome. Time: O(n), Space: O(1)"""
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second_half = reverse_iterative(slow.next)
    
    # Compare halves
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True


# ===== ADVANCED OPERATIONS =====

def remove_duplicates_sorted(head):
    """Remove duplicates from sorted linked list. Time: O(n), Space: O(1)"""
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head


def remove_duplicates_unsorted(head):
    """Remove duplicates from unsorted linked list. Time: O(n), Space: O(n)"""
    if not head:
        return head
    
    seen = set()
    seen.add(head.val)
    current = head
    
    while current.next:
        if current.next.val in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next
    
    return head


def rotate_right(head, k):
    """Rotate linked list to right by k positions. Time: O(n), Space: O(1)"""
    if not head or not head.next or k == 0:
        return head
    
    # Find length and make circular
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    tail.next = head  # Make circular
    
    # Find new tail (length - k % length - 1 steps from head)
    k = k % length
    steps_to_new_tail = length - k
    new_tail = head
    
    for i in range(steps_to_new_tail - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head


def partition_list(head, x):
    """Partition list around value x. Time: O(n), Space: O(1)"""
    smaller_head = ListNode(0)
    greater_head = ListNode(0)
    smaller = smaller_head
    greater = greater_head
    
    while head:
        if head.val < x:
            smaller.next = head
            smaller = smaller.next
        else:
            greater.next = head
            greater = greater.next
        head = head.next
    
    greater.next = None
    smaller.next = greater_head.next
    
    return smaller_head.next


# ===== UTILITY FUNCTIONS =====

def linked_list_to_array(head):
    """Convert linked list to array for easier testing."""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


def are_equal(head1, head2):
    """Check if two linked lists are equal."""
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    
    return head1 is None and head2 is None


# ===== TEMPLATES =====

def traverse_template(head):
    """Template for traversing linked list."""
    current = head
    
    while current:
        # Process current.val
        print(current.val)
        current = current.next


def two_pointer_template(head):
    """Template for two pointer problems."""
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # Check condition
        if slow == fast:
            return True
    
    return False


def recursive_template(head):
    """Template for recursive operations."""
    # Base case
    if not head:
        return None
    
    # Recursive case
    result = recursive_template(head.next)
    
    # Process current node
    return head


# ===== TEST FUNCTIONS =====

def test_basic_operations():
    """Test basic linked list operations."""
    print("=== TESTING BASIC OPERATIONS ===\n")
    
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original list: {print_linked_list(head)}")
    print(f"Length: {get_length(head)}")
    print(f"Middle node: {get_middle(head).val}")
    print(f"2nd from end: {get_nth_from_end(head, 2).val}")
    
    # Test insertions
    head = insert_at_beginning(head, 0)
    print(f"After insert 0 at beginning: {print_linked_list(head)}")
    
    head = insert_at_end(head, 6)
    print(f"After insert 6 at end: {print_linked_list(head)}")
    
    head = insert_at_index(head, 3, 2.5)
    print(f"After insert 2.5 at index 3: {print_linked_list(head)}")
    
    # Test deletions
    head = delete_at_beginning(head)
    print(f"After delete at beginning: {print_linked_list(head)}")
    
    head = delete_node_with_value(head, 2.5)
    print(f"After delete value 2.5: {print_linked_list(head)}")
    
    print()


def test_advanced_operations():
    """Test advanced linked list operations."""
    print("=== TESTING ADVANCED OPERATIONS ===\n")
    
    # Test reversal
    head = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {print_linked_list(head)}")
    
    reversed_head = reverse_iterative(head)
    print(f"Reversed: {print_linked_list(reversed_head)}")
    
    # Test palindrome
    palindrome_head = create_linked_list([1, 2, 3, 2, 1])
    print(f"Palindrome test: {print_linked_list(palindrome_head)} -> {is_palindrome(palindrome_head)}")
    
    # Test merge
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    merged = merge_two_sorted(l1, l2)
    print(f"Merged sorted lists: {print_linked_list(merged)}")
    
    # Test cycle detection
    cycle_head = create_linked_list([1, 2, 3, 4])
    # Create cycle: 4 -> 2
    tail = cycle_head
    while tail.next:
        tail = tail.next
    tail.next = cycle_head.next
    
    print(f"Has cycle: {has_cycle(cycle_head)}")
    print(f"Cycle start value: {find_cycle_start(cycle_head).val}")
    print(f"Cycle length: {cycle_length(cycle_head)}")
    
    print()


def create_test_cases():
    """Create various test cases for practice."""
    print("=== TEST CASES FOR PRACTICE ===\n")
    
    test_cases = [
        ([1, 2, 3, 4, 5], "Basic list"),
        ([1], "Single node"),
        ([], "Empty list"),
        ([1, 1, 2, 2, 3], "With duplicates"),
        ([5, 4, 3, 2, 1], "Reverse order"),
        ([1, 3, 2, 4], "Random order")
    ]
    
    for arr, description in test_cases:
        if arr:
            head = create_linked_list(arr)
            print(f"{description}: {print_linked_list(head)}")
        else:
            print(f"{description}: None")
    
    print()


# ===== COMPLEXITY ANALYSIS =====
"""
OPERATION COMPLEXITY ANALYSIS:

Operation               | Time  | Space | Notes
------------------------|-------|-------|-------------------------
Insert at beginning     | O(1)  | O(1)  | Best case for insertion
Insert at end           | O(n)  | O(1)  | Need to traverse to end
Insert at index         | O(n)  | O(1)  | Need to traverse to position
Delete at beginning     | O(1)  | O(1)  | Best case for deletion
Delete at end           | O(n)  | O(1)  | Need to find second-to-last
Delete at index         | O(n)  | O(1)  | Need to traverse to position
Search                  | O(n)  | O(1)  | Linear search only
Access by index         | O(n)  | O(1)  | No random access
Get length              | O(n)  | O(1)  | Unless maintained separately
Reverse                 | O(n)  | O(1)  | Iterative version
Merge two sorted        | O(m+n)| O(1)  | m, n are list lengths
Detect cycle            | O(n)  | O(1)  | Floyd's cycle detection
Find intersection       | O(m+n)| O(1)  | Two pointer technique

LINKED LIST vs ARRAY:

Aspect              | Array     | Linked List
--------------------|-----------|-------------
Memory Layout       | Contiguous| Scattered
Cache Performance   | Better    | Worse
Random Access       | O(1)      | O(n)
Insert/Delete Begin | O(n)      | O(1)
Insert/Delete End   | O(1)*     | O(n)
Memory Overhead     | Lower     | Higher (pointers)
Memory Allocation   | Static    | Dynamic

* Amortized for dynamic arrays

WHEN TO USE LINKED LISTS:
✓ Frequent insertions/deletions at beginning
✓ Size varies significantly during runtime
✓ Don't need random access to elements
✓ Implementing other data structures (stacks, queues)
✓ Memory is limited and you need exact allocation

WHEN TO USE ARRAYS:
✓ Need random access to elements
✓ Frequent access by index
✓ Better cache performance important
✓ Less memory overhead needed
✓ Need to use algorithms like binary search

COMMON PATTERNS:
1. Two Pointers (slow/fast) - cycle detection, middle element
2. Dummy Head - simplifies edge cases in insertion/deletion
3. Runner Technique - find nth from end, intersection
4. Recursion - tree-like problems, reversal
5. Hash Set - remove duplicates, detect intersection

INTERVIEW TIPS:
- Always check for null/empty lists
- Consider edge cases: single node, two nodes
- Draw diagrams to visualize pointer movements
- Use dummy head node to simplify insertion/deletion
- Remember to update all necessary pointers
- Practice both iterative and recursive solutions
"""

if __name__ == "__main__":
    test_basic_operations()
    test_advanced_operations()
    create_test_cases()
    
    print("=== QUICK REFERENCE ===")
    print("Node class: ListNode(val, next)")
    print("Create list: create_linked_list([1,2,3])")
    print("Print list: print_linked_list(head)")
    print("Basic ops: insert_at_*, delete_at_*, search()")
    print("Advanced: reverse_*, has_cycle(), merge_two_sorted()")
    print("Patterns: two pointers, dummy head, recursion")