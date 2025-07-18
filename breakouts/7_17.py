'''
Problem #1
Given a string s consisting of lowercase and/or uppercase English letters and digits, return all possible strings that can be formed by changing the case of the letters in s. You may not alter the order of characters in the string, and digits should remain unchanged.

Input: s = "a1b2"
Output: ["a1b2", "A1b2", "a1B2", "A1B2"]
Input: s = "3z4"
Output: ["3z4", "3Z4"]
Input: s = "12345"
Output: ["12345"]

plan:
create the result list 
append initial string
iterate thru character in string
	if char is a letter
		iterate again for all letters
		swap the case
		add to result list if its not already in there

return result list
'''

def possible_strings(s: str) -> list[str]:
	result = []
	result.append(s)
	for char in s:
		if char.isalpha():
			new_str = list(s)
			for i in range(len(new_str)):
				if new_str[i].isalpha:
					new_str[i] = new_str[i].isupper()
					result.append(new_str.join(""))

					new_str[i] = new_str[i].islower()
					result.append(new_str.join(""))
	return result

	
# Problem 1
'''
(())
'''
def is_nested0(paren_s):
	if len(paren_s) % 2 != 0:
		return False
	
	pass

def is_nested(s: str) -> bool:
    if len(s) % 2 != 0:
        return False 

    if not s:
        return True 

    if s[0] == ')' or s[-1] =='(':
        return False

    return is_nested(s[1:-1])

def is_nested2(s):
	
	if s[0] == ')':
		return True
	elif s[0] == '(':
		return is_nested(s[1:])

	return false

# test_str = "(())"
# print(is_nested2(test_str))

#Problem 2:

def binary_search(arr,low,high,target):
    if low > high:
        return None
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid, arr[mid]
    elif arr[mid] < target:
        return binary_search(arr,mid+ 1,high,target)
    else:
        return binary_search(arr,low,mid - 1,target)

test_arr = [1,2,3,4,5]

print(binary_search(test_arr,0,len(test_arr)-1,6))

'''
Mock Interview:
Given a string s consisting of lowercase and/or uppercase English letters and digits, return all possible strings that can be formed by changing the case of the letters in s. You may not alter the order of characters in the string, and digits should remain unchanged.

Input: s = "a1b2"
Output: ["a1b2", "A1b2", "a1B2", "A1B2"]
Input: s = "3z4"
Output: ["3z4", "3Z4"]
Input: s = "12345"
Output: ["12345"]

plan:
create the result list 
append initial string
iterate thru character in string
	if char is a letter
		iterate again for all letters
		swap the case
		add to result list if its not already in there

return result list
'''

# def possible_strings(s: str) -> list[str]:
# 	result = []
# 	result.append(s)
# 	for char in s:
# 		if char.isalpha():
# 			new_str = list(s)
# 			for i in range(len(new_str)):
# 				if new_str[i].isalpha:
# 					new_str[i] = new_str[i].isupper()
# 					result.append(new_str.join(""))

# 					new_str[i] = new_str[i].islower()
# 					result.append(new_str.join(""))
# 	return result


