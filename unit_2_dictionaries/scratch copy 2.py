
#! Problem 3: Print Pair 
def print_pair(dictionary,target):
    found = False
    for i in dictionary:
        if(i == target):
            print(f"Key: {i}\nValue: {dictionary.get(i)}")
            found = True
    if not found:
        print("That pair does not exist!")
    

dictionary = {"Spongebob": "Squarepants","Squidward":"Tentacles","Patrick":"Star"}


print_pair(dictionary,"Patrick")
print_pair(dictionary,"Plankton")
print_pair(dictionary,"Spongebob")
