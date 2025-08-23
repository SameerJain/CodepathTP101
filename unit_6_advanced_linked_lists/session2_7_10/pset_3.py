class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    
    def circular_list_length(head):4dfe496] testing autosave
 1 file changed
        """
        edge cases for empty or small linked lists 
        first detect if a cycle exists
            if it doesnt exist, return an error 
        put a head as the start of the linked list
        have an iterator variable that will go through the cycle
        if the iterator reaches the starter, we have ended the loop
        return the counter variable
        """

        if not head:
            return None 
        
        if head.next is None:
            return None
        
        slow, fast = head, head.next 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                is_cycle = True
                break
        
        if not is_cycle:
            return None 
        
        curr = head
        counter = 0
        while curr:
            curr = curr.next 
            counter += 1
            if curr == head:
                break
        return counter 


    def detect_and_remove_cycle(head):
        """
        standard edge cases
        first check if there is a cycle 
        get to the end of the cycle 
        break the link by setting it to none 
        return the new list  
        """
        if not head:
            return None
        if head.next is None:
            return None 
        
        slow, fast = head, head
        is_cycle = False 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next 
            if slow == fast:
                is_cycle = True 
                break
        
        if not is_cycle:
            return False
        
        curr = head
        while curr:
            if curr.next == head:
                curr.next = None
            curr = curr.next 
        return head 

    def merge_two_lists(head_a,head_b):

        if head_a is None and head_b is None:
            return None 
        if head_a is None:
            return head_b
        if head_b is None:
            return head_a
        
        temp_node = Node(-1)
        temp_node.next = head_a
        curr = temp_node
        new_head = curr

        while head_a and head_b:
            if head_a.value < head_b.value:
                curr.next = head_a
                head_a = head_a.next
            elif head_b.value <= head_a.value:
                curr.next = head_b
                head_b = head_b.next 
            curr = curr.next 
        
        if head_a:
            curr.next = head_a
        if head_b:
            curr.next = head_b
        
        return new_head.next


    def skip_and_remove(head,m,n):
        """
        manage edge cases: empty list, m or n are negative values, 
        set a bool for if m is 0
        iterate thru the list using a curr and a prev pointer 
            skip:
                move curr up m times, using a counter variable and subtracting down
            delete:
                set prev to curr
                move curr up n times or if curr.next is None
                set prev.next to curr 
                    if m = 0 is active, set curr to head. if not this if statement just wont run
        return head 
        """


        if not head:
            return None 

        if m < 0 or n < 0:
            return "m or n cannot be 0"

        no_skips = True if m == 0 else False

        prev = None
        temp_node = Node(-1,head)
        curr = temp_node

        while curr:
            skip_count = m
            while skip_count > 0:
                skip_count -=1
                curr = curr.next 
            prev = curr
            del_count = n
            while del_count > 0:
                del_count -= 1
                curr = curr.next 
                if curr == None:
                    prev.next = curr
                    return head 
            if no_skips:
                head = curr
            prev.next = curr
        
        return head 



    def rotate_doubly_linked_list(head,k):
        """
        make the list circular
        move to one before the spot to rotate
        set that next one to head 
        break the link
        """

        if head is None:
            return None

        curr = head 
        while curr.next:
            curr = curr.next
        curr.next = head

        curr = head 
        while k > 1:
            curr = curr.next
        curr.next = head 
        curr.next = None

        return head 

    def merge_nodes(head):
    """
    create a min_val 
    create a val for the current sum of all zeros
    if the node value is zero then we compare and swap. 
    """

    curr = head
    min_val = float(inf)
    sum_val = 0
    temp,temp_head = ,Node(0), Node(0)
    
    while curr:
        if curr.value == 0:
            newNode = Node(num_val)
            temp.next = newNode
            temp = temp.next 
            min_val = min(min_val,sum_val)
            sum_val = 0
        else:
            sum_val += curr.value
    return min_val, temp_head


#! Problem 1: Circular Linked List Length 


node_1 = Node(5)
node_2 = Node(4)






#! Problem 2: Detest and REmove Cycle in a Linked List 
#! Problem 3: Merge Two Sorted Linked Lists 
#! Problem 4: Skip and Remove Nodes in a Linked List 
#! Problem 5: Rotate a Doubly Linked List to the left 
#! Problem 6: Merge Nodes Between Zeros in a Linked List 








