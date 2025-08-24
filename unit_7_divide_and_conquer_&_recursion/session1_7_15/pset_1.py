
#! Problem 1: Hello Hello
def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)

def repeat_hello_iterative(n):
    for i in range(0,n):
        print("Hello")
#The actual doing of the code is still there but there is an if statement and a function call to itself 

#! Problem 2: Factorial Cases
def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    else:
        return factorial(n) * factorial(n-1)


#! Problem 3: Recursive Sum
def sum_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[-1] + sum_list(lst[:len(lst)-1])

lst = [1,2,3,4,5]
# print("Expected: 15   Actual: ",sum_list(lst))

#! Problem 4: Recursive Power of 2
def is_power_of_two(n):
    if n == 2:
        print(n)
        return True
    if n <= 1:
        print(n)
        return False

    return is_power_of_two(n/2)

x = 4
print(is_power_of_two(x), x)

#! Problem 5: Binary Search 1
def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
    left = 0
	# Initialize a right pointer to the last index in the list
    right = len(lst) - 1
	# While left pointer is less than right pointer:
    while left < right:
		# Find the middle index of the array
	    mid = (left + right) // 2
		# If the value at the middle index is the target value:
			if lst[mid] == target:
            # Return the middle index
            return mid
		# Else if the value at the middle index is less than our target value:
			elif lst[mid] < target:
            # Update pointer(s) to only search right half of the list in next loop iteration
            
        # Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1

def binary_search(lst, target):
	pass
#! Problem 6: Backwards Binary Search 
def find_last(lst,target):
    pass

#! Problem 7: Find Floor
def find_floor(lst,x):
    pass






