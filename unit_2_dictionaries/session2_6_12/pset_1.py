
# #!? Problem 1: Cast Vote
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


# #!? Problem 2: Keys in Common
# '''
# init result list

# return result
# '''
# def common_keys(dict1,dict2):
#     return list(dict1.keys() & dict2.keys())

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)


#!? Problem 3: Highest Priority Task
'''
var highesttask
var highesttaskvalue
iterate thru list
    if the value is greater than current highest
        set the new highest 
        update the key 
    else if its the same
        update the key to the lower one alphabetically using min()
'''


def get_highest_priority_task(tasks):
    
    highest_task_value = 0
    highest_task = ""
    
    for key, value in tasks.items():
        if value > highest_task_value:
            highest_task_value = value
            highest_task = key
        elif value == highest_task_value:
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

#! Problem 4: Frequency Count

'''
create result dictionary 
iterate thru keys 
insert freqs using .get
return result
'''
def count_occurrences(nums):






#! Problem 5: Find Majority Element


def find_majority_element(elements):
    pass

#! Problem 6: Has Duplicates


def hasDuplicates(nums, k):
    pass

#! Problem 7: Make Pairs


def divideList(nums):
    pass
