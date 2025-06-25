
#! (DONE) Problem 1: Sum of Strings 
"""
sum variable
loop thru type casting and add up
"""
def sum_of_number_strings(nums):
    final_sum = 0
    for num in nums:
        final_sum += int(num)
    return final_sum

# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)

#! (DONE) Problem 2: Remove Duplicates
def remove_duplicates1(nums):
    if not nums:
        return 0
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.remove(nums[i])
        else:
            i += 1

    return nums


"""
use two pointers
track when they are the same
    if we run into a different number
        we put it after a duplicate and replace i
    return the idx after the last one we use 
"""
def remove_dupes(items):
    if not items:
        return 0
    
    i = 0  # Pointer for the position of the last unique element
    
    for j in range(1, len(items)):
        print(f"i: {i}, j: {j}, list: {items}")
        if items[j] != items[i]:
            print(f"Not equal. items[j]: {items[j]}, items[i]: {items[i]}\n\n\n")
            i += 1
            items[i] = items[j]
    
    return i + 1

nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_dupes(nums))

#! (DONE) Problem 3: Reverse Letters
"""
iterate thru string and put all letters chars in list

iterate thru string and insert chars back if the curr char is a letter
start from back of created list
"""
def reverse_only_letters(s):
    s_letters = []
    result = ""
    
    for char in s:
        if char.isalpha():
            s_letters.append(char)
    i = len(s_letters)
    for char in s:
        if char.isalpha():
            i -= 1
            result += s_letters[i]
        else:
            result += char
    
    return result

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
# print(reversed_s)


#! (DONE) Problem 4: Longest Uniform Substring 

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
# print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
# print(l2)

#! (DONE) Problem 5: Teemo's Attack 
"""
iterate thru time series
    if the frame is an attack frame
        damage += 1
        set poision counter 
        add poision by 1 to damage
    add time
"""
def find_poisioned_duration(time_series,duration):
    
    i,j,damage = 0,0,0
    poision_left = duration

    while i < time_series[-1]:
        if i == time_series[j]:
            j += 1
            poision_left = duration
        elif poision_left > 0:
            damage += 1
        poision_left -= 1
        i += 1
    damage += duration
    return damage

"""
add either the duration or the difference between the next 2 times if its smaller
we are not taking damage at the frame we are being attacked
add the last damage at the very end 
"""
def find_poisoned_duration(time_series, duration):
    total_duration = 0
    for i in range(len(time_series)-1):
        # Calculate the actual poisoning time between two attacks
        actual_duration = min(time_series[i+1] - time_series[i] - 1, duration)

        total_duration += actual_duration
    # Add the duration of the last attack
    total_duration += duration
    return total_duration

time_series = [1,4,9]
damage = find_poisioned_duration(time_series,3)
print(damage)

"""
use freq map to get list of unique elements

iterate thru list 1
    its its not in list 2 and the keyval is exactly 1
    add it to the sum variable
return sum variable 
"""
#! (DONE) Problem 6: Sum Unique Elements 
def sum_of_unique_elements(lst1,lst2):
    freqs = {}
    final_sum = 0
    for num in lst1 + lst2:
        freqs[num] = freqs.get(num,0) + 1

    for num in lst1:
        if freqs[num] == 1:
            final_sum += num
    return final_sum

lstA = [1,2,3,4]
lstB = [3,4,5,6]
lstC = [7,7,7,7]

sum1 = sum_of_unique_elements(lstA,lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC,lstB)
print(sum2)



