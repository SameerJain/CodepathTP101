
#! (DONE) Problem 1: Highest Exponent 
def find_highest_exponent(base,limit):
    i = 0
    product = base * i

    while product < limit:
        i += 1
        product = base ** i

    return i - 1

# exp = find_highest_exponent(2,100)
# print(exp)

# exp2 = find_highest_exponent(3,5)  
# print(exp2)

#! Problem 2: 2-Pointer Target Sum 

#? We have to sort the list first but the problem statement is incorrect and gives an unsorted list
"""
sort the list
if the 2 numbers add up to target return
if sum is less move right down
if sum is more move left up
""" 
def two_sum(nums,target):
    
    if not nums:
        return None

    nums.sort()
    
    left, right = 0, len(nums) - 1

    while left < right:
        sum_val = nums[left] + nums[right]
        if sum_val == target:
            return [left,right]
        elif sum_val > target:
            right -= 1
        else:
            left += 1
    return []

# nums = [2,7,11,15,7]
# # [2,7,7,11,15]
# sol1 = two_sum(nums,9)
# print(sol1)

# sol2 = two_sum(nums,18)
# print(sol2)

#? This is also wrong given the problem statement 
#! Problem 3: Evaluate Two SUm 
def two_sum_p3(nums,target):
    prev_map = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff],i]
        prev_map[nums[i]] = i

# Two pointer Method
# Time: O(nlogn) or O(n) if sorted
# Space: O(1)

#Hash Map Method
# Time: O(n)
# Space: o(n)

#! Problem 4: 2-Pointer Reverse Letters 
def reverse_only_letters(s):
    left, right = 0, len(s) - 1
    new_str = list(s) 
    while left < right:
        if s[left].isalpha() == False:
            left += 1
        elif s[right].isalpha() == False:
            right -= 1
        else:
            new_str[left], new_str[right] = new_str[right], new_str[left]
            left += 1
            right -= 1
    return ''.join(new_str)
    

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)


#! Problem 5: Reverse Prefix 
"""
iterate to find first occurence of ch
if not in list return does not exist

make str as list so we can modify 
set up 2 pointers where right pointer is the first instance
swap 
"""
def reverse_prefix(word,ch):
    left, right = 0, None
    new_str = list(word)

    for i in range(len(word)):
        if word[i] == ch:
            right = i
            break

    if not right:
        return word

    while left < right:
        new_str[left], new_str[right] = new_str[right], new_str[left]
        left += 1
        right -= 1
    
    return ''.join(new_str)
    


# word = "abcdefd"
# rev_word = reverse_prefix(word,"d")
# print(rev_word)

# word2 = "helloworld"
# rev_word2 = reverse_prefix(word2,"w")
# print(rev_word2)

# word3 = "xyzxyz"
# rev_word3 = reverse_prefix(word3,"a")
# print(rev_word3)



#! Problem 6: Squash Spaces 
"""
create empty char list
iterate thru s
    if is whitespace and before isnt char
        continue
    else add to char list
return combined list



if its a char 
    we add to list
else if space
    if we are at first idx or one before is space
        cont
    else
        add  

"""

def squash_spaces(s):
    char_list = []

    for i in range(len(s)):
        if s[i].isalpha():
            char_list.append(s[i])
        elif s[i] == ' ':
            if i == 0 or s[i-1] == ' ':
                continue
            else:
                char_list.append(s[i])

    return ''.join(char_list)

print(squash_spaces("  hello   world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))

