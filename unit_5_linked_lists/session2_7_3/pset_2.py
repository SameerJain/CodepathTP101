class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

def is_two_pair(player_hand):
    suits = ["Hearts","Spades","Clubs","Diamonds"]
    rank = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    freqs = {}
    for card in player_hand:
        freqs[card.rank] = freqs.get(card.rank,0) + 1
    pair_count = 0
    for value in freqs.values():
        if value >= 2:
            pair_count += 1
        if pair_count >= 2:
            return True
    return False

def find_middle_node(head):
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next 
        if fast == None:
            return slow
        slow = slow.next

    return slow

def ll_pop(head,i):
    if not head:
        return None

    counter = 0
    curr = head
    if i == 0:
        head = head.next
        curr.next = None
        return head
    
    while counter < i - 1:
        curr = curr.next
        counter += 1
        if curr is None:
            return head
    curr.next = curr.next.next 
    return head


def find_max(head):
    curr = head
    max_val = 0
    while curr:
        max_val = max(max_val,curr.value)
        curr = curr.next
    return max_val


def delete_tail(head):

    if head is None:
        return None
    
    if head.next is None:
        head = None
        return head
    
    curr = head

    while curr.next.next:
        curr = curr.next 
    curr.next = None


    return head

def ll_length(head):
    curr = head
    counter = 0
    while curr:
        counter += 1
        curr = curr.next
        
    return counter

class Node:
	def __init__(self, value, next=None,prev = None):
		self.value = value
		self.next = next
        # self.prev = prev

def add_first(head,val):
    temp = Node(val)
    temp.next = head
    head = temp
    return temp

def print_list(head):
    if head is None:
        return None

    curr = head
    while curr:
        print(f"{curr.value} -> ",end = "")
        curr = curr.next

    return print("|NULL")

class SLLNode:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
        

class DLLNode:
    def __init__(self,value,next = None):
        self.value=value
        self.next=next


def dll_to_sll(dll_head):
    curr = dll_head
    while curr:
        curr.prev = None
        curr = curr.next
    return curr


#! (DONE) Problem 1: Poker Two Pair Hand 
# card_one = Card("Hearts", "Ace")
# card_two = Card("Hearts", "4")
# card_three = Card("Diamonds", "Ace")
# card_four = Card("Diamonds", "4")
# card_five = Card("Diamonds", "6")
# card_six = Card("Diamonds", "7")

# player_one_hand = [card_one, card_two, card_three, card_four, card_five]
# print(is_two_pair(player_one_hand))

# player_two_hand = [card_two, card_three, card_four, card_five, card_six]
# print(is_two_pair(player_two_hand))
#! (DONE) Problem 2: Barbie Linked List 

node_1 = Node("Barbie")
node_2 = Node("President Barbie")
node_3 = Node("Weird Barbie")
node_4 = Node("Ken")

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)

# print_list(node_1)

#! (DONE) Problem 3: Insert Value First 

# node_a = Node("A")
# node_b = Node("B")
# node_c = Node("C")
# node_a.next = node_b
# node_b.next = node_c
# print_list(node_a)
# new_list = add_first(node_a,0)
# print_list(new_list)


#! (DONE) Problem 4: Linked List Length 
"""
iterate thru list with counter variable
Get to end of list
return counter variable 
"""

num1 = Node(1)
num2 = Node(2)
num3 = Node(3)

num1.next = num2
num2.next = num3

# head = num1
# print(ll_length(head))

# head = None
# print(ll_length(head))


#! (DONE) Problem 5: Delete Tail 

# # original list of 3
# print_list(num1)

# # deleting 3 
# delete_tail(num1)
# print_list(num1)

# # deleting 2
# delete_tail(num1)
# print_list(num1)

# # deleting 1
# delete_tail(num1)
# print_list(num1)

#! (DONE) Problem 6: Greatest Node 

num4 = Node(10)
num3.next = num4

# max_val = find_max(num1)
# print(max_val)

#! (DONE) Problem 7: Pop Node 

# print_list(num1)
# num1 = ll_pop(num1,0)
# print_list(num1)

#! (DONE) Problem 8: Find Middle Node 

num5 = Node(4)
num4.next = num5
# head = num1
# mid = find_middle_node(head)
# print(mid.value)

#! (DONE) Problem 9: Create Double Links
# head = Node("First")
# tail = Node("Last")

# head.next = tail
# tail.prev = head

# print(head.value, "<->", head.next.value)
# print(tail.prev.value, "<->", tail.value)

#! (DONE)Problem 10: Double to Single 

Ice = DLLNode("Ice")
Water = DLLNode("Water")
Steam = DLLNode("Steam")

Ice.next = Water
Water.next = Steam

Steam.prev = Water
Water.prev = Steam

dll_head = Ice

print_list(dll_head)
sll_head = dll_to_sll(dll_head)
print_list(dll_head)


