class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def is_circular(head):
    slow,fast = head,head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow == fast
    
def find_last_node_in_cycle(head):
    if head is None:
        return None

    prev = None
    curr = head
    seen_nodes = {}
    
    while curr:
        if curr in seen_nodes.keys():
            break
        prev = curr
        curr = curr.next
    
    return prev

def partition(head, val):
    less_head, more_head = Node(0), Node(0)
    temp_less, temp_more = less_head, more_head

    curr = head

    while curr:
        if curr.value < val:
            temp_less.next = curr
        elif curr.value > val:
            temp_more.next = curr
        else:
            part_node = curr
        curr = curr.next

    less_head = less_head.next
    more_head = more_head.next
    temp_less.next = part_node
    part_node.next = temp_more

    return less_head 


def binary_to_int(head):
    """
    collect values of linked list in array
    put values at front of the list 

    create count variable
    add to count by 2^(idx + 1)
    """

    if head is None:
        return None
    
    values = []
    curr = head
    final_sum = 0

    while curr:
        values.insert(0,curr.value)
        curr = curr.next
    
    for idx in range(len(values)):
        final_sum += 2 ** (idx)

    return final_sum


def add_two_numbers(head_a,head_b):
    list_1_values = []
    list_2_values = []

    while head_a:
        list_1_values.insert(0,head_a.value)
        head_a = head_a.next

    while head_b:
        list_1_values.insert(0,head_b.value)
        head_b = head_b.next
    
    list_1_sum = 0
    for i in range(len(list_1_values)):
        list_1_sum += list_1_values[i] * (10 ** i)

    list_2_sum = 0
    for i in range(len(list_2_values)):
        list_2_sum += list_2_values[i] * (10 ** i)

    return list_1_sum + list_2_sum

def reverse_between(head,m,n):
    prev = None
    curr = head

    while curr:
        prev = curr
        curr = curr.next
        m -= 1
        n -= 1
        if m == 0:
            while n > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                n -= 1

    return head

def print_list(head:Node) -> None:
    pass
#test nodes 
num5 = Node(5)
num4 = Node(4,num5)
num3 = Node(3,num4)
num2 = Node(2,num3)
num1 = Node(1,num2)

#! Problem 1: Detect Circular Linked List
print_list(num5) 
num3.next = num1

#! Problem 2: Find Last Node in a Linked List Cycle 

#! Problem 3: Partition List Around Value 

#! Problem 4: Convert Binary Number in a Linked List to Integer 

#! Problem 5: Add Two Numbers Represented by Linked Lists 

#! Problem 6: Reverse Sublist of a Linked List 

