
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

create_dictionary(keys,values)

#! Problem 3: Print Pair 
def print_pair(dictionary,target):
    pass

dictionary = {"Spongebob": "Squarepants","Squidward":"Tentacles","Patrick":"Star"}

print_pair(dictionary,"Patrick")
print_pair(dictionary,"Plankton")
print_pair(dictionary,"Spongebob")
#! Problem 4: Keys Versus Values
def keys_v_values(dictionary):
    pass

dictionary1 = {1:10,2:20,3:30,4:40,5:50,6:60}
greater_sum = keys_v_values(dictionary)
print(greater_sum)

dictionary2 = {100:10,200:20,300:30,400:40,500:50,600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

#! Problem 5: Restock Inventory
def restock_inventory(current_inventory,restock_list):
    pass

current_inventory = {
    "appples":30,
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
    pass

report_card = {"Math":"A","Science":"C","History":"A","Art":"B","English":"B","Spanish":"A"}

# print(calculate_gpa(report_card))

#! Problem 7: Best Book 
def highest_rated(books):
    pass

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
    pass

lst = ["apple","banana","cherry"]

# print(index_to_value_map(lst))

