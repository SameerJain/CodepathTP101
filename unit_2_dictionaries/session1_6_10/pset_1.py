
#! Problem 1: Subsequence
'''
get length of sequence
iterate thru lst
if we have the same number we continue our counter
if its different we reset
if we finish the sequence we return true
ret false
'''
def is_subsequence(lst,sequence):
    seq_length = len(sequence)
    seq_index = 0
    for ele in lst:

        #print(f"ele:{ele} seq_length: {seq_length}, seq_index: {seq_index}\n")
        if ele == sequence[seq_index]:
            #print(f"sequence number found. ele: {ele}. seq_index = {seq_index}")
            seq_index += 1
        
        if seq_index == seq_length:
            #print(f"passed. seq_index {seq_index} seq_length {seq_length}")
            return True
        
    return False
    

lst = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,8,11]
# print(is_subsequence(lst,sequence))


#! Problem 2: Create a Dictionary 
def create_dictionary(keys,values):
    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    print(new_dict.items())

keys = ["peanut","dragon","star","pop","space"]
values = ["butter","fly","fish","corn","ship"]

#create_dictionary(keys,values)

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


# print_pair(dictionary,"Patrick")
# print_pair(dictionary,"Plankton")
# print_pair(dictionary,"Spongebob")




#! Problem 4: Keys Versus Values
def keys_v_values(dictionary):
    key_sum,value_sum = 0,0
    for key, value in dictionary.items():
        key_sum += key
        value_sum += value
    if key_sum > value_sum:
        return "keys"
    elif key_sum < value_sum:
        return "values"
    else:
        return "balanced"
dictionary1 = {1:10,2:20,3:30,4:40,5:50,6:60}
greater_sum = keys_v_values(dictionary1)
#print(greater_sum)

dictionary2 = {100:10,200:20,300:30,400:40,500:50,600:60}
greater_sum = keys_v_values(dictionary2)
#print(greater_sum)

#! Problem 5: Restock Inventory
'''
iterate thru current inventory 
if we have the key already we add to it
otherwise we create the key and add the value
'''
def restock_inventory(current_inventory,restock_list):
    for key,value in restock_list.items():
        if key in current_inventory.keys():
            current_inventory[key] += value
        else:
            current_inventory[key] = value
    return current_inventory

current_inventory = {
    "apples":30,
    "bananas":15,
    "oranges":10
}

restock_list = {
    "oranges":20,
    "apples":10,
    "pairs": 5
}

# print(restock_inventory(current_inventory,restock_list))

#! Problem 6: Calculate GPA
def calculate_gpa(report_card):
    
    grade_values = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
    }
    
    total_points = 0
    
    for value in report_card.values():
        total_points += grade_values[value]
        
    return total_points / len(report_card.values()) 

report_card = {"Math":"A","Science":"C","History":"A","Art":"B","English":"B","Spanish":"A"}

# print(calculate_gpa(report_card))

#! Problem 7: Best Book 
def highest_rated(books):
    highest_rating = books[0]
    for book in books[1:]:
        if book["Rating"] > highest_rating["Rating"]:
            highest_rating = book
    return highest_rating

books = [                  
    {"Title": "Tomorrow, and Tomorrow, and Tomorrow",
    "Author": "Gabrielle Zevin",
    "Rating": 4.18
    },
    
    {
        "Title": "A Fortune For Your Disaster",
        "Author": "Hanif Abdurraqib",
        "Rating": 4.47
    },
    
    {    
        "Title": "The Seven Jusband of Evenlyn Hugo",
        "Author": "Taylor Jenkins Reid",
        "Rating": 4.40
    }
]
# print(highest_rated(books))


#! Problem 8: Index Value Map 
def index_to_value_map(lst):
    result = {}
    for i in range(len(lst)):
        result[i] = lst[i]
    return result

lst = ["apple","banana","cherry"]

print(index_to_value_map(lst))

