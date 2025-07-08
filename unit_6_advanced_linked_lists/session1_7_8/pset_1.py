
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def count_element(head,val):
    if head is None:
        return None

    curr = head
    freq_count = 0
    while curr:
        if curr.value == val:
            freq_count += 1
        curr = curr.next
    return freq_count

def print_list(node):
    current = node
    while current:
        print(current.value, end= " -> " if current.next else " -> NULL")
        current = current.next
    print()

def remove_tail_broken(head):
    if head is None:
        return None
    if head.next is None:
        return None

    current = head

    while current.next:
        current = current.next
    
    current.next = None
    return head

def remove_tail_fixed(head):
    if head is None:
        return None
    if head.next is None:
        return None

    current = head

    while current.next.next:
        current = current.next
    
    current.next = None
    return head

def find_middle_element(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value

def is_palindrome(head):
    """
    store the values in a list
    use 2ptrs on the list to see if its a palindrome
    """
    """
    or modify half of the list to be reversed then use 2ptrs on it
    """

def reverse(head):
    pass

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1_2 = Node(1)
node1.next = node2
node2.next = node3
node3.next = node4

#! (DONE) Problem 1: Nested Constructors
# test_list = Node(4,Node(3, Node(2, None)))
# print_list(test_list)

#! (DONE) Problem 2: Find Frequency 
# print_list(node3)
# print(f"Expected: 2 - {count_element(node3,1)}")


#! (DONE) Problem 3: Remove Tail
# print_list(node1)
# remove_tail_fixed(node1)
# print_list(node1)

#! (DONE) Problem 4: Find the Middle 


# print(f"Even. Expected: 3 - {find_middle_element(node1)}")

# #Odd list
# node3.next = None
# print(f"Odd. Expected: 2 - {find_middle_element(node1)}")

# Time: o(n)
# Space: o(1)

#! Problem 5: is palindrome?

node_c = Node(1)
node_b = Node(2,node_c)
node_a = Node(1,node_b)

print_list(node_a)
print(f"1 2 1. Expected: True - {is_palindrome(node1)}")

node_c.next = node1
print_list(node_a)
print(f"Big List. Expected: False - {is_palindrome(node1)}")


#! Problem 6: Put it in reverse