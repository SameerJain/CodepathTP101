
#! Problem 1: Highest Exponent 
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
def two_sum(nums,target):
    pass

nums = [2,7,11,15,7]

sol1 = two_sum(nums,9)
print(sol_1)

sol2 = two_sum(nums,18)
print(sol2)

#? This is also wrong given the problem statement 
#! Problem 3: Evaluate Two SUm 
def two_sum_p3(nums,target):
    prev_map = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff],i]
        prev_map[nums[i]] = i


#! Problem 4: 2-Pointer Reverse Letters 
def reverse_only_letters(s):
    pass
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)


#! Problem 5: Reverse Prefix 
def reverse_prefix(word,ch):
    pass

word = "abcdefd"
rev_word = reverse_prefix(word,"d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2,"w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefic(word3,"a")
print(rev_word3)



#! Problem 6: Squash Spaces 
def squash_spaces(s):
    pass

print(squash_spaces("  hello   world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))

