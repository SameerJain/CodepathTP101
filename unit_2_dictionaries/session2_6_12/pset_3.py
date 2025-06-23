
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
    if it has been found
        if it he idx is less than the min index we swap 
"""
def find_min_index_of_repeating(nums: list[int]) -> int | None:
    found_nums = {}
    min_index = None
    for idx, ele in enumerate(nums):
        if ele not in found_nums:
            found_nums[ele] = idx
        el:
            return found_nums[ele]
    
    return min_index

nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [ 5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))
print(find_min_index_of_repeating(nums2))
print(find_min_index_of_repeating(nums3))

#! Problem 7: Target Sum 
def two_sum(nums,target):
    
