
#! Problem 1: Perfect Number 
"""
store divisors in list 
if sum of list matches, return true or false otherwise
"""
def is_perfect_number(n):
    divisors = []
    i = n - 1
    while i > 0:
        if n % i == 0:
            return  
        i -= 1
    pass

#! Problem 2: 2-Pointer Palindrome
"""
Set a pointer on each end 
swap them on at a time
only iterate for half of the list 
"""
def is_palindrome(s):
    left,right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
s = "amanaplanacanalpanama"
s2 = "helloworld"

# print(is_palindrome(s))
# print(is_palindrome(s2))

#! Problem 3: Evaluate Palindrome 
def is_palindrome(s):
    reverse = s[::-1]
    return reverse == s

# Time: O(n/2) or O(n)
# Space: O(1)

# Time: O(n)
# Space: (n)

#! Problem 4: Making Palindromes 
#? test case variables are messed up
"""

"""
def make_palindrome0(s):
    left, right = 0, len(s) - 1
    new_str = list(s)
    while left < right:
        smaller_val = chr(min(ord(s[left]),ord(s[right])))
        new_str[left], new_str[right] = smaller_val, smaller_val
        left += 1
        right -= 1
    
    return ''.join(new_str)

def make_palindrome(s: str) -> str:
    left, right = 0, len(s) - 1
    final_str = list(s)
    while left < right:
        if s[left] < s[right]:
            final_str[right] = s[left]
        else:
            final_str[left] = s[right]
        left += 1
        right -= 1
    return ''.join(final_str)
s = "egcfe"
s_pal = make_palindrome(s)
# print(s_pal)
# s_pal == "efcfe"
# The min number of operations to make s a palindrome is 1 by changing `f` to `g`
# another palindrome possible is "egcge", but it is not lexicographically smaller


s = "abcd"
s_pal = make_palindrome(s)
# print(s_pal)
# s_pal == "abba"
# The min number of operations to make s a palindrome is 2 by changing `c` to `b` and `d` to `a`
# a palindrome cannot be created in 1 operation


s = "seven"
s_pal = make_palindrome(s)
# print(s_pal)
# s_pal == "neven"
# The min number of operations to make s a palindrome is 1 by changing `s` to `n`
# to get a palindrome that is lexographically smaller, it would take more operations


#! Problem 5: Reverse Vowels 
def reverse_vowels(s):
    vowels = ['a','e','i','o','u']
    new_str = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -=1 
        else:
            new_str[left], new_str[right] = new_str[right], new_str[left]
            left += 1
            right -=1 
    return ''.join(new_str)

# s1 = "hello"
# rev_s1 = reverse_vowels(s1)
# print(rev_s1)

# s2 = "leetcode"
# rev_s2 = reverse_vowels(s2)
# print(rev_s2)


#! Problem 6: 2-Pointer Remove Element 
def removeElement(nums,val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i, nums[:3]

nums = [5, 4, 4, 3, 4, 1]
nums_len = removeElement(nums, 4)
print(nums) # same list
print(nums_len)
