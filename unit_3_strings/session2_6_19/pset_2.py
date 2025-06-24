
#! Problem 1: String to Integer 
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

nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)

#! Problem 2: Delete Minimum
def delete_minimum_elements(nums):
    pass

strings = ["flower","flow","flight"]
common_string = longest_common_prefix(strings)
print(common_str)

#! Problem 3: Longest Common Prefix 
def longest_common_prefix(strings):
    pass

str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
print(count)

str2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)

#! Problem 4: Consecutive Characters
def count_consecutive_characters(str1):
    pass 

s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))
print(count)
s2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)

#! Problem 5: Partition Labels 
def partition_label(s):
    pass

# s1 = "ababcbacadefegdehijhklij"
# print(partition_label(s1))

# s2 = "abcabadefffeda"
# print(partition_label(s2))


#! Problem 6: Interleave Lists 
def interleave_lists(lst1,lst2):
    pass

# lst1 = [1,2,3,4]
# lst2 = [10,20]
# inter_lst = interleave_lists(lst1,lst2)
# print(inter_lst)