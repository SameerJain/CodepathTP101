
class Pokemon:
    def __init__(self, name, types,evolution=None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution
    

    def __repr__(self):
        return f"Pokemon(name='{self.name}', types={self.types})"
        
    def print_pokemon(self):
        return ({
            "name": self.name,
            "types": self.types,
            "is_caught":self.is_caught
        })
    


    def catch(self):
        self.is_caught = True
    
    def choose(self):
        if self.is_caught:
            print((f"{self.name} I choose you!"))
        else:
            print(f"{self.name} is wild! Catch them if you can!")

    def add_type(self,new_type):
        self.types.append(new_type)
        
def get_evolutionary_line(starter_pokemon: Pokemon) -> list[Pokemon]:
    result = []
    current = starter_pokemon
    result.append(current)
    while current.evolution:

        result.append(current.evolution)
        current = current.evolution
        
    return result

def get_by_type(my_pokemon,pokemon_type):
    result = []
    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            result.append(pokemon)
    return result
#! (DONE) Problem 1: Pokemon Class 
# Pikachu = Pokemon("Pikachu","Electric")
# print(Pikachu.name, Pikachu.types, Pikachu.is_caught)

#! (DONE) Problem 2: Create Squirtle 
# squirtle = Pokemon("Squirtle","Water")
# squirtle.print_pokemon()

#! (DONE) Problem 3: Is Caught
# squirtle.is_caught = True
# squirtle.print_pokemon()

#! (DONE) Problem 4: Catch Pokemon
# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()

#! (DONE) Problem 5: Choose Pokemon 
# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()

#! (DONE) Problem 6: Add Pokemon Type

# jigglypuff = Pokemon("Jigglypuff",["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()
    

#! (DONE) Problem 7: Get Pokemon 

####? this problem statement print statement could be better
# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print([pokemon.name for pokemon in normal_pokemon])


#! (DONE) Problem 8: Pokemon Evolution 
# charizard = Pokemon("Charizard", ["fire", "flying"])
# charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
# charmander = Pokemon("Charmander", ["fire"], charmeleon)

# charmander_list = get_evolutionary_line(charmander)
# print(charmander_list)

# charmeleon_list = get_evolutionary_line(charmeleon)
# print(charmeleon_list)

# charizard_list = get_evolutionary_line(charizard)
# print(charizard_list)




class Node:
    def __init__(self,value,next= None):
        self.value = value
        self.next = next

def print_linked_list(head):
    temp = head
    result = []
    while temp:
        result.append(temp.value)
        temp = temp.next
    newres = " -> ".join(result)
    newres += "-> NULL"
    print(newres)


#! (DONE) Problem 9: Node Class

node_one = Node('a')
node_two = Node('b')

# print(node_one.value)
# print(node_one.next)
# print(node_two.value)
# print(node_two.next)


#! (DONE) Problem 10: Linking Nodes
node_one.next = node_two


# print(node_one.value)
# print(node_one.next.value)
# print(node_two.value)

#! (DONE) Problem 11: Mario Party 

node_1 = Node("Mario")
node_2 = Node("Luigi")
node_3 = Node("Wario")
node_4 = Node("Toad")

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = None

# print(node_1.value,"->",node_1.next.value)
# print(node_2.value,"->",node_2.next.value)
# print(node_3.value,"->",node_3.next.value)
# print(node_4.value,"->",node_4.next)

#! (DONE) Problem 12: Printing Linked List
print_linked_list(node_1)
