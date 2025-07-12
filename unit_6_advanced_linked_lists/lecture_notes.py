# Write a function to find the middle node of a singly linked list. If the list has an even number of nodes, return the second middle node.

# Examples:
# Input: head = [1, 2, 3, 4, 5]
# Output: Node with value 3
# Input: head = [1, 2, 3, 4, 5, 6]
# Output: Node with value 4

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Examples:
# Input: s = "leetcode"
# Output: 0
# Input: s = "loveleetcode"
# Output: 2
# Input: s = "aabb"
# Output: -1

"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""


"""
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    
def print_list(head: Node):
    if head is None:
        return print("Head is None")
    
    curr = head

    while curr:
        print(f"{curr.value} -> ",end = " " if curr.next else "NULL\n")
        curr = curr.next 
    return 





# def merge_two_linked_lists(head1: Node,head2: Node) -> Node | None:
#     if head1 is None or head2 is None:
#         return None
    
#     curr1 = head1
#     curr2 = head2
#     # print(f"Setting curr values to iterate over list. curr1.value = {curr1.value}, curr2 = {curr2.value}")

#     temp = Node(None)
#     new_head = temp
    
#     # print(f"Setting temp variable to construct list and new head as access point. temp value = {temp.value}. temp.next.value = {temp.next.value}")

#     while curr1 and curr2:
#         if curr1.value < curr2.value:
#             # print(f"curr1 < curr2. {curr1.value} vs {curr2.value}")
#             temp.next = curr1
#             # print(f"New temp value = {temp.value}")
#             curr1 = curr1.next
#             # if curr1:
#                 # print(f"new curr1 = {curr1.value}") 
#         elif curr1.value >= curr2.value:
#             # print(f"curr1 > curr2. {curr1.value} vs {curr2.value}")
#             temp.next = curr2
#             # print(f"New temp value = {temp.value}")
#             curr2 = curr2.next
#             # if curr2:
#                 # print(f"new curr2 = {curr2.value}") 

#         temp = temp.next

#     while curr1:
#         temp.next = curr1
#         curr1 = curr1.next
#         temp = temp.next

#     while curr2:
#         temp.next = curr2
#         curr2 = curr2.next
#         temp = temp.next
    
#     new_head = new_head.next
#     return new_head




node5 = Node(9,None)
node4 = Node(7,node5)
node3 = Node(5,node4)
node2 = Node(3,node3)
node1 = Node(1,node2)

nodee = Node(8,None)
noded = Node(6,nodee)
nodec = Node(5,noded)
nodeb = Node(4,nodec)
nodea = Node(2,nodeb)


"""
understand the problem
ask clarifying questions 
go through a test case

think about the solution
write it with initial head

then create a program to trace
then add the back solution
then trace

thwn add if statement for the start
then trace

then add edge cases 
"""

"""




return none if both lists are empty
create a new_head to access new list 
iterate thru both linked lists
    check if the current value for one list is less than the value of the other
        put the next ptr to the smaller node
    if 1 list is complete 
        end loop
return new_head


1 -> 3 -> 5

2 -> 4 -> 6

1-> 2 -> 3 -> 4 -> 5 -> 6 
"""

def merge_two_linked_lists(head1,head2):
    if head1 is None and head2 is None:
        return None

    curr_1 = head1 #1
    curr_2 = head2 #2

    new_head = None

    if curr_1.value < curr_2.value: # 1< 2
        new_head = curr_1 # 1
        curr_1 = curr_1.next # curr_1 = 3
    elif curr_1.value >= curr_2.value:
        new_head = curr_2
        curr_2 = curr_2.next
    
    temp = new_head # temp = 1

    while temp: 
        if curr_1.value < curr_2.value: # 3, 
            temp.next = curr_1
            curr_1 = curr_1.next
        elif curr_1.value >= curr_2.value:
            temp.next = curr_2
            curr_2 = curr_2.next
        
        temp = temp.next

        if curr_1 is None or curr_2 is None:
            break

    if curr_1 or curr_2:
        while curr_1:
            temp.next = curr_1
            curr_1 = curr_1.next
            temp = temp.next
        while curr_2:
            temp.next = curr_2
            curr_2 = curr_2.next
            temp = temp.next

    return new_head

new_list = merge_two_linked_lists(node1,nodea)
print_list(new_list)
