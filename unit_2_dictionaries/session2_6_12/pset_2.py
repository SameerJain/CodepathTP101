
#! Problem 1: Update Score
"""
insert name if not there already with score
"""
def update_score(scores,players,points):
    # Alternate way: 
    # scores[players] = scores.get(players,0) + points 
    
    if players in scores:
        scores[players] += points
    else:
        scores[players] = points
    return scores
    
scores = {"Alice": 100,"Bob": 90}

# update_score(scores, "Alice", 10)
# print(scores)
# update_score(scores, "Calvin", 20)
# print(scores)
# update_score(scores, "Calvin", 5)
# print(scores)

#! Problem 2: Dictionary Intersection 

def dict_intersection(d1,d2):
    return list(d1.items() & d2.items())

"""
init result dict 
iterate thru d1
if the key and value are the same
    append both together to result dict
return result 
"""
def dict_intersection2(d1: dict[str,int],d2: dict[str,int]) -> list[int]:
    result = {}
    for key, value in d1.items():
        if key in d2 and d2[key] == value:
            result[key] = value
    return result

d1 = {'a': 1,'b': 2,'c': 3}
d2 = {'b': 2,'c': 4}
# print(dict_intersection2(d1,d2))

#! Problem 3: Filter by Price
"""
init removed items
iterate thru items
    if key's val < threshold
        add to removed items
        remove from orignal dict
return removed items 
"""
def remove_items_below_price(items, price_threshold):
    removed = []
    for key, value in items.items():
        if value < price_threshold:
            removed.append(key)
        
    if not removed:
        return None

    for obj in removed:
        items.pop(obj)

    return removed

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
# print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
# print(removed_list_two)





#! Problem 4: Find Odd Occurrences
"""
Create Fequency dict 

iterate and get frequencies 

iterate thru dict
    if key's val is odd
        add to result dict
    if the result dict is greater than size 3:
        return error as their should only be 2 values
"""
def find_odd_occurrences(nums):
    freqs = {}
    result = []

    for num in nums:
        freqs[num] = freqs.get(num,0) + 1
    
    for key,value in freqs.items():
        if value % 2 == 1:
            result.append(key)
        if len(result) > 2:
            raise ValueError(f"There can only be 2 unique values. Values: {result}")
    
    return result
nums = [1,4,2,3,2,3,3,4,4,4]
odd_list = find_odd_occurrences(nums)
# print(odd_list)

#! Problem 5: Find Mode 
"""
do a freq count with dict

iterate and find the highest key val, store in list

iterate again to find which one came first if thats the case
"""

def find_mode(lst: list[int]) -> int:
    freqs = {}
    highest_num = 0 
    highest_nums = []
    for num in lst:
        freqs[num] = freqs.get(num,0) + 1

    for key, value in freqs.items():
        if value >= highest_num:
            if value > highest_num and highest_nums:
                highest_nums.pop(-1)
            highest_num = key
            highest_nums.append(key)
    
    for num in lst:
        if num in highest_nums:
            return num

def find_mode2(lst): #? Given solution does not have edge case of item appearing first 
    frequency_map = {}
    max_count = 0
    most_frequent = None
    for num in lst:
        if num in frequency_map:
	        frequency_map[num] += 1
        else:
	        frequency_map[num] = 1
        if frequency_map[num] > max_count:
                max_count = frequency_map[num]
                most_frequent = num
    return most_frequent

lst = [1,2,3,2,3,3,5,4,4,4,4,5,5,5]
mode = find_mode2(lst)
# print(mode)


#! Problem 6: How many smaller 
"""
init result dict

iterate thru nums
    if the current val is not the key and smaller than the current val
        we add + 1 to its value in result dict
return result.values()
"""
def smallerNumbersThanCurrent(nums):
    smaller_than = []

    for num1 in nums:
        less_amount = 0
        for num2 in nums:
            if num1 == num2:
                continue
            if num2 < num1:
                less_amount += 1
        smaller_than.append(less_amount)
    
    return smaller_than

nums = [6,1,2,2,3]
#print(smallerNumbersThanCurrent(nums))

#! Problem 7: Good Pairs 
"""
count the frequency of each number

get the ceiling amount of each 
"""
def numIdenticalPairs(nums):
    pass

testlist = ()
lst = [2,1]
lst2 = [2,1]
testlist.append(lst)
print((testlist))

