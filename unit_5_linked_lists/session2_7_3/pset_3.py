class Player:
    def __init__(self,character,kart,outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes
    
    def get_toutnament_place(self,opponents):
        pass


class Node:
    def __init(self,value,next=None):
        self.value = value
        self.next = next
    
    def add_second(head,val):
        pass

    def increment_ll(head):
        pass

def copy_ll(head):
    pass

def find_min(head):
    pass

def ll_remove(head,val):
    pass

def tail_to_head(head):
    pass

def get_length(node):
    pass


def print_list(head):
    pass

#! Problem 1: Calculate Tournament Placement
print("Problem 1: ")

player1 = Player("Mario","Standard",[1,2,1,1,3])
player2 = Player("Luigi","Standard",[2,1,3,2,2])
player3 = Player("Peach","Standard",[3,3,2,3,1])

opponents = [player2,player3]
print(f"{player1.character} was number {player1.get_tournament_place(opponent)}")

#! Problem 2: Update Linked List Sequence 
print("Problem 2: ")

red = Node('red')
yellow = Node('yellow')
blue = Node('blue')
red.next = yellow
yellow.next = blue

#! Problem 3: Insert Node as second element 
print("Problem 3: ")

num1 = Node(1)
num3 = Node(3)
num4 = Node(4)
num1.next = num3
num3.next = num4

head = num1
add_second(head,2)


#! Problem 4: Increment Linked List Node Values 
print("Problem 4: ")

print(my_list.value)

my_list = increment_ll(my_list)
print(my_list.value)
my_list.value

my_list = increment_ll(my_list)
print(my_list.value)

#! Problem 5: Copy Linked List 
print("Problem 5: ")

copy = copy_ll(head)    
print(head.value,copy.value)

head.value = 10
print(head.value,copy.value)



#! Problem 6: Find Minimum in Linked List 
print("Problem 6: ")

#! Problem 7: Remove Node by Value from Linked List 
print("Problem 7:")

#! Problem 8: Move Tail to Front of Linked List 
print("Problem 8:")

#! Problem 9: Convert Singly Linked List to doubly Linked List 
print("Problem 9:")

crazy_in_love = Node("Crazy in Love")
formation = Node("Formation")
texas_hold_em = Node("Texas Hold Em")
crazy_in_love.next = formation
formation.next = texas_hold_em

#! Problem 10: Find Length of Doubly Linked List from any node 
print("Problem 10:")