
#! Problem 1: Return Book
def return_book(title,library):
    # library[title] = library.get(title,0) + 1
    
    if title in library:
        library[title] += 1
    else:
        library[title] = 1
    return library

library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
# print(updated_lib)

updated_lib = return_book("The Giver", library)
# print(updated_lib)


#! Problem 2: Dictionary Difference
"""
iterate thru d1
    if the key is not in d2
        we add the key and the value into result
    if the key is but the value is not equal
        we add to the result the same way  
"""
def dict_difference(d1,d2):
    result = {}
    for key,value in d1.items():
        if key not in d2 or key in d2 and d2[key] != value:
            result[key] = value
    return result

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}

# print(dict_difference(d1,d2))

#! Problem 3: Take from stock
"""
if item name in items
    if the current value is less than the quantity to remove
        error: not in inventory
    else
        subract the value by the given amount
else 
    error: not in inventory
"""
def pop_stock(items,item_name,quantity):
    if item_name in items:
        if items[item_name] < quantity:
            return "Not enough stock"
        else:
            items[item_name] -= quantity
            return items
    else:
        return "Item does not exist"

items = {"chocolate": 20, "candy": 5, "chips": 10}

resultA = pop_stock(items, "candy", 2)
resultB = pop_stock(items, "candy", 5)
resultC = pop_stock(items, "lollipops", 5)
resultD = pop_stock(items, "chocolate", 5)

# print(resultA)
# print(resultB)
# print(resultC)
# print(resultD)

#! Problem 4: Group by frequency 
"""
do frequncy count

create new dict
iterate thru new dict
    append keys based on their value 
"""
def group_by_frequency(lst):
    freqs = {}
    for ele in lst:
        freqs[ele] = freqs.get(ele,0) + 1
    result = {}
    for key, value in freqs.items():
        result[value] = result.get(value,[]) + [key]
    
    return result
    
lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
# print(group_by_frequency(lst))

#! Problem 5: No duplicates Allowed
"""
iterate and store frequencies in a key

create a list and append all the keys from the dict 
"""
def remove_dupliucates_from_front(nums):
    freqs = {}
    for num in nums:
        freqs[num] = freqs.get(num,0) + 1
    result = []
    for key in freqs.keys():
        result.append(key)
    return result

#? What is going on here? This is from answer key but we dont have to append twice
def remove_duplicates_from_front2(nums):
    frequency_map = {}
    for num in nums:
        frequency_map[num] = True
    last_occurrences = []
    for num in nums:  # Reverse iterate
        if frequency_map[num]:
            last_occurrences.append(num)
            frequency_map[num] = False
    return last_occurrences  # Reverse again to original order

nums = [6,5,3,5,2,8,3]

# print(remove_duplicates_from_front2(nums))

#! Problem 6: First Repeating Element 
"""
create a found dict 
create a min_index
iterate thru the list
    if the num isnt in the dict, add it, add the value as the key
    if it has been found before
        if its the first duplicate number found 
            we set min_index from none to the the first duplicates idx from the beginning 
        else if theres already a found index
            if the first nums idx is less than the min index
                we swap out min_index for the new one 
"""
# def find_min_index_of_repeating(nums: list[int]) -> int | None:
#     found_nums = {}
#     min_index = None
#     print(f"Input list: {nums}")
#     for idx, ele in enumerate(nums):
#         if ele not in found_nums:
#             found_nums[ele] = idx
#             print(f"New element added: {ele}, idx: {idx}, found_nums[ele]: {found_nums[ele]}")
#         else:
#             if min_index == None:
#                 min_index = found_nums[ele]
#                 print(f"Setting min_index to {found_nums[ele]}.idx: {idx}, found_nums[ele]: {found_nums[ele]}")

#             elif found_nums[ele] < min_index: 
#                 print(f"Setting new min_index. ele: {ele}, idx: {idx} found_nums[ele]: {found_nums[ele]}. Current min_index: {min_index}")
#                 min_index = found_nums[ele]
#                 print(f"new min_index: {min_index}")
#     print("Final min_index:")
#     return min_index

# nums = [5, 6, 3, 4, 3, 6, 4]
# nums2 = [5, 6, 3, 4]
# nums3 = [ 5, 6, 2, 4, 3, 4, 3]
# print(find_min_index_of_repeating(nums))
# print(find_min_index_of_repeating(nums2))
# print(find_min_index_of_repeating(nums3))

#! Problem 7: Target Sum 
"""
create a compliment dictionary
iterate thru nums 
    comp = target nums[i]
    if comp in dict
        return idx of the comp its tied to, and current number
    store comp in dict tied to idx
"""
def two_s2um(nums: list[int],target: int) -> tuple[int,int] | None:
    compliments = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if nums[i] in compliments.keys():
            return [compliments[nums[i]],i]
        compliments[comp] = i
    return None

def two_sum(nums: list[int], target):
    compliments = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in compliments:
            return [compliments[diff],i]
        compliments[nums[i]] = i
    # print(nums, target,compliments)
    


nums = [2,7,11,15]
q_1 = two_sum(nums,9)
q_2 = two_sum(nums,18)

nums2 = [3,3]
q_3 = two_sum(nums2,6)

print(q_1)
print(q_2)
print(q_3)

