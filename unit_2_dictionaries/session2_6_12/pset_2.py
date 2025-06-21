
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
print(dict_intersection2(d1,d2))

#! Problem 3: Filter by Price
"""

"""
def remove_items_below_price(items, price_threshold):
    pass

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)





#! Problem 4: Find Odd Occurrences
def find_odd_occurrences(nums):
    pass

#! Problem 5: Find Mode 
def find_mode(lst):
    pass

#! Problem 6: How many smaller 
def smallerNumbersThanCurrent(nums):
    pass

#! Problem 7: Good Pairs 
def numIdenticalPairs(nums):
    pass

