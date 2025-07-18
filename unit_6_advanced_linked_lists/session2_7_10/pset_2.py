class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def make_circular(head):
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = head
    return head

def collect_cycle_nodes0(head):
    if head is None:
        return None
    
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    start = head

    while start != slow:
        start = start.next
        slow = slow.next 
    
    values = []
    while True:
        values.append(slow.value)
        slow = slow.next 
        if slow == start:
            break

    return values

def collect_cycle_nodes(head):
    if head is None:
        return None
    curr = head

    seen_before = {}

    while curr:
        if curr in seen_before:
            break
        seen_before[curr] = True
        curr = curr.next

    values = []
    values.append(curr.value)
    loop_start = curr
    curr = curr.next 

    while curr != loop_start:
        values.append(curr.value)
        curr = curr.next
    
    return values


def delete_dupes(head):
    if head is None:
        return None
    if head.next is not None and head.value == head.next.value:
        head = head.next 

    first_dup = head
    prev = None
    curr = head

    while curr:
        if curr.value != first_dup.value:
            first_dup.next = curr
        curr = curr.next

    return head

def rotate_right(head,k):
    pass

def delete_node(head,val):
    pass

def print_list(head:Node) -> None:
    if head is None:
        return None

    curr = head
    counter = 15
    while curr and counter != 0:
        print(f"{curr.value} -> ",end = " " if curr.next else "NULL\n")
        curr = curr.next 
        counter -= 1


#test nodes 
num6 = Node(6)
num5 = Node(1,num6)
num4 = Node(4,num5)
num3 = Node(3,num4)
num2 = Node(1,num3)
num1 = Node(1,num2)




#! (DONE) Problem 1: Convert a Singly Linked List to a Cicular Linked List 
# print_list(num1)
# new_list = make_circular(num1)
# print_list(num1)
#! (DONE) Problem 2: Collect Nodes of a Cycle in a Linked List 
# num4.next = num2

# print(f"Expected- 2,3,4: {collect_cycle_nodes(num1)}")

#! Problem 3: Delete Duplicates in a Linked List 

# new_list = delete_dupes(num1)
# print_list(new_list)

#! Problem 4: Identical Linked Lists 

#! Problem 5: Circular Linked List Rotate 

#! Problem 6: Circular Linked List Delete 
