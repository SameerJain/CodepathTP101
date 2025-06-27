def get_element_at_index(lst, index):
    if index < 0 or index >= len(lst):
        return None  # Handle out-of-bounds cases
    return lst[index]

# time complexity: O(1)
# space complexity: O(1)
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
#time complexity: O(N)
#Space compexity: O(1)

"""
Given a string s, determine if it can become a palindrome by removing at most one character.
A palindrome is a word, phrase, or sequence that reads the same backward as forward.
"""



def valid_palindrome(s):
    if len(s) == 1:
        return False
    while left < right:
        if s[left] != s[right]:
                new_str = new_str[:left] + new_str[left] 
                valid_palindrome(new_str,left,right)
        left += 1
        right -= 1
    return True

"""
Input: s = "aba"
Output: True
"""
s = "abcdaa"
print(valid_palindrome(s,0,len(s)- 1))

