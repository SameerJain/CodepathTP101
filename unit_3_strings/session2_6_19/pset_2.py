
#! (DONE) Problem 1: String to Integer 
"""
iterate thru string
append to list as an int
return
"""
def string_to_integer_mapping(s):
    result = []
    for char in s:
        result.append(int(char))
    return result

s="12345"
# print(string_to_integer_mapping(s))


#! (DONE) Problem 2: Delete Minimum
"""
sort the arr
remove one by one and return
"""
"""
while the minimum number is not empty 
get remove it mins using min

"""
def delete_minimum_elements(nums):
    result = []
    nums.sort()
    for num in nums.copy():
        nums.remove(num)
    print(nums)
    return result

# nums = [5,3,2,8,3,1]
# removed_lst = delete_minimum_elements(nums)
# print(removed_lst)

#! (DONE) Problem 3: Longest Common Prefix     
"""
if the string is empty return empty string

find the shortest string

iterate thru list
    if you find a char that doesnt equal to the shortest
        return what you have found
"""

def longest_common_prefix0(strings):
    
    if not strings:
        return ''

    min_len = float('inf')         
    min_string = ''
    for string in strings:
        min_len = min(min_len,len(string))

    for i in range(1,len(min_string)):
        for c in strings:
            if min_string[:i] != c[:i]:
                return min_string[:i-1]
    return ''

"""
New version:

if the string is empty we return an empty string
get the min string length and the corresponding string

iterate thru that string
    until its not the same we return it
"""

def longest_common_prefix(strings):
    if not strings:
        return ''

    min_string = strings[0]
    for string in strings:
        if len(string) < len(min_string):
            min_string = string
    
    for i in range(1,len(min_string)):
        for string in strings:
            if min_string[:i] != string[:i]:
                return min_string[:i-1]
    return ''

strings = ["flower", "flow", "flight"]
common_string = longest_common_prefix(strings)
# print(common_string)

strs = ["dog", "racecar", "car"]
common_str = longest_common_prefix(strs)
# print(common_str)

#! Problem 4: Consecutive Characters
def count_consecutive_characters1(str1):
    count = 1
    max_count = 1
    for i in range(len(str1)-1):
        if str1[i] != str1[i+1]:
            max_count = max(max_count,count)
            count = 1
        else:
            count += 1
    max_count = max(max_count,count)
    return max_count

def count_consecutive_characters(s):
    if not s:
        return 0
    max_count = 1
    current_count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1
    return max_count

str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
# print(count) # 4

str2 = "abcde"
count2 = count_consecutive_characters(str2)
# print(count2) # 1

#! Problem 5: Partition Labels 
"""
if empty s ret 0
clean string to all lowercase

use map to get first idx value 
then if its there already, 
    we 

"""

def partition_label(s):
    # If string is empty, return empty list
    if not s:
        return []
    # Clean input to only allow lowercase
    s = s[:].lower()
    #Get the last idx of every char
    last_idxs = {}
    for i, char in enumerate(s):
            last_idxs[char] = i
    
    # set up creating the partition
    partition = []
    start = 0
    end = 0

    # Do the partitioning
    for i, char in enumerate(s):
        end = max(end,last_idxs[char])
        if i == end:
            partition.append(end - start + 1)
            start = i + 1
    return partition

s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))

s2 = "abcabcbadefffeda"
print(partition_label(s2))


#! Problem 6: Interleave Lists

"""
iterate using the same pointer
get the length of both 
set i to be the length of the larger string
iterate
""" 

def interleave_lists(lst1,lst2):
    
    bigger_list = max(len(lst1),len(lst2))
    result = []
    for i in range(bigger_list):
        if i < len(lst1):
            result.append(lst1[i])
        if i < len(lst2):
            result.append(lst2[i])

    return result

# print(interleave_lists([1,2,3,4,5],[4,3]))
# lst1 = [1,2,3,4]
# lst2 = [10,20]
# inter_lst = interleave_lists(lst1,lst2)
# print(inter_lst)