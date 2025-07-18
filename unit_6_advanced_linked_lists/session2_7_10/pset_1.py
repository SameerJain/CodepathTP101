class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def is_circular(head):
    slow,fast = head,head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

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
        seen_nodes[curr] = True
        prev = curr
        curr = curr.next
    
    return prev.value

def partition(head, val):
    if head is None:
        return None

    curr1 = head
    curr2 = head
    new_list = Node(0)
    new_head = new_list

    while curr1:
        if curr1.value < val:
            new_list.next = curr1
            new_list = new_list.next
        curr1 = curr1.next

    while curr2:
        if curr2.value >= val:
            new_list.next = curr2
            new_list = new_list.next
        curr2 = curr2.next

    return new_head.next

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
        values.append(curr.value)
        curr = curr.next
    # print(values)
    for idx in range(len(values)):
        if values[idx] == 1:
            final_sum += 2 ** (idx)
        # print(f"{idx} , {final_sum}")

    return final_sum

def add_two_numbers(head_a,head_b):
    list_1_values = []
    list_2_values = []

    while head_a:
        list_1_values.insert(0,head_a.value)
        head_a = head_a.next

    while head_b:
        list_2_values.insert(0,head_b.value)
        head_b = head_b.next

    list_1_sum = 0
    for i in range(len(list_1_values)):
        list_1_sum += list_1_values[i] * (10 ** i)

    list_2_sum = 0
    for i in range(len(list_2_values)):
        list_2_sum += list_2_values[i] * (10 ** i)

    print(list_1_values)

    print(list_1_sum, list_2_sum)

    return list_1_sum + list_2_sum



def reverse_between0(head,m,n):
    temp_head = Node(0)
    temp_head.next = head
    prev = None
    curr = temp_head

    while curr:
        prev = curr
        curr = curr.next
        m -= 1
        n -= 1
        if m == 1:
            start_of_reverse = curr
            while n > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                n -= 1
            head.next = prev
            start_of_reverse.next = curr
            break

    return head

def reverse_between(head, m, n):
    if not head or m == n:
        return head

    # Create a temporary head node to simplify edge cases where m is 1
    temp_head = Node(0)
    temp_head.next = head
    prev = temp_head

    # Step 1: Reach the node just before position m
    for i in range(m - 1):
        prev = prev.next
    
    # `prev` now is the node just before m, and `start` will be the first node to reverse
    start = prev.next
    then = start.next

    # Step 2: Reverse from m to n
    for _ in range(n - m):
        start.next = then.next  # Remove `then` from the list
        then.next = prev.next  # Insert `then` at the beginning of the reversed section
        prev.next = then  # Move `prev` to point to `then` as the new start of the reversed section
        then = start.next  # Move `then` to the next node to be reversed

    return temp_head.next

def print_list(head:Node) -> None:
    if head is None:
        return None
    
    curr = head

    while curr:
        print(f"{curr.value} -> ",end = " " if curr.next else "NULL\n")
        curr = curr.next 

#test nodes 
num6 = Node(6)
num5 = Node(5,num6)
num4 = Node(4,num5)
num3 = Node(3,num4)
num2 = Node(2,num3)
num1 = Node(1,num2)

#! (DONE) Problem 1: Detect Circular Linked List

# num3.next = num1
# print_list(num1)
# print(f"Expected: True{is_circular(num1)}")
# num3.next = num4
# print(is_circular(num1))

#! (DONE) Problem 2: Find Last Node in a Linked List Cycle 

# num4.next = num2
# print(find_last_node_in_cycle(num1))


#! (DONE) Problem 3: Partition List Around Value 

# new_list = partition(num1,3)
# print_list(new_list)


#! (DONE) Problem 4: Convert Binary Number in a Linked List to Integer 
# bin_node_4 = Node(1)
# bin_node_3 = Node(1,bin_node_4)
# bin_node2 = Node(0,bin_node_3)
# bin_node1 = Node(1,bin_node2)

# print(binary_to_int(bin_node1))

#! (DONE) Problem 5: Add Two Numbers Represented by Linked Lists 
# bin_node_4 = Node(9)
# bin_node_3 = Node(8,bin_node_4)
# bin_node2 = Node(6,bin_node_3)
# bin_node1 = Node(1,bin_node2)

# print(add_two_numbers(num1,bin_node1))

#! (DONE) Problem 6: Reverse Sublist of a Linked List 

# new_list = reverse_between(num1,1,5)

# print_list(new_list)
