class Pokemon():
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self,opponent):
        opponent.hp -= self.damage
        if opponent.hp <= 0:
            print(f"{opponent.name} fainted")
        else:
            print(f"{self.name} dealt {self.damage} to {opponent.name}")

class Node:
    def __init__(self,value,next=None,prev = None):
        self.value = value
        self.next = next
        self.prev = prev
    
    def __repr__(self):
        return f"value: {self.value}"

def print_list(head):
    curr = head
    while curr:
        print(curr.value, "->", end=" ")
        curr = curr.next
    print("NULL")
    return

def add_first(head,new_node):
    new_node.next = head
    return new_node

def get_tail(head):
    curr = head
    while curr.next:
        curr = curr.next
    return curr

def ll_replace(head,original,replacement):
    curr = head

    while curr:
        if curr.value == original:
            curr.value = replacement
        curr = curr.next
    
    return head

def listify_first_n(head,n):
    result = []
    curr = head
    counter = 0
    while curr is not None and counter < n:
        result.append(curr.value)
        curr = curr.next
        counter += 1
    return result

def ll_insert(head,val,i):
    """
    if idx is 0
        insert before head

    get to idx before target idx 
    set new node to next one
    set curr to new node

    if we get to the end of the list

    """
    
    new_node = Node(val)
    counter = 0
    curr = head
    while curr.next and counter < i - 1:
        curr = curr.next
        counter += 1

    new_node.next = curr.next
    curr.next = new_node

    return new_node

def list_to_linked_list(lst):
    
    """
    set curr node
    iterate thru list
        create a temp node equal to that value
        set curr.next equal to it 
    set curr next to none
    """
    head = curr = Node(lst[0])

    for i in range(1,len(lst)):
        temp_node = Node(lst[i])
        curr.next = temp_node
        curr = curr.next
    return head
    
        

def print_reverse(tail):
    curr = tail
    
    while curr:
        print(curr.value, end = " ")
        curr = curr.prev
    pass


#! (DONE) Problem 1: Battle Pokemon
# pikachu = Pokemon("Pikachu", 35, 200)
# bulbasaur = Pokemon("Bulbasaur", 45, 30) 

# opponent = bulbasaur
# pikachu.attack(opponent)

#! (DONE) Problem 2: Convert to Linked List

# node_1 = Node("Jigglypuff")
# node_2 = Node("Wigglypuff")
# node_1.next = node_2

# print(node_1.value,"->",node_1.next.value)
# print(node_2.value,"->",node_2.next)
# print_list(node_1)

#!(DONE) Problem 3: Add First

#Using the Linked List from Problem 2
# print(node_1.value, "->", node_1.next.value)

# new_node = Node("Ditto")
# node_1 = add_first(node_1, new_node)
# print(node_1.value, "->", node_1.next.value, "->", node_1.next.next.value)

#! (DONE) Problem 4: Get Tail

# num1 = Node(1)
# num2 = Node(2)
# num3 = Node(3)
# num1.next = num2
# num2.next = num3


# head = num1
# tail = get_tail(num1)
# print(tail) 

#!(DONE) Problem 5: Replace Node 

# num3 = Node(5)
# num2 = Node(6,num3)
# num1 = Node(5,num2)

# head = num1
# ll_replace(head,5,"banana")
# print_list(head)

#! (DONE) Problem 6: List Nodes

# a = Node('a')
# b = Node('b')
# c = Node('c')

# j = Node('j')
# k = Node('k')
# l = Node('l')

# head = a
# a.next= b
# b.next = c

# lst = listify_first_n(head,2)
# print(lst)

# head2 = j
# j.next = k
# k.next = l
# lst2 = listify_first_n(head2,5)
# print(lst2)

#! (DONE) Problem 7: Insert Value

# a.value = 3
# b.value = 8
# c.value = 12
# c.next = j
# j.value = 9
# j.next = None


# print_list(a)
# ll_insert(a,20,70)
# print_list(a)


#! (DONE) Problem 8: Linked Listify 
# normal_list = ["Betty","Veronica","Archie","Jughead"]
# linked_list = list_to_linked_list(normal_list)
# print_list(linked_list)

#! (DONE) Problem 9: Doubly Linked List 

# poliwag = Node("Poliwag")
# poliwhirl = Node("Poliwhirl")
# poliwrath = Node("Poliwrath")

# poliwag.next = poliwhirl
# poliwhirl.next = poliwrath

# poliwhirl.prev = poliwag
# poliwrath.prev = poliwhirl

# print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)

# #! (DONE) Problem 10: Print Backwards 

# print_reverse(poliwrath)
