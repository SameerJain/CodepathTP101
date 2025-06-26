
#! (DONE) Problem 1: Remove Vowels 
def remove_vowels(s):
    result = []
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    for char in s:
        if char not in vowels:
            result.append(char)

    return ''.join(result)

# s = "Hello World"
# new_string = remove_vowels(s)
# print(new_string)

#! Problem 2: Missing Integer
"""
if nums is empty return empty list 
iterate thru list till the last one
    if the number is not more than one before it 
    return
return the last number + 1
"""
def find_missing_positive(nums):
    if not nums:
        return None
    for i in range(len(nums) - 1):
        if nums[i+1] > nums[i] + 1:
            return nums[i] + 1
    return nums[-1] + 1 


# print(find_missing_positive([]))

# num1 = [1,2,3,5,6,10]
# print(find_missing_positive(num1))

# num2 = [1,2,3,4,5]
# print(find_missing_positive(num2))


#! Problem 3: Word Follows Pattern 
"""
if either pattern or s is empty return error
seperate sentence into list 
if list length is diff than string length return error
iterate thru list
    assign string letter to word
        if the key isnt in the map
            if the value isnt in the map
                add to map
            else if the value is in map, return false
        else if the key is paired already
            return false
return true 
"""
def wordPattern0(pattern,s):
    if len(pattern) < 1 or len(s) < 1:
        return "Invalid Input of size 0"

    s_list = s.split()

    if len(s_list) != len(pattern):
        return False
    
    pattern_map = {}

    for i in range(len(s_list)):
        if pattern[i] not in pattern_map.keys():
            if s_list[i] not in pattern_map.values():
                pattern_map[pattern[i]] = s_list[i]
            else:
                return False
        elif pattern_map[pattern[i]] != s_list[i]:
            return False
    return True

def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    pattern_map = {}
    for index, word in enumerate(words):
        p_char = pattern[index]
        # Did we already use this char for another word?
        if p_char not in pattern_map:
            pattern_map[p_char] = word
        elif pattern_map[p_char] != word:
            return False

    # We couldn't find any mis-matches
    return True

# pattern1 = "abba"
# s = "dog cat cat dog"
# print(wordPattern(pattern1,s))
# s2 = "dog cat cat fish"
# print(wordPattern(pattern1,s2))

# pattern2 = "aaaa"
# s3 = "dog cat dog cat"
# print(wordPattern(pattern2,s3))
# s4 = "dog dog dog dog"
# print(wordPattern(pattern2,s4))

#? These test cases are not supported in the answer key
# pattern3 = "ab"
# s5 = "dog dog"
# print(wordPattern0(pattern3,s5))

# pattern4 = "abc"
# s6 = "dog dog fish"
# print(wordPattern0(pattern4,s6))

#! Problem 4: Binary Substrings 
"""
For the length of the substring from the second idx

create string list to test for answers
create a count that has the nmber of zeroes and ones 
if the count of each is volated
    and an increase to the final sum count 
"""

"""
we use the fact that the number of binary substrings in the run of the sequence is equal to the min of zeros and ones 
"""

def binary_substrings_count0(s):
    prev_run_length = 0
    curr_run_length = 1
    count = 0
    subtring_list = []
    for i in range(1, len(s)):
        print(f"prev: {prev_run_length}, curr: {curr_run_length}")
        if s[i] == s[i-1]:
            curr_run_length += 1
        else:
            prev_run_length = curr_run_length
            curr_run_length = 1
        if prev_run_length >= curr_run_length:
            count += 1
            
            subtring_list.append(s[:i])
    return count, subtring_list

def binary_substrings_count(s):
    prev_length = 0
    curr_length = 1

    count = 0

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            curr_length += 1
        else:
            prev_length = curr_length
            curr_length = 1
        if prev_length >= curr_length:
            count += 1
    return count

# s = "00110011"
# print(binary_substrings_count(s))

# s2 = "10101"
# print(binary_substrings_count(s2))

# s3 = "1111"
# print(binary_substrings_count(s3))


#! Problem 5: Exclusive Elements 
"""
get the elements that are in lst1 but not lst2
get the elements that are in lst2 but not lst1
"""

def exclusive_elements(lst1,lst2):
    result = []

    for num in lst1:
        if num not in lst2:
            result.append(num)

    for num in lst2:
        if num not in lst1:
            result.append(num)
    return result

# lst1 = [3,1,8,10]
# lst2 = [4,5,3,7,8]
# excl_lst = exclusive_elements(lst1, lst2)
# print(excl_lst)




#? The given answer key hase some bugs
#! Problem 6: Flowerbed
"""
init count
iterate thru the list
    if number is 0:
        if not start
            if space before is 0
                swap to 1
        if space after is 0
            if not end
                swap to 1

return count >= n
""" 
def can_place_flowers(flowerbed,n):
    count = 0
    can_place_before = False
    can_place_after = False
    for i in range(len(flowerbed)):
        can_place_before = False
        can_place_after = False
        # print(f"Start of iteration. flowerbed[i]: {flowerbed[i]}, i: {i}")
        if flowerbed[i] == 0:
            if i > 0:
                if flowerbed[i-1] == 0:
                    can_place_before = True
            if i < len(flowerbed) - 1:
                if flowerbed[i+1] == 0:
                    can_place_after = True
            if (can_place_before == True) and (can_place_after == True):
                # print("Can place flower")
                flowerbed[i] = 1
                count +=1
        # print(f"End of iteration. i: {i}, canplacebefore: {can_place_before}, canplaceafter: {can_place_after} count: {count}")
        # print(flowerbed)
    return count >= n

flowerbed = [1,0,0,0,1]
approved2 = can_place_flowers(flowerbed, 2)
print(approved2)     
approved1 = can_place_flowers(flowerbed, 1)