
#! Problem 1: Choose your Pokemon 
def choose_pokemon(my_pokemon):
    for pokemon in my_pokemon:
        print(f"{pokemon} I choose you!")

my_pokemon = ["Pikachu","Charizard","Eevee"]
# choose_pokemon(my_pokemon)

#! Problem 2: Rotate Left 
"""
create new string with size n from left
remove from left
append to right using string
"""

def rotate_left0(s,n):
    left_chunk = s[:n]
    new_str = s.replace(left_chunk,"",1)
    new_str += left_chunk
    return new_str

def rotate_left(s,n):
    return s[n:] + s[:n]

s = "rotation"
# print(rotate_left(s, 2))

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
def first_repeated_char(s: str) -> int | None:
    idx_map = {}
    first_idx = float('inf')

    for i in range(len(s)):
        char = s[i]
        if char in idx_map:
            first_idx = min(first_idx,idx_map[char])
        else:
            idx_map[char] = i

    return first_idx if first_idx != float('inf') else None

def first_repeated_char0(s):
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

# print(first_repeated_char(s))
# print(first_repeated_char(s2))
# print(first_repeated_char(s3))


#! Problem 4: Find the Imposter 

"""
iterate thru 
    if the letter is not in s1 return it 

freq count both strings using hashmap
iterate thru keys of 2
if its not in s1 return it
"""

def find_difference(s1,s2):
    for char in s2:
        if char not in s1:
            return char
    return None

s1 = "abcd"
s2 = "baedc"
# print(find_difference(s1, s2))

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

# s = "abcdeefghhhhh"
# count = length_of_longest_substring(s)
# print(count)

# s2 = "aaaaaaaaaaaaaaa"
# count = length_of_longest_substring(s2)
# print(count)


#! Problem 6: Roman to Integer 
"""
OLD:create hashmap for symbols
    use if statements for special cases
    store special cases separately
"""

"""
Iterate from right to left:
    if the value to the left is less
        subract and move down
"""

"""
iterate from left to right
    if the value on the right is less
        subtract and move down
"""

def roman_to_int(s):
    value_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }

    final_sum = 0
    i = len(s) - 1
    while i >= 0:
        final_sum += value_map[s[i]]
        if i != 0 and value_map[s[i-1]] < value_map[s[i]]:
            final_sum -= value_map[s[i-1]]
            i -= 1
        i -= 1
    return final_sum


s = "XL"
print(roman_to_int(s))

s2 = "LVIII"
print(roman_to_int(s2))

s3 = "MCMXCIV"
print(roman_to_int(s3))