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
    pass

def ll_pop(head,i):
    pass

def find_max(head):
    pass

def delete(head):
    pass

def ll_length(head):
    pass

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def add_first(head,val):
    temp = Node(val)
    temp.next = head
    head = temp
    return temp

def print_list(head):
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
    def __init__(self,value,next = None,pre = None):
        self.value=value
        self.next=next
        self.prev=prev

    def dll_to_sll(dll_head):
        pass


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

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_a.next = node_b
node_b.next = node_c
print_list(node_a)
new_list = add_first(node_a,0)
print_list(new_list)


#! Problem 4: Linked List Length 
head = num1
print(ll_length(head))
head = None







#! Problem 5: Delete Tail 
#! Problem 6: Greatest Node 
#! Problem 7: Pop Node 
#! Problem 8: Find Middle Node 
#! Problem 9: Create Double Links
#! Problem 10: Double to Single 

