
#! Problem 1: Calling Mississippi
def count_mississippi(limit):
    for num in range(1, limit):
        print(f"{num} mississippi")


# count_mississippi(6)

#! Problem 2: Swap Ends


def swap_ends(my_str):

    if len(my_str) <= 1:
        return my_str

    new_string = []
    i = 0
    for c in my_str:
        if i == 0:
            new_string.append(my_str[-1])
        elif i == len(my_str) - 1:
            new_string.append(my_str[0])
        else:
            new_string.append(c)
        i += 1
        # print(f"new_string: {new_string}")
    return ''.join(new_string)


def swap_ends2(my_str):
    return my_str[-1] + my_str[1:-1] + my_str[0]

# my_str = "bbagqwerjfhnkiwehrfnjuiwqrheiwhrl"

# print(swap_ends2(my_str))


#! Problem 3: Is Pangram

def is_pangram(my_str):
    letter_freq = {}
    new_str = my_str.lower()
    for c in new_str:
        letter_freq[c] = letter_freq.get(c, 0) + 1
    if len(letter_freq.keys()) < 26:
        return False
    return True


my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

str2 = "The dog jumped"
# print(is_pangram(str2))
#! Problem 4: Reverse String

'''
iterate thru list reversed
append to list 
join into string
'''
def reverse_string(my_str):
    reversed_string = []
    for c in my_str[::-1]:
        reversed_string.append(c)
    return ''.join(reversed_string)
# print(reverse_string("Hello"))

#! Problem 5: First Unique
'''
iterate thru string 
    store frequencies in a hashmap as long as they havent shown up before 
if the result map ends up being empty, we return -1 error

iterate thru string again 
    if the current letter is in map, return idx of current letter   
'''

def first_unique_char(my_str):
    freqs = {}
    for c in my_str:
        freqs[c] = freqs.get(c,0) + 1
    
    for i in range(len(my_str)):
        if freqs[my_str[i]] == 1: 
            return i
    return -1

# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))

#! Problem 6: Minimum Distance

'''
iterate words and counter 
if word 1 is found, reset counter to 0
if word 2 is found, return counter 


'''

def min_distance0(words, word1, word2):
    counter = 0
    for word in words:
        counter += 1
        if word == word1:
            counter = 0
        elif word == word2:
            return counter 
    return None

"""
set lists for word 1 and word 2
iterate thru words
    if word is word 1
        append index
        if word 1 has been found already
        get the distance using abs()
        set min distance to new min
    do same for word 2 
return None

"""
def min_distance(words,word1,word2):
    word1_idxs = []
    word2_idxs = []
    min_dist = float('inf')
    for idx, word in enumerate(words):
        if word == word1:
            word1_idxs.append(idx)
            if word2_idxs:
                dist = abs(word1_idxs[-1] - word2_idxs[-1])
                min_dist = min(min_dist,dist)
        if word == word2:
            word2_idxs.append(idx)
            if word1_idxs:
                dist = abs(word2_idxs[-1] - word1_idxs[-1])
                min_dist = min(min_dist,dist)
    
    return min_dist if min_dist != float('inf') else None

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)    
