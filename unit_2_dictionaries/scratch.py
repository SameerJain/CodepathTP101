
'''
if name is already a key
    add 1
else
    insert key
    
return votes
'''

# def cast_vote(votes,candidate):
#     if candidate in votes:
#         votes[candidate] += 1
#     else:
#         votes[candidate] = 1
#     return votes

# votes = {"Alice": 5, "Bob": 3}
# cast_vote(votes, "Alice")
# print(votes)
# cast_vote(votes, "Gina")
# print(votes)


# {"Alice": 6, "Bob": 3}
# {"Alice": 6, "Bob": 3, "Gina": 1}

# def common_keys(dict1, dict2):
#     return list(dict1.keys() & dict2.keys())


# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)








'''
find task with highest priority

use max() to get highest priority
'''
def get_highest_priority_task(tasks):
    
    highest_priority_num = 0
    highest_task = ""
    for key, value in tasks.items():
        if value > highest_priority_num:
            highest_priority_num = value
            highest_task = key
        elif value == highest_priority_num:    
            highest_task = min(highest_task,key)
            
    tasks.pop(highest_task)
    
    return highest_task

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)

def best_breakout_room(room):
    print("The best breakout room today was",room)

best_breakout_room(68)

