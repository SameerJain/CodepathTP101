
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
def find_difference(s1,s2):
    pass

#! Problem 5: Longest Substring
def length_of_longest_substring(s):
    pass

#! Problem 6: Roman to Integer 
def roman_to_int(s):
    pass