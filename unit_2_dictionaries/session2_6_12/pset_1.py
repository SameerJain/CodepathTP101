
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

# tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# print(tasks)

#! Problem 4: Frequency Count

'''
create result dictionary 
iterate thru keys 
insert freqs using .get
return result
'''
def count_occurrences(nums_array):
    result = {}
    for idx, ele in enumerate(nums_array):
        result[ele] = result.get(ele,0) + 1
    
    return result

def count_occurrences3(nums_array):
    result = {}
    for num in nums_array:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1

    return result

nums_array = [1, 2, 2, 3, 3, 3, 4]

# print(count_occurrences3(nums_array))


#! Problem 5: Find Majority Element
"""
get the size of array 
iterate thru the list 
    count the frequency of each number
    if the frequency is equal to ceiling of n/2, return the key
    or you can do if its greater than n/2, return the key its the same thing
return None 
"""


def find_majority_element(elements):
    result = {}

    for ele in elements:
        result[ele] = result.get(ele,0) + 1
        if result[ele] > len(elements) / 2:
            return ele
    return None

elements = [2,2,1,1,1,2,2]
# print(find_majority_element(elements))

#! Problem 6: Has Duplicates

"""
create frequency dict 
iterate thru list only for specified amount using range(0,k-1)
if the key's value is greater than 1, return True
return false at end
"""

def hasDuplicates(nums_array, k):
    freqs = {}
    for i in range(0,k):
        val = nums_array[i]
        freqs[val] = freqs.get(val,0) + 1
        if freqs[val] > 1:
            return True
    return False

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = hasDuplicates(nums, 3)
# print(check1)
check2 = hasDuplicates(nums, 5)
# print(check2)

#! Problem 7: Make Pairs

"""
iterate thru and get frequency of numbers in dict
iterate thru values and if any of them are odd, we return false
"""
def divideList(nums: list[int]) -> bool:
    freqs = {}
    
    for num in nums:
        freqs[num] = freqs.get(num,0) + 1

    for value in freqs.values():
        if value % 2 == 1:
            return False
    
    return True

nums = [3,2,3,2,2,2]
num2 = [1,2,3,4]
"""

"""
print(divideList(nums))
print(divideList(num2))