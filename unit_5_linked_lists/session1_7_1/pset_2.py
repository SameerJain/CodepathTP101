class Card():
    
    valid_suits = ["Hearts","Spades","Clubs","Diamonds"]
    valid_ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    rank_values = {"Jack":11,"Queen":12,"King":13,"Ace":1}

    def __init__(self,suit,rank,next = None):
        self.suit = suit
        self.rank = rank
        self.next = next

    def __str__(self): #this is used to print out a specific instance of the class
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    def is_valid(self):

        
        if self.suit not in self.valid_suits:
            return False
        
        if self.rank not in self.valid_ranks:
            return False

        return True

    def get_value(self):
        if self.rank in self.rank_values.keys():
            return self.rank_values[self.rank]
        elif self.rank in self.valid_ranks:
            return int(self.rank)
        return None

def print_hand(starting_card):
    result = []
    curr = starting_card

    while curr:
        result.append(curr)
        curr = curr.next

    return print(result)

class Hand:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return f"{self.cards}"

    def add_card(self,card):
        self.cards.append(card)

    def remove_card(self,card):
        self.cards.remove(card)

    def print_hand(self):
        print(f"{self.cards}")

def sum_hand(hand):
    sum_total = 0
    for card in hand.cards:
        sum_total += card.get_value()
    return sum_total





#! (DONE) Problem 1: Card Class
card = Card("Spades","8")

#!(DONE) Problem 2: Print Card
card = Card("Clubs","Ace")

# card.print_card()

#! (DONE) Problem 3: #! Verify Update 
card = Card("Hearts","Ace")

# card.print_card()

#! (DONE) Problem 4: #! Valid Card
# my_card = Card("Hearts","7")
# print(my_card.is_valid())

# second_draw = Card("Spades","Joker")
# print(second_draw.is_valid())

#! (DONE) Problem 5: Get Value 
# card = Card("Hearts","7")
# print(card.get_value()) 

# card_two = Card("Spades","Jack")
# print(card_two.get_value()) 




#! (DONE) Problem 6: Hand Class
# card_one = Card("Hearts", "3")
# card_two = Card("Spades", "8")

# player1_hand = Hand()
# player1_hand.print_hand()
# # cards = []
# player1_hand.add_card(card_one)
# player1_hand.print_hand()
# # cards = [card_one]
# player1_hand.add_card(card_two)
# player1_hand.print_hand()
# # cards = [card_one, card_two]
# player1_hand.remove_card(card_one)
# player1_hand.print_hand()
# # cards = [card_two]
# print(card)

#! (DONE) Problem 7: Sum of Cards

# card_one = Card("Hearts", "3")
# card_two = Card("Hearts", "Jack")
# card_three = Card("Spades", "3")

# hand = Hand()
# hand.add_card(card_one)
# hand.add_card(card_two)
# hand.add_card(card_three)

# sum_val = sum_hand(hand)
# print(sum_val)

#? how to print out the name that was given to an object like what it wants in the test case

#! Problem 8: Print Hand 
card_one = Card("Hearts","3")
card_two = Card("Hearts","4")
card_three = Card("Diamonds","King")

card_one.next = card_two
card_two.next = card_three
print_hand(card_one)


class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next 

def print_linked_list(head):
    pass


# #! Problem 9: Head and Tail Nodes 
# print(head.value)
# print(head.next)
# print(tail.value)
# print(tail.next)

# #! Problem 10: Middle Node 
# print(head.next.value)
# print(middle.next.value)
# print(tail.next.value)

# #! Problem 11: Zodiac Signs 
# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)

# #! Problem 12: Print Linked List
# # input linked list: a->b->c->d->e
# print_linked_list(a)


