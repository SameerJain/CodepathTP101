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



def valid_palindrome0(s):
    if len(s) == 1:
        return False
    while left < right:
        if s[left] != s[right]:
                new_str = new_str[:left] + new_str[left] 
                valid_palindrome(new_str,left,right)
        left += 1
        right -= 1
    return True

def valid_palindrome(s):
    left = 0 
    right = len(s) - 1

    def is_palindrome(left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            return True

    while left < right:
        if s[left] != s[right]:
            return is_palindrome(left+1,right) or is_palindrome(left,right-1)
        left += 1
        right -= 1
    return True
    
s = "abcbaa"
print(valid_palindrome(s))

"""
0 1 2 3 4 5
a b c d a a

pass 1: same
pass 2: mismatch
    (2,4)
    (1,3)

"""

"""
Input: s = "aba"
Output: True
"""


