class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def find_max(head):
    if head is None:
        return None
    curr = head
    max_val = curr.value

    while curr.next:
        max_val = max(max_val,curr.value)
        curr = curr.next
    
    return max_val

def middle_match(head,val):
    slow,fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow.value == val

def get_loop_start(head):
    """
    determine if there is a cycle    
    if there is not then return none

    """
    seen_before = {}
    curr = head
    while curr:
        if curr in seen_before.keys():
            return curr.value
        seen_before[curr] = True
        curr = curr.next
    return None

def count_critical_points(head):
    pass
    
def print_list(head):
    if head is None:
        return None
    
    curr = head

    while curr:
        print(f"{curr.value} -> ", end = " " if curr.next else "NULL\n")
        curr = curr.next
    return 


#Test list
node8 = Node(8,None)
node7 = Node(7,node8)
node6 = Node(6,node7)
node5 = Node(5,node6)
node4 = Node(4,node5)
node3 = Node(3,node4)
node2 = Node(2,node3)
node1 = Node(1,node2)

#! (DONE) Problem 1: One to Many 
# head = Node("Mario", Node("Luigi",Node("Wario")))
# print_list(head)

#! (DONE) Problem 2: Find Max

# node5.value = 10
# print(f"Expected: 10: {find_max(node1)}")

#! Problem 3: Remove First Value 
# Function with a bug!
def remove_by_value(head, val):
    # Check if the list is empty
    if head is None:
        return head

    # If the node to be removed is the head of the list
    if head.value == val:
        return head.next

    # Initialize pointers
    current = head.next
    previous = head

    # Traverse the list to find the node to remove
    while current:
        if current.value == val:
            previous.next = current.next
            current.next = None
            return head
        previous = current
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head

# print_list(node1)
# new_list = remove_by_value(node1,8)
# print_list(node1)

#! (DONE) Problem 4: Middle Match 

# print(middle_match(node1,1))
# Time: o(n)
# Space: o(1)

#! Problem 5: Where do we begin 
node4.next = node2

print(get_loop_start(node1))

#! Problem 6: Was that a crit?

