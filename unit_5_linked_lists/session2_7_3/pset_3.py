class Player:
    def __init__(self,character,kart,outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes
    
    def get_tournament_place(self,opponents):
        avgs = []
        ranks_sum = 0

        for rank in self.race_outcomes:
            ranks_sum += rank
        self_avg = (ranks_sum / len(self.race_outcomes))
        avgs.append(self_avg)

        for opponent in opponents:
            ranks_sum = 0
            for rank in opponent.race_outcomes:
                ranks_sum += rank
            avgs.append(ranks_sum / len(opponent.race_outcomes))

        avgs.sort()

        for i in range(len(avgs)):
            if self_avg == avgs[i]:
                return i + 1

        return "Error"



class Node:
    def __init__(self,value,next=None,prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    
    def add_second(head,val):
        if not head:
            return None
        
        new_node = Node(val)
        new_node.next = head.next
        head.next = new_node

        return head


    def increment_ll(head):
        curr = head
        while curr:
            curr.value += 1
            curr = curr.next
        return head

def copy_ll(head):
    if head is None:
        return None

    new_head = Node(head.value)
    new_head.next = (head.next)
    curr = head.next

    while curr:
        new_node = Node(curr.value)
        new_node.next = curr.next
        curr = curr.next

    return new_head


def find_min(head):
    curr = head
    min_val = curr.value

    while curr:
        min_val = min(min_val,curr.value)
        curr = curr.next

    return min_val

def ll_remove(head,val):
    curr = head

    while curr.next:
        if curr.next.value == val:
            curr.next = curr.next.next
        curr = curr.next
    return head

def tail_to_head(head):

    curr = head
    prev = None

    while curr.next:
        prev = curr
        curr = curr.next

    prev.next = None
    curr.next = head

    return curr

def get_length_dll(node):
    """
    move to start of list going back 
    go to start 
    """
    curr = node
    counter = 0
    while curr.prev:
        curr = curr.prev
    
    while curr:
        counter += 1
        curr = curr.next
    
    return counter

def print_list_sll(head):
    if head is None:
        return None

    curr = head
    while curr:
        print(f"{curr.value} -> ", end=" ")
        curr = curr.next
    print("NULL")
    return "Print Complete"

def print_list_dll(head):
    if head is None:
        return None
    curr = head
    while curr:
        print(f"{curr.value} <->", end = " ")
        curr = curr.next
    print("NULL")
    return


#! Problem 1: Calculate Tournament Placement
print("\n\nProblem 1: ")

player1 = Player("Mario","Standard",[1,2,1,1,3])
player2 = Player("Luigi","Standard",[2,1,3,2,2])
player3 = Player("Peach","Standard",[3,3,2,3,1])

opponents = [player2,player3]
print(f"{player1.character} was number {player1.get_tournament_place(opponents)}")

#! Problem 2: Update Linked List Sequence 
print("\n\nProblem 2: ")

red = Node('red')
yellow = Node('yellow')
blue = Node('blue')
red.next = yellow
yellow.next = blue

print(f"Orginal: {print_list_sll(red)}")

orange = Node('orange')
green = Node('green')
red.next = orange
orange.next = yellow
yellow.next = green
green.next = blue


print(f"New: {print_list_sll(red)}")

#! Problem 3: Insert Node as second element 
print("\n\nProblem 3: ")

num1 = Node(1)
num3 = Node(3)
num4 = Node(4)
num1.next = num3
num3.next = num4

head = num1
print(f"Original: {print_list_sll(head)}")
head.add_second(2)
print(f"New: {print_list_sll(head)}")

#! Problem 4: Increment Linked List Node Values 
print("\n\nProblem 4: ")

my_list = Node(5)
my_list2 = Node(6)
my_list3 = Node(7)
my_list.next = my_list2
my_list2.next = my_list3

print(f"Old list{my_list.value}")

my_list = my_list.increment_ll()
print(f"Expected: 6 - {my_list.value}")
my_list.value

my_list = my_list.increment_ll()
print(f"Expected: 7 - {my_list.value}")

#! Problem 5: Copy Linked List 
print("\n\nProblem 5: ")

copy = copy_ll(num1)    
print(f"copy: {num1.value,copy.value}")

num1.value = 10
print(num1.value,copy.value)

#! Problem 6: Find Minimum in Linked List 
print("\n\nProblem 6: ")

test_node5 = Node(5)
test_node6 = Node(6)
test_node7 = Node(7)

test_node5.next = test_node6
test_node6.next = test_node7

print(f"Minimum Value: {find_min(test_node5)}")
#! Problem 7: Remove Node by Value from Linked List 
print("\n\nProblem 7:")

print(f"Old List:\n {print_list_sll(test_node5)}")
ll_remove(test_node5,6)
print(f"New List\n: {print_list_sll(test_node5)}")

#! Problem 8: Move Tail to Front of Linked List 
print("\n\nProblem 8:")

test_node1 = Node(1)
test_node2 = Node(2)
test_node3 = Node(3)
test_node4 = Node(4)
test_node1.next = test_node2
test_node2.next = test_node3
test_node3.next = test_node4

print(f"Old List:\n {print_list_sll(test_node1)}")
new_list = tail_to_head(test_node1)
print(f"New List\n: {print_list_sll(new_list)}")

#! Problem 9: Convert Singly Linked List to doubly Linked List 
print("\n\nProblem 9:")

crazy_in_love = Node("Crazy in Love")
formation = Node("Formation")
texas_hold_em = Node("Texas Hold Em")
crazy_in_love.next = formation
formation.next = texas_hold_em

print(f"Current Singly Linked List:{print_list_sll(crazy_in_love)}")
print(f"Desired Doubly Linked List: {print_list_dll(crazy_in_love)}")

#! Problem 10: Find Length of Doubly Linked List from any node 
print("\n\nProblem 10:")

test_node_double_3 = Node(3)
test_node_double_5 = Node(5)
test_node_double_6 = Node(6)
test_node_double_7 = Node(7)

test_node_double_3.next = test_node_double_5
test_node_double_5.next = test_node_double_6
test_node_double_6.next = test_node_double_7

test_node_double_7.prev = test_node_double_6
test_node_double_6.prev = test_node_double_5
test_node_double_5.prev = test_node_double_3


print(get_length_dll(test_node_double_6))