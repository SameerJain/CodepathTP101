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
    pass

def get_loop_start(head):
    pass

def count_critical_points(head):
    pass
    
def print_list(head):
    if head is None:
        return None
    
    curr = head

    while curr:
        print(f"{curr.value} -> ", end = " " if curr.next else "NULL")
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
#! Problem 4: Middle Match 
#! Problem 5: Where do we begin 
#! Problem 6: Was that a crit?
