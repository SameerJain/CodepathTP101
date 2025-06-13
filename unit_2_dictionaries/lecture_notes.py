
#! Group Anagrams 

'''
iterate thru the list of strings    
    sort the word
    set that sorted word as the key
    append that same sorted word for the same key
return the list using the values 

if we are using normal dictionaries we have to check if the list for the key has been initialized, otherwise we can just add, but if we are using a defaultdict we can just ignore that 
'''

from collections import defaultdict
def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return list(anagrams.values()) 

def group_anagrams2(words):
    anagrams = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())
words = ["eat","tea","tan","ate","nat","bat"]

# print(group_anagrams2(words))

'''
init result 
iterate thru list
    if item key not in result
        add it to result 
    loop thru items in tuple starting at idx 1

return result 
'''
def count_by_category(items):
    result = {}    
    for item in items:
        for item_count in item:
            if item_count == item[0]:
                if item_count not in result:
                    result[item_count] = 0
            else:
                result[item[0]] += 1
    return result

items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]

for cat, val in items:
    print(cat,val)
