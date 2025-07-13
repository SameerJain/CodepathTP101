class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def frequency_map(head: None) -> dict[int, int]:
    freqs = {}

    if head is None:
        return None

    curr = head

    while curr:
        freqs[curr.value] = freqs.get(curr.value,0) + 1
        curr = curr.next
    
    return freqs
    # Time: O(n)
    # Space: O(n)

# Function with a bug!
def remove_by_value(head, val):
    # Handle empty list and removal from the head
    if not head:
        return None
    if head.value == val:
        return head.next  # Return the second node as the new head

    current = head
    while current.next:
        if current.next.value == val:
            node_to_remove = current.next
            current.next = current.next.next
            node_to_remove.next = None# Skip the node with the value
            return head  # Return the original head
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

def cycle_length(head):
    if head is None:
        return head
    
    curr = head
    seen_before = {}
    while curr:
        if curr in seen_before:
            break
        seen_before[curr] = True
        curr = curr.next
    
    counter = 1
    cycle_end = curr
    curr = curr.next

    while curr:
        if curr == cycle_end:
            break
        counter += 1
        curr = curr.next
    return counter

"""
find the start of the cycle 
iterate again thru the list 

"""


def reverse_first_k(head, k):
    prev = None
    curr = head
    tail = head

    while k > 0 and curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        k -= 1

    while curr:
        tail.next = curr
        curr = curr.next
        tail = tail.next 

    return prev

def print_list(head: Node) -> None:
    if head is None:
        print("Head is None")
        return 

    curr = head

    while curr:
        print(f"{curr.value} -> ",end = " " if curr.next else "NULL\n")
        curr = curr.next

#Test Nodes

node6 = Node(6)
node5 = Node(5,node6)
node4 = Node(4,node5)
node3 = Node(3,node4)
node2 = Node(2,node3)
node1 = Node(1,node2)

#! (DONE) Problem 1: The Power of One
#? On the codepath description and answer key this seems to be 2 different problems combined

# head = Node("Ash",(Node("Misty",Node("Brock"))))

# print_list(head)

#! (DONE) Problem 2: Frequency Map 

# print_list(node1)

# print(frequency_map(node1))

#! (DONE) Problem 3: Get it out of here!

# print_list(node1)
# new_list = remove_by_value(node1,2)
# print_list(new_list)

#! (DONE) Problem 4: Does it cycle
# node4.next = node2
# print(has_cycle(node1))

#! (DONE)Problem 5: Are we there Yet 
# node4.next = node2
# print(f"Expected: 3. Result: {cycle_length(node1)}")

#!  (DONE) Problem 6: Reverse Them, K?

# print_list(node1)
# new_list = reverse_first_k(node1,3)
# print_list(new_list)

