
class Player():
    def __init__(self,character,kart):
        self.character = character
        self.kart = kart
    self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"
    
    def set_player(self,nums):
        pass

    def add_item(self,item_name):
        pass

    def print_inventory(self):
        pass

    def print_results(race_results):
        pass

    def _get_place(my_player):
        pass

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

    def chase_list():
        pass
#! Problem 1: Player Class

#! Problem 2: Player Match

#! Problem 3: Update Kart 
print(player_one.get_player())

# < your code to update kart>

print(player_one.get_player())

#! Problem 4: Set Character 
player_one.set_player("Peach")
player_two.set_player("Kermit")

#! Problem 5: Add Special Item
player_one = Player("Yoshi", "Dolphin Dasher")
# items = []

player_one.add_item("red shell")
# items = ["red shell"]

player_one.add_item("super star")
# items = ["red shell", "super star"]

player_one.add_item("super smash")
# items = ["red shell", "super star"]

#! Problem 6: Print Inventory 
player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()

#! Problem 7: Race Results 
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)

#! Problem 8: Get Rank 
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place("Luigi")
print(player1_rank)

player2_rank = get_place("Peach")
print(player2_rank)

player3_rank = get_place("Mario")
print(player3_rank)


class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    


#! Problem 9: Tom and Jerry
print(cat.value)
print(cat.next)
print(cat.next.value)
print(mouse.value)
print(mouse.next) 

#! Problem 10: Chase List 
print(dog.value)
print(dog.next)
print(dog.next.value)
print(cat.next)
print(cat.next.value)
print(mouse.next.value)

#! Problem 11: Update Chase 



#! Problem 12: Chase String 
dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))