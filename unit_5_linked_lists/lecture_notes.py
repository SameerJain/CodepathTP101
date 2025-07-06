"""
Problem #1

Write a function to reverse a singly linked list. The function should take the head of a linked list as input and return the new head of the reversed linked list.

Examples:
Input: head = [1 -> 2 -> 3 -> 4 -> 5]
Output: [5 -> 4 -> 3 -> 2 -> 1]
Input: head = [1]
Output: [1]
Input: head = None(DONE)(DONE)(DONE)
Output: None done
"""

class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

def print_list(head: Node) -> None:
    curr = head
    while curr:
        print(f"{curr.value}",end = " -> " if curr.next else " -> NULL\n")
        curr = curr.next
    return

def reverse_list(head: Node) -> Node:
    prev = None
    curr = head
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print_list(node1)
new_list_head = reverse_list(node1)
print_list(new_list_head)

"""
Problem #2
Write a function to remove all duplicate values from a sorted linked list. After removing duplicates, each element in the list should appear only once.
Examples:
Input: head = [1 -> 1 -> 2]
Output: [1 -> 2]
Input: head = [1 -> 1 -> 2 -> 3 -> 3]
Output: [1 -> 2 -> 3]
Input: head = []
Output: []
"""

def remove_duplicates(head: Node) -> Node:
    """
    set 2 nodes to start
    case for size 0
    iterate the fast ptr till fast.next
        if fast.next != slow.val
            move slows next to fast.next
            fast.next is None
            fast is now slow.next
            move up slow

                   F
    1 -> 1 -> 2 -> 3
                   S   
    """
    slow = head
    fast = head

    while fast.next:
        if fast.next.value != slow.value:
            slow.next = fast.next
            fast.next = None
            fast = slow.next
            slow = slow.next
        if fast.next != None:
            fast = fast.next
    return head


node15 = Node(3)
node14 = Node(3,node15)
node13 = Node(2,node14)
node12 = Node(1,node13)
node11 = Node(1,node12)

print_list(node11)
new_head = remove_duplicates(node11)
print_list(node11)

