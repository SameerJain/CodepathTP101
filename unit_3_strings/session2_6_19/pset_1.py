#This is a comment
#! Problem 1: Sum of Strings 
def sum_of_number_strings(nums):
    pass

#! Problem 2: Remove Duplicates
def remove_duplicated(nums):
    pass

#! Problem 3: Reverse Letters
def reverse_only_letters(s):
    pass

#! Problem 4: Longest Uniform Substring 

'''
iterate thru all of it 
create iterator
length substring
if the two pointers are the same, we add + 1
if they are different, we reset the length of the substring

return the max length 
'''

def longest_uniform_substring(s):
    curr_length = 1
    max_length = 1

    for i in range(len(s) -1):
        if s[i] == s[i+1]:
            curr_length += 1
            max_length = max(max_length,curr_length)
        else:
            curr_length = 1
      
    return max_length

s1 = "aaaaaaaaaaaaaaaaabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)

#! Problem 5: Teemo's Attack 
def find_poisoned_duration(time_series,duration):
    pass

#! Problem 6: Sum Unique Elements 
def sum_of_unique_elements(lst1,lst2):
    pass

