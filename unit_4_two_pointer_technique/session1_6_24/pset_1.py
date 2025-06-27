
#! (DONE) Problem 1: Prime Number 

# Time: O(n)
# Space: O(1)
def is_prime(n):
    if n <= 1:
        return False

    i = n - 1

    while i > 1:
        if n % i == 0:
            return False
        i -=1 

    return True

# Time: O(n)
# Space: O(1)

# print(is_prime(5))
# print(is_prime(12))
# print(is_prime(9))



#!(DONE) Problem 2: 2-Pointer Reverse List 

""" 
set a pointer on each end
swap them one at a time
only iterate for half od the list 
"""

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left],lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

lst = [1,2,3,4,5]

# Time: O(n/2)
# Space: O(1) 
# print(reverse_list(lst))

#! (DONE) Problem 3: Evaluating Solutions

#? Question doesnt assume sorted list 

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left],lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

lst = [1,2,3,4,5]
# print(reverse_list(lst))

# Time Complexity: O(n/2) or O(N) 
# Space Complexity: O(1)

def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]

# Time Complexity: O(2N) or O(N)
# Space Complexity: O(1)

#! Problem 4: Move Even Integers 

def is_even(num):
    return True if num % 2 == 0 else False

def is_odd(num):
    return True if num % 2 != 0 else False

def sort_array_parity(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        if is_even(nums[left]):
            left += 1
        elif is_odd(nums[right]):
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return nums

nums = [3,1,2,4]
nums2 = [0]
# Time: O(n)
# Space: O(1)
# print(sort_array_parity(nums))
# print(sort_array_parity(nums2))

#! Problem 5: Palindrome 
"""

func for palindrome:
    use 2 pointers to check if all same



"""

def is_palindrome(word):
    left, right = 0, len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True

def first_palindrome0(words):
    for word in words:
        if is_palindrome(word):
            return word
    return ""

def first_palindrome(words: list[str]) -> str:
    for word in words:
        
        left, right = 0, len(word) - 1
        is_pal_flag = True

        while left < right:

            if word[left] != word[right]:
                is_pal_flag = False
                break

            left += 1
            right -= 1

        if is_pal_flag:
            return word

    return ""
# Time: O(n * m)
# Space: O(1)

# words = ["abc","car","ada","racecar","cool"]
# palindrome1 = first_palindrome(words)
# print(palindrome1)

# words2 = ["abc","racecar","cool"]
# palindrome2 = first_palindrome(words2)
# print(palindrome2)

# words3 = ["abc", "def", "ghi"]
# palindrome3 = first_palindrome(words3)
# print(palindrome3)
    
"""
iterate thru list
create pointer to iterate and pointer for duplicate

if number is not a duplicate, swap with a duplicate number at the start 
"""

#! Problem 6: Remove Duplicates with O(1)
def remove_duplicates(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[j]!= nums[i]:
            nums[i+1] = nums[j]
            i += 1
    return nums[:i]

# Time:O(n)
# Space: O(n)

nums = [1,1,2,3,4,4,4,5]
print("test3",nums)
print("test2",remove_duplicates(nums))
print("test",nums) # same list

