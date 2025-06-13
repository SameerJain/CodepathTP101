
#! Problem 1: Cast Vote
def cast_vote(votes,candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
#! Problem 2: Keys in Common
'''
init result list 

return result
'''
def common_keys(dict1,dict2):
    pass

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)
#! Problem 3: Highest Priority Task
def get_highest_priority_task(tasks):
    pass

#! Problem 4: Frequency Count
def count_occurrences(nums):
    pass

#! Problem 5: Find Majority Element
def find_majority_element(elements):
    pass

#! Problem 6: Has Duplicates
def hasDuplicates(nums,k):
    pass

#! Problem 7: Make Pairs
def divideList(nums):
    pass


