
#! 3.2.3 Problem 3: First Duplicate 
#* MY SOLUTION 
def first_repeated_char1(s: str) -> int | None:
    idx_map = {}
    first_idx = float('inf')

    for i in range(len(s)):
        char = s[i]
        if char in idx_map:
            first_idx = min(first_idx,idx_map[char])
        else:
            idx_map[char] = i

    return first_idx if first_idx != float('inf') else None

#* ANSWER KEY
def first_repeated_char(s):
    seen_chars = []
    for index, char in enumerate(s):
        if char in seen_chars:
            return index
        seen_chars.append(char)
    return None

# #* Tests
# s = "hello world"
# s2 = "aAbBCC"
# s3 = "abcdefg"
# print(first_repeated_char(s))
# print(first_repeated_char(s2))
# print(first_repeated_char(s3))





#! 3.2.3 Problem 5: Longest Substring
#* ANSWER KEY - original
def length_of_longest_substring(s):
    start = maxLength = 0
    usedChar = {}
    
    for i, char in enumerate(s):
        if char in usedChar and start <= usedChar[char]:
            start = usedChar[char] + 1
        else:
            maxLength = max(maxLength, i - start + 1)
        usedChar[char] = i
    
    return maxLength

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


#* Tests
s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count)

s2 = "aaaaaaaaaaaaaaa"
count = length_of_longest_substring(s2)
print(count)






