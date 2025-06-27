
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
    
    def print_pokemon(self):
        print({
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
        
        pass
    
    def get_by_type(my_pokemon,pokemon_type):
        pass

    def get_evolutionary_line(starter_pokemon):
        pass
    
    def print_linked_list(head):
        pass

    

#! Problem 1: Pokemon Class 
Pikachu = Pokemon("Pikachu","Electric")
print(Pikachu.name, Pikachu.types, Pikachu.is_caught)

#! Problem 2: Create Squirtle 
squirtle = Pokemon("Squirtle","Water")
squirtle.print_pokemon()

#! Problem 3: Is Caught
squirtle.is_caught = True
squirtle.print_pokemon()

#! Problem 4: Catch Pokemon
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()

#! Problem 5: Choose Pokemon 
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()
#! Problem 6: Add Pokemon Type

jigglypuff = Pokemon("Jigglypuff",["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()


#! Problem 7: Get Pokemon 
jigglypuff = Pokemon("Jigglypuff",["Normal","Fairy"])
diglett = Pokemon("Diglett",["Ground"])
meowth  = Pokemon("Meowth",)


#! Problem 8: Pokemon Evolution 


#! Problem 9: Node Class


#! Problem 10: Linking Nodes


#! Problem 11: Mario Party 


#! Problem 12: Printing Linked List
