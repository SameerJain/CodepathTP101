"""
ADVANCED LINKED LISTS - COMPLETE CHEATSHEET
===========================================

Advanced Topics Covered:
1. Complex Node Structures (Random pointers, Multi-level)
2. Advanced Sorting Algorithms (Merge sort, Quick sort)
3. K-Group Operations (Reverse, Swap, Split)
4. Arithmetic Operations (Add numbers, Multiply)
5. Cache Implementation (LRU, LFU)
6. Skip Lists and Advanced Data Structures
7. Graph Representations with Linked Lists
8. Memory-Optimized Algorithms
9. Advanced Pattern Matching
10. Complex Transformations

Key Advanced Patterns:
- Multiple pointer coordination
- Stack/Queue with linked lists
- HashMap integration for O(1) lookups
- Recursive backtracking
- In-place complex operations
- Memory-efficient copying
"""

import heapq
from collections import defaultdict, OrderedDict

# ===== ADVANCED NODE DEFINITIONS =====

class ListNode:
    """Enhanced ListNode with additional utilities."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"
    
    def __lt__(self, other):
        """For heap operations."""
        return self.val < other.val


class RandomListNode:
    """Node with random pointer for copy list problems."""
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random
    
    def __repr__(self):
        random_val = self.random.val if self.random else None
        return f"RandomNode(val={self.val}, random={random_val})"


class MultiLevelNode:
    """Node for multi-level doubly linked list."""
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class SkipListNode:
    """Node for skip list implementation."""
    def __init__(self, val=0, level=0):
        self.val = val
        self.forward = [None] * (level + 1)


# ===== ADVANCED SORTING ALGORITHMS =====

def merge_sort_linked_list(head):
    """
    Sort linked list using merge sort.
    Time: O(n log n), Space: O(log n) - recursive stack
    """
    if not head or not head.next:
        return head
    
    # Split list into two halves
    def get_middle(head):
        slow = fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None  # Split the list
        return slow
    
    def merge(l1, l2):
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
        
        current.next = l1 or l2
        return dummy.next
    
    middle = get_middle(head)
    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(middle)
    
    return merge(left, right)


def quick_sort_linked_list(head):
    """
    Sort linked list using quicksort.
    Time: O(n log n) average, O(n²) worst, Space: O(log n)
    """
    def get_tail(head):
        while head and head.next:
            head = head.next
        return head
    
    def partition(start, end):
        if start == end or start == end.next:
            return start
        
        pivot = start
        current = start.next
        
        while current != end.next:
            if current.val < pivot.val:
                start = start.next
                start.val, current.val = current.val, start.val
            current = current.next
        
        start.val, pivot.val = pivot.val, start.val
        return start
    
    def quick_sort_rec(start, end):
        if start != end and start != end.next:
            pivot = partition(start, end)
            quick_sort_rec(start, pivot)
            quick_sort_rec(pivot.next, end)
    
    if not head:
        return head
    
    tail = get_tail(head)
    quick_sort_rec(head, tail)
    return head


def merge_k_sorted_lists_heap(lists):
    """
    Merge k sorted lists using min heap.
    Time: O(n log k), Space: O(k)
    """
    heap = []
    
    # Add first node of each list to heap
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next


# ===== K-GROUP OPERATIONS =====

def reverse_k_group(head, k):
    """
    Reverse nodes in k-group.
    Time: O(n), Space: O(1)
    """
    def reverse_segment(start, end):
        prev = end.next
        current = start
        
        while current != end.next:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        return end
    
    def get_kth_node(start, k):
        current = start
        for i in range(k - 1):
            if not current:
                return None
            current = current.next
        return current
    
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    
    while True:
        start = prev_group_end.next
        end = get_kth_node(start, k)
        
        if not end:
            break
        
        next_group_start = end.next
        new_start = reverse_segment(start, end)
        
        prev_group_end.next = new_start
        start.next = next_group_start
        prev_group_end = start
    
    return dummy.next


def swap_pairs(head):
    """
    Swap every two adjacent nodes.
    Time: O(n), Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        # Perform swap
        prev.next = second
        first.next = second.next
        second.next = first
        
        prev = first
    
    return dummy.next


def split_list_to_parts(head, k):
    """
    Split linked list into k parts.
    Time: O(n), Space: O(k)
    """
    # Get length
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    part_size = length // k
    extra_nodes = length % k
    
    result = []
    current = head
    
    for i in range(k):
        part_head = current
        current_part_size = part_size + (1 if i < extra_nodes else 0)
        
        # Move to end of current part
        for j in range(current_part_size - 1):
            if current:
                current = current.next
        
        # Break the connection
        if current:
            next_part = current.next
            current.next = None
            current = next_part
        
        result.append(part_head)
    
    return result


# ===== ARITHMETIC OPERATIONS =====

def add_two_numbers(l1, l2):
    """
    Add two numbers represented as linked lists (reverse order).
    Time: O(max(m,n)), Space: O(max(m,n))
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next


def add_two_numbers_ii(l1, l2):
    """
    Add two numbers represented as linked lists (normal order).
    Time: O(max(m,n)), Space: O(max(m,n))
    """
    def reverse_list(head):
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
    
    # Reverse both lists
    rev_l1 = reverse_list(l1)
    rev_l2 = reverse_list(l2)
    
    # Add reversed lists
    result = add_two_numbers(rev_l1, rev_l2)
    
    # Reverse result
    return reverse_list(result)


def multiply_two_numbers(l1, l2):
    """
    Multiply two numbers represented as linked lists.
    Time: O(m*n), Space: O(m+n)
    """
    def list_to_number(head):
        num = 0
        while head:
            num = num * 10 + head.val
            head = head.next
        return num
    
    def number_to_list(num):
        if num == 0:
            return ListNode(0)
        
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        
        dummy = ListNode(0)
        current = dummy
        for digit in reversed(digits):
            current.next = ListNode(digit)
            current = current.next
        
        return dummy.next
    
    num1 = list_to_number(l1)
    num2 = list_to_number(l2)
    product = num1 * num2
    
    return number_to_list(product)


# ===== COPY WITH RANDOM POINTER =====

def copy_random_list(head):
    """
    Deep copy linked list with random pointers.
    Time: O(n), Space: O(n)
    """
    if not head:
        return None
    
    # Phase 1: Create copy nodes and interweave them
    current = head
    while current:
        copy_node = RandomListNode(current.val)
        copy_node.next = current.next
        current.next = copy_node
        current = copy_node.next
    
    # Phase 2: Set random pointers for copy nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Phase 3: Separate original and copy lists
    dummy = RandomListNode(0)
    copy_current = dummy
    current = head
    
    while current:
        copy_current.next = current.next
        current.next = current.next.next
        copy_current = copy_current.next
        current = current.next
    
    return dummy.next


def copy_random_list_hashmap(head):
    """
    Copy with random pointer using hashmap.
    Time: O(n), Space: O(n)
    """
    if not head:
        return None
    
    node_map = {}
    
    # First pass: create all nodes
    current = head
    while current:
        node_map[current] = RandomListNode(current.val)
        current = current.next
    
    # Second pass: set next and random pointers
    current = head
    while current:
        if current.next:
            node_map[current].next = node_map[current.next]
        if current.random:
            node_map[current].random = node_map[current.random]
        current = current.next
    
    return node_map[head]


# ===== FLATTEN MULTI-LEVEL LIST =====

def flatten_multilevel_list(head):
    """
    Flatten multi-level doubly linked list.
    Time: O(n), Space: O(1)
    """
    if not head:
        return head
    
    current = head
    
    while current:
        if current.child:
            # Save next node
            next_node = current.next
            
            # Connect to child
            current.next = current.child
            current.child.prev = current
            current.child = None
            
            # Find tail of child branch
            child_tail = current.next
            while child_tail.next:
                child_tail = child_tail.next
            
            # Connect child tail to saved next
            if next_node:
                child_tail.next = next_node
                next_node.prev = child_tail
        
        current = current.next
    
    return head


def flatten_multilevel_recursive(head):
    """
    Flatten using recursive approach.
    Time: O(n), Space: O(d) where d is max depth
    """
    def flatten_rec(head):
        current = head
        tail = None
        
        while current:
            if current.child:
                child_tail = flatten_rec(current.child)
                next_node = current.next
                
                # Connect to child
                current.next = current.child
                current.child.prev = current
                current.child = None
                
                # Connect child tail to next
                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail
                
                tail = child_tail
                current = next_node
            else:
                tail = current
                current = current.next
        
        return tail
    
    if head:
        flatten_rec(head)
    return head


# ===== LRU CACHE IMPLEMENTATION =====

class LRUCache:
    """
    LRU Cache using doubly linked list + hashmap.
    Time: O(1) for get/put, Space: O(capacity)
    """
    
    class DLLNode:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Create dummy head and tail
        self.head = self.DLLNode()
        self.tail = self.DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """Add node right after head."""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Remove an existing node."""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """Move node to head (mark as recently used)."""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """Remove last node (least recently used)."""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node
    
    def get(self, key):
        node = self.cache.get(key)
        
        if node:
            # Move to head (mark as recently used)
            self._move_to_head(node)
            return node.val
        
        return -1
    
    def put(self, key, value):
        node = self.cache.get(key)
        
        if node:
            # Update value and move to head
            node.val = value
            self._move_to_head(node)
        else:
            new_node = self.DLLNode(key, value)
            
            if len(self.cache) >= self.capacity:
                # Remove LRU item
                tail = self._pop_tail()
                del self.cache[tail.key]
            
            self.cache[key] = new_node
            self._add_node(new_node)


# ===== LFU CACHE IMPLEMENTATION =====

class LFUCache:
    """
    LFU Cache using multiple doubly linked lists.
    Time: O(1) for get/put, Space: O(capacity)
    """
    
    class Node:
        def __init__(self, key=0, val=0, freq=0):
            self.key = key
            self.val = val
            self.freq = freq
            self.prev = None
            self.next = None
    
    class DLList:
        def __init__(self):
            self.head = LFUCache.Node()
            self.tail = LFUCache.Node()
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0
        
        def add_to_head(self, node):
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            self.size += 1
        
        def remove_node(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        
        def remove_tail(self):
            if self.size > 0:
                tail_node = self.tail.prev
                self.remove_node(tail_node)
                return tail_node
            return None
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.cache = {}  # key -> node
        self.freq_map = defaultdict(self.DLList)  # freq -> DLList
    
    def _update_freq(self, node):
        """Update frequency of a node."""
        old_freq = node.freq
        new_freq = old_freq + 1
        
        # Remove from old frequency list
        self.freq_map[old_freq].remove_node(node)
        
        # Update min_freq if necessary
        if old_freq == self.min_freq and self.freq_map[old_freq].size == 0:
            self.min_freq += 1
        
        # Add to new frequency list
        node.freq = new_freq
        self.freq_map[new_freq].add_to_head(node)
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._update_freq(node)
            return node.val
        return -1
    
    def put(self, key, value):
        if self.capacity == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove LFU item
                lfu_list = self.freq_map[self.min_freq]
                lfu_node = lfu_list.remove_tail()
                del self.cache[lfu_node.key]
            
            # Add new node
            new_node = self.Node(key, value, 1)
            self.cache[key] = new_node
            self.freq_map[1].add_to_head(new_node)
            self.min_freq = 1


# ===== SKIP LIST IMPLEMENTATION =====

class SkipList:
    """
    Skip List for O(log n) search/insert/delete.
    Expected Time: O(log n), Space: O(n)
    """
    
    def __init__(self):
        self.max_level = 16
        self.header = SkipListNode(-1, self.max_level)
        self.level = 0
    
    def _random_level(self):
        """Generate random level for new node."""
        import random
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level
    
    def search(self, target):
        current = self.header
        
        # Start from highest level and go down
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].val < target:
                current = current.forward[i]
        
        current = current.forward[0]
        return current and current.val == target
    
    def add(self, num):
        update = [None] * (self.max_level + 1)
        current = self.header
        
        # Find position to insert
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        # If value doesn't exist, insert new node
        if not current or current.val != num:
            new_level = self._random_level()
            
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level
            
            new_node = SkipListNode(num, new_level)
            
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node
    
    def erase(self, num):
        update = [None] * (self.max_level + 1)
        current = self.header
        
        # Find node to delete
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        # If found, delete the node
        if current and current.val == num:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            
            # Update level
            while self.level > 0 and not self.header.forward[self.level]:
                self.level -= 1
            
            return True
        return False


# ===== ADVANCED TRANSFORMATIONS =====

def reorder_list(head):
    """
    Reorder list: L0→L1→...→Ln-1→Ln becomes L0→Ln→L1→Ln-1→...
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second_half = slow.next
    slow.next = None
    
    def reverse(head):
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
    
    second_half = reverse(second_half)
    
    # Merge two halves
    first = head
    second = second_half
    
    while second:
        temp1 = first.next
        temp2 = second.next
        
        first.next = second
        second.next = temp1
        
        first = temp1
        second = temp2


def odd_even_list(head):
    """
    Group odd and even positioned nodes together.
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return head
    
    odd = head
    even = head.next
    even_head = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    
    odd.next = even_head
    return head


def remove_zero_sum_sublists(head):
    """
    Remove consecutive nodes that sum to 0.
    Time: O(n), Space: O(n)
    """
    dummy = ListNode(0)
    dummy.next = head
    
    prefix_sum = 0
    sum_map = {0: dummy}
    current = head
    
    # First pass: build prefix sum map
    while current:
        prefix_sum += current.val
        sum_map[prefix_sum] = current
        current = current.next
    
    # Second pass: remove zero sum sublists
    prefix_sum = 0
    current = dummy
    
    while current:
        prefix_sum += current.val
        current.next = sum_map[prefix_sum].next
        current = current.next


# ===== ADVANCED PATTERN MATCHING =====

def find_pattern_in_list(head, pattern):
    """
    Find if pattern exists as sublist.
    Time: O(n*m), Space: O(1)
    """
    if not pattern:
        return True
    if not head:
        return False
    
    current = head
    
    while current:
        if current.val == pattern[0]:
            # Check if pattern matches from current position
            temp_current = current
            pattern_idx = 0
            
            while temp_current and pattern_idx < len(pattern):
                if temp_current.val != pattern[pattern_idx]:
                    break
                temp_current = temp_current.next
                pattern_idx += 1
            
            if pattern_idx == len(pattern):
                return True
        
        current = current.next
    
    return False


def longest_increasing_sublist(head):
    """
    Find length of longest increasing sublist.
    Time: O(n), Space: O(1)
    """
    if not head:
        return 0
    
    max_length = 1
    current_length = 1
    prev = head
    current = head.next
    
    while current:
        if current.val > prev.val:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
        
        prev = current
        current = current.next
    
    return max_length


# ===== UTILITY FUNCTIONS =====

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


def print_linked_list(head, max_nodes=20):
    """Print linked list with cycle detection."""
    if not head:
        return "None"
    
    result = []
    current = head
    seen = set()
    count = 0
    
    while current and count < max_nodes:
        if id(current) in seen:
            result.append(f"... -> CYCLE to {current.val}")
            break
        
        seen.add(id(current))
        result.append(str(current.val))
        current = current.next
        count += 1
    
    if current and count >= max_nodes:
        result.append("...")
    elif not current:
        result.append("None")
    
    return " -> ".join(result)


def benchmark_operation(operation, *args, iterations=1000):
    """Benchmark an operation."""
    import time
    
    start_time = time.time()
    for _ in range(iterations):
        operation(*args)
    end_time = time.time()
    
    avg_time = (end_time - start_time) / iterations
    return avg_time


# ===== TEST FUNCTIONS =====

def test_advanced_sorting():
    """Test advanced sorting algorithms."""
    print("=== TESTING ADVANCED SORTING ===\n")
    
    # Test merge sort
    head = create_linked_list([4, 2, 1, 3, 5])
    print(f"Original: {print_linked_list(head)}")
    
    sorted_head = merge_sort_linked_list(head)
    print(f"Merge sorted: {print_linked_list(sorted_head)}")
    
    # Test quick sort
    head2 = create_linked_list([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Original: {print_linked_list(head2)}")
    
    quick_sort_linked_list(head2)
    print(f"Quick sorted: {print_linked_list(head2)}")
    
    print()


def test_k_group_operations():
    """Test k-group operations."""
    print("=== TESTING K-GROUP OPERATIONS ===\n")
    
    # Test reverse k-group
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    print(f"Original: {print_linked_list(head)}")
    
    reversed_head = reverse_k_group(head, 3)
    print(f"Reverse in groups of 3: {print_linked_list(reversed_head)}")
    
    # Test swap pairs
    head2 = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {print_linked_list(head2)}")
    
    swapped_head = swap_pairs(head2)
    print(f"Swap pairs: {print_linked_list(swapped_head)}")
    
    print()


def test_arithmetic_operations():
    """Test arithmetic operations."""
    print("=== TESTING ARITHMETIC OPERATIONS ===\n")
    
    # Test add two numbers
    l1 = create_linked_list([2, 4, 3])  # 342
    l2 = create_linked_list([5, 6, 4])  # 465
    print(f"Number 1: {print_linked_list(l1)} (represents 342)")
    print(f"Number 2: {print_linked_list(l2)} (represents 465)")
    
    result = add_two_numbers(l1, l2)
    print(f"Sum: {print_linked_list(result)} (represents 807)")
    
    print()


def test_cache_implementations():
    """Test cache implementations."""
    print("=== TESTING CACHE IMPLEMENTATIONS ===\n")
    
    # Test LRU Cache
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(f"LRU get(1): {lru.get(1)}")  # 1
    lru.put(3, 3)  # evicts 2
    print(f"LRU get(2): {lru.get(2)}")  # -1
    
    # Test LFU Cache
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(f"LFU get(1): {lfu.get(1)}")  # 1
    lfu.put(3, 3)  # evicts 2 (least frequent)
    print(f"LFU get(2): {lfu.get(2)}")  # -1
    
    print()


# ===== COMPLEXITY ANALYSIS =====
"""
ADVANCED OPERATIONS COMPLEXITY:

Operation                    | Time        | Space      | Notes
----------------------------|-------------|------------|------------------
Merge Sort                  | O(n log n)  | O(log n)   | Stable, recursive
Quick Sort                  | O(n log n)* | O(log n)   | *O(n²) worst case
Merge K Lists (heap)        | O(n log k)  | O(k)       | n = total nodes
Reverse K Groups            | O(n)        | O(1)       | In-place
Copy with Random Ptr        | O(n)        | O(1)       | Interweaving trick
Copy with Random Ptr (map)  | O(n)        | O(n)       | Hash map approach
Flatten Multi-level         | O(n)        | O(1)       | Iterative
LRU Cache Operations        | O(1)        | O(capacity)| HashMap + DLL
LFU Cache Operations        | O(1)        | O(capacity)| Multiple DLLs
Skip List Operations        | O(log n)*   | O(n)       | *Expected time
Add Two Numbers             | O(max(m,n)) | O(max(m,n))| m,n = list lengths
Pattern Matching            | O(n*m)      | O(1)       | n=list, m=pattern
Remove Zero Sum Sublists    | O(n)        | O(n)       | Prefix sum map

ADVANCED PATTERNS:

1. **Interweaving Pattern**: Copy with random pointer
   - Create copy nodes between original nodes
   - Set pointers, then separate lists

2. **Multiple Frequency Lists**: LFU Cache
   - Maintain separate DLL for each frequency
   - Update min_frequency dynamically

3. **Prefix Sum Elimination**: Remove zero sum sublists
   - Build prefix sum map
   - Remove nodes between same prefix sums

4. **Layered Processing**: Multi-level flattening
   - Process child branches immediately
   - Maintain connection to next main branch

5. **Divide and Conquer**: Merge sort for linked lists
   - Split list recursively
   - Merge sorted sublists

MEMORY OPTIMIZATION TECHNIQUES:

1. **In-place Operations**: Minimize extra space
   - Reverse operations without extra nodes
   - Swap operations using only pointers

2. **Dummy Node Pattern**: Simplify edge cases
   - Avoid special handling for head operations
   - Uniform treatment of all nodes

3. **Two-Phase Processing**: Separate concerns
   - First pass: gather information
   - Second pass: perform transformations

4. **Probabilistic Data Structures**: Skip lists
   - Expected O(log n) performance
   - Self-balancing through randomization

INTERVIEW STRATEGIES:

1. **Identify the Pattern**: 
   - Multiple pointers (fast/slow, k-apart)
   - Stack/recursion for reversal problems
   - HashMap for O(1) lookups

2. **Consider Edge Cases**:
   - Empty lists, single nodes
   - Cycles in input
   - Very large inputs

3. **Optimize Step by Step**:
   - Start with brute force
   - Identify bottlenecks
   - Apply appropriate data structures

4. **Practice Complex Combinations**:
   - Sort + merge operations
   - Copy + transform operations
   - Cache + data structure problems

REAL-WORLD APPLICATIONS:

- **LRU/LFU Caches**: Database buffer pools, CPU caches
- **Skip Lists**: Alternative to balanced trees in databases
- **Multi-level Lists**: HTML DOM traversal, file systems
- **Arithmetic Lists**: Big integer arithmetic, polynomial operations
- **Pattern Matching**: DNA sequence analysis, text processing
"""

if __name__ == "__main__":
    test_advanced_sorting()
    test_k_group_operations() 
    test_arithmetic_operations()
    test_cache_implementations()
    
    print("=== ADVANCED PATTERNS SUMMARY ===")
    print("1. Interweaving: Copy with random pointers")
    print("2. Multi-frequency: LFU cache implementation") 
    print("3. Prefix sum: Remove zero sum sublists")
    print("4. Layered processing: Flatten multi-level lists")
    print("5. Divide & conquer: Merge sort for linked lists")
    print("6. Probabilistic: Skip list for O(log n) operations")