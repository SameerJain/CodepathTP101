class Player():
    def __init__(self,character,kart, opponent = None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent

    def get_player(self):
        return print(f"{self.character} driving the {self.kart}",end=" \n")
    
    def set_player(self,name):
        valid_characters = ["Mario","Luigi","Peach","Yoshi","Toad","Wario","Donkey Kong","Bowser"]
        if name not in valid_characters:
            return print("Invalid Character")
        
        self.character = name
        
        return print("Character Updated")

    def add_item(self,item_name):
        valid_items =["banana","green shell","red shell","bob-omb","super star","lightning","bullet bill"]
        if item_name not in valid_items:
            return 
        self.items.append(item_name)
        return 

    def print_inventory(self):
        
        if len(self.items) == 0:
            return print("Inventory Empty")

        player_inventory = {}

        for item in self.items:
            player_inventory[item] = player_inventory.get(item,0) + 1
        return print(player_inventory)

def print_results(race_results):
    print("Race Results:")
    for i in range(len(race_results)):
        print(f"{i+1}. {race_results[i].character}")

def get_place(my_player):
    counter = 1
    curr = my_player
    while curr.ahead:
        counter += 1
        curr = curr.ahead
    return counter



class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}"

    def chase_list(self):
        curr = self
        print(f"{curr.value}", end = " ")
        while curr.next:
            print(f"chases {curr.next.value}", end = " ")
            curr = curr.next
        return 

#? I think there is a missing tab in the problem description 
#!(DONE) Problem 1: Player Class

player_one = Player("Yoshi","Super Blooper")


#! (DONE) Problem 2: Player Match

player_two = Player("Bowser","Pirhana Prowler")
player_one.get_player()
print("vs", end = " ")
player_two.get_player()

#? went from print to return for function
#! (DONE) Problem 3: Update Kart 
player_one.get_player()


player_one.kart = "Dolphin Dasher"
player_one.get_player()

#! (DONE) Problem 4: Set Character 

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

#! (DONE) Problem 6: Print Inventory 
player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()

#!(DONE) Problem 7: Race Results 
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)

#? Over here you are not passing in the object just the name
#! (DONE) Problem 8: Get Rank 
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
print(player1_rank)

player2_rank = get_place(peach)
print(player2_rank)

player3_rank = get_place(mario)
print(player3_rank)

#? how to pass in name of an object
#! (DONE) Problem 9: Tom and Jerry

cat = Node("Tom")
mouse = Node("Jerry")

cat.next = mouse

print(cat.value)
print(cat.next)
print(cat.next.value)
print(mouse.value)
print(mouse.next) 

#? I am gettingn an error when i print mouse.next.value
#! Problem 10: Chase List 
dog = Node("Spike")
dog.next = cat
print(dog.value)
print(dog.next)
print(dog.next.value)
print(cat.next)
print(cat.next.value)
print(mouse.next)

#! Problem 11: Update Chase 
dog.next = None

cheese = Node("Gouda")


#! Problem 12: Chase String 
dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

dog.chase_list()
