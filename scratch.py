
#! Problem 3: First Duplicate 
#? I dont understand why the expected output is 3,5 None
"""
create a hashmap with key as letter and values as first appearance
iterate thru string
    if its in the map, we set first_rep_idx to the value
    if theres another one, we check which one is lower and swap
    if its not in the map we add it

ret none at end of loop
"""
def first_repeated_char0(s: str) -> int | None:
    idx_map = {}
    first_idx = float('inf')

    for i in range(len(s)):
        char = s[i]
        if char in idx_map:
            first_idx = min(first_idx,idx_map[char])
        else:
            idx_map[char] = i

    return first_idx if first_idx != float('inf') else None

def first_repeated_char(s):
    seen_map = {}
    for i in range(len(s)):
        char = s[i]
        if char in seen_map:
            return i
        seen_map[char] = i
    return None

s = "hello world"
s2 = "aAbBCC"
s3 = "abcdefg"

print(first_repeated_char(s))
print(first_repeated_char(s2))
print(first_repeated_char(s3))


#! Problem 5: Longest Substring
"""
init len of substring
iterate thru list
if char is different than what came before it:
    count += 1
if its same 
    count = 0
return longest_len
"""

#* MY SOLUTION -assuming chars can repeat non-consecutiveky
def length_of_longest_substring0(s):
    
    curr_sub_len = 0
    max_sub_len = 0
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            curr_sub_len += 1
            if i == 1:           
                curr_sub_len += 1
        else:
            # print(f"Streak Broken.: idx: {i}, letter: {s[i]},prev_letter {s[i-1]} curr_string: {s[:i]}")
            max_sub_len = max(max_sub_len,curr_sub_len)
            curr_sub_len = 0
    return max_sub_len

#* MY SOLUTION - assuming chars cant repeat non-consecutively
def length_of_longest_substring(s: str) -> int:
    last_used = {}
    seq_length = 0
    seq_start = 0
    max_length = 0
    for i, char in enumerate(s):
        if char in last_used and seq_start < last_used[char]:
            seq_start = last_used[char] + 1
        else:
            max_length = max(max_length, i - seq_start + 1)
        last_used[char] = i
        # print(f"i: {i}, char: {char}, donewith: {s[:i]}")
        # print(f"usedChar: {last_used}, start: {seq_start}, maxLength: {seq_length}")
        # print(f"startpos: {s[seq_start::]}\n\n\n")
    #print("Result: ")
    if max_length == 1:
        return 0
    return max_length

#* ANSWER KEY - with edit
def length_of_longest_substring0(s):
    start = maxLength = 0
    usedChar = {}
    
    
    for i, char in enumerate(s):
      #  print(f"i: {i}, char: {char}, donewith: {s[:i]}")
      #  print(f"usedChar: {usedChar}, start: {start}, maxLength: {maxLength}")
      #  print(f"startpos: {s[start::]}\n\n\n")
        if char in usedChar and start <= usedChar[char]:
            start = usedChar[char] + 1
        else:
            maxLength = max(maxLength, i - start + 1)
        usedChar[char] = i

    # for the case theres no sequence just replace 1 to 0
    if maxLength <= 1:
        return 0

    return maxLength

s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count)

# s2 = "aaaaaaaaaaaaaaa"
# count = length_of_longest_substring(s2)
# print(count)

#! Problem 5: No duplicates Allowed
# def remove_duplicates_from_front(nums):
#     frequency_map = {}
#     for num in nums:
#         frequency_map[num] = True
#     last_occurrences = []
#     for num in nums[::-1]:  # Reverse iterate
#         if frequency_map[num]:
#             last_occurrences.append(num)
#             frequency_map[num] = False
#     return last_occurrences[::-1]  # Reverse again to original order

# def remove_duplicates_from_front1(nums):
#     frequency_map = {}
#     for num in nums:
#         frequency_map[num] = True
#     last_occurrences = []
#     for num in nums:  # Reverse iterate
#         if frequency_map[num]:
#             last_occurrences.append(num)
#             frequency_map[num] = False
#     return last_occurrences  # Reverse again to original order
# nums = [6,5,3,5,2,8,3]

# print(remove_duplicates_from_front(nums))
# print(remove_duplicates_from_front1(nums))