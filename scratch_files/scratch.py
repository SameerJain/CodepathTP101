class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def print_list(head:Node) -> None:
    if head is None:
        return None
    
    curr = head

    while curr:
        print(f"{curr.value} -> ",end = " " if curr.next else "NULL\n")
        curr = curr.next 

def shuffle(head):
    # Write your code here
    if head is None:
        return None
    
    if head.next is None:
        return 
    
    curr1 = head
    curr2 = head.next
    
    temp_head = curr2
    prev = Node(0)
    while curr1 and curr1.next:
        curr1.next = curr2.next
        curr2.next = curr1
        prev.next = curr2
        prev = curr1
        curr1 = curr1.next
        if curr1 is not None and curr1.next is not None:
            curr2 = curr1.next
    
    head = temp_head

    return head

#test nodes 

num5 = Node("e")
num4 = Node("d",num5)
num3 = Node("c",num4)
num2 = Node("b",num3)
num1 = Node("a",num2)

print_list(num1)

new_list = (shuffle(num1))
print_list(new_list)