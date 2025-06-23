
# #! Problem 1: Perfect Match 
# def match_made(dictionary):
#     for key, value in dictionary.items():
#         print( f"{key} and {value} are a perfect match.")
    

# dictionary = {"Peanut Butter": "Jelly","Patrick":"Star","Ash":"Pikachu"}
# (match_made(dictionary))

#! Problem 2: Remove Char 
def remove_char1(s,n):
    return s.replace(s[2],"",1)
    
def remove_char2(s,n):
    return s[:n] + s[n+1::] 

def remove_char3(s,n):
    new_str = ""
    for i in range(len(s)):
        if i == n:
            continue
        new_str+= s[i]
    return new_str

s = "typpo"
fixed_s = remove_char3(s, 2)
# print(fixed_s)

#! Problem 3: Count Vowels 
def vowel_count(s):
    vowel_list = ['a','e','i','o','u']
    vowel_count = 0
    for c in s.lower():
        if c in vowel_list:
            vowel_count += 1 
    return vowel_count

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)

#! Problem 4: Reverse Sentence 
def reverse_sentence(sentence: str) -> str:
    """
    split the sentence into a list of words
    reverse the list 
    rejoin the list
    """
    new_sent = ' '.join(sentence.split()[::-1])
    # new_sent = ' '.join(new_sent)
    return new_sent

sentence = "I solemnly swear I am up to no good"
# print(reverse_sentence(sentence))

#! Problem 5: String Compression 
"""
iterate thru string
    up until it gets to the end of the letter sequence, store the amount
    then insert into the new string the amount
if the length is greater than original, return original
"""
def compress_string0(my_str):
    curr_count = 0
    new_str = ""
    for i in range(1,len(my_str)):
        print(f"my_str[i]: {my_str[i]}, my_str[i-1]: {my_str[i-1]}, count: {curr_count},  new_str: {new_str}")
        curr_count += 1
        if my_str[i] == my_str[i-1]:
            continue
        else:
            new_str += my_str[i-1]
            new_str += str(curr_count)
            curr_count = 0
    
    return new_str if len(new_str) < len(my_str) else my_str

def compress_string0(my_str: str) -> str:
    if not my_str:
        return my_str

    new_str = ""
    i = 0
    while i < len(my_str):
        curr_char = my_str[i]
        curr_count = 1
        i += 1
        while i < len(my_str) and curr_char == my_str[i]:
            curr_count += 1
            i += 1
        new_str += curr_char
        new_str += str(curr_count)
    return new_str if len(new_str) < len(my_str) else my_str

def compress_string(my_str):
    if not my_str:
        return my_str
    
    new_str = ""
    char_count = 1

    for i in range(1,len(my_str)):
        if my_str[i] == my_str[i-1]:
            char_count += 1
        else:
            new_str += my_str[i-1] + str(char_count)
            char_count = 1
    new_str += my_str[i] + str(char_count)

    if len(new_str) > len(my_str):
        return my_str
    
    return new_str

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2) 
    


#! Problem 6: Needle in a Haystack 
"""
iterate thru string

set window to length of needle
if window is same as needle
return the idx
"""

def find_the_needle(haystack,needle):
    print(f"length of haystack: {len(haystack)}")
    print(f"Length of needle: {len(needle)}")
    for i in range(len(haystack) - len(needle) + 1):
        print(f"i: {i}")
        window = haystack[i:i + len(needle)]
        if window == needle:
            return i
    return -1
haystack = "tomeornottome"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))

        