""" 
Unit 1 Cheatsheet
Overview:
Here is a helpful cheatsheet outlining common Python functions that will help you in your problem solving journey! Use this as reference as you solve the breakout problems below. This is not an exhaustive list of all Python syntax and built-in functionality; it only includes specialized syntax needed to ace Unit 1. In addition to the material below, by the end of this unit you should know how to:

-Write, use, and modify variables, functions, and print statements
-Use conditional logic (if statements)
-Work with lists (accessing, iterating, etc)
"""

#? Built-In Functions
#!‼️ This material is in scope for the Unit 1 assessment.
# Print
print(s) # Prints the message s to the console. Try it
# Accepts one parameter s: the message you would like to print
# Example Usage:

# Example 1: Printing a string
print("Welcome to TIP101!") # Prints "Welcome to TIP101!" to the console

# Example 2: Printing an integer
print(100) # Prints 100 to the console

# Example 3: Printing a variable
s = "Welcome to CodePath!"
num = 7
print(s)   # Prints "Welcome to CodePath" to the console
print(num) # Prints 7 to the console

# Example 4: Printing a list
lst = ["TIP101", "TIP102", "TIP103"]
print(lst) # Prints ["TIP101", "TIP102", "TIP103"] to the console

# Example 5: Printing an expression
x = 5
y = 3
print(x + y) # Prints 8 to the console

#Length
len(s) #Returns the length of a list or string. Try it

# Accepts one parameter s: the list or string we would like to get the length of
# Returns the number of items in a list or the number of characters in a string
# Example Usage:


# Example 1: Getting the length of a list
lst = ['a', 'b', 'c']
lst_length = len(lst) 
print(lst_length) # Output: 3

# Example 2: Getting the length of string
s = 'abcd'
s_length = len(s)
print(s_length) # Output: 4

# Range
range(start, stop, step) # Returns a sequence of numbers. Try it
'''
Accepts three parameters:
start: the first number in the sequence, this is an optional parameter. If we do not provide a start, the range will start from 0.
stop: the last value in the sequence exclusive, meaning that the stop value is not actually included in the sequence. This is a required parameter
step: how much to increment each number in the sequence. If we do not provide a step, each successive number in the sequence will increment by 1.
Example Usage:
'''

# Example 1: Just the stop value 
range(10) # Evaluates to the sequence: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Example 2: Start and stop value
range(1, 11) # Evaluates to the sequence: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Example 3: Start, stop, and step value
range(0, 30, 5) # Evaluates to the sequence: 0, 5, 10, 15, 20, 25
'''
For Loops
for num in nums Iterates through every number in nums. Try it

For loops in Python allow you to iterate over a sequence (such as a list, string, or range) and execute a block of code multiple times. This is particularly useful for accessing each element in a list or executing a function multiple times.

Example Usage:
''';
# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Outputs each fruit on a new line

# Example 2: Using a for loop with a range
for i in range(5):
    print(i)  # Prints numbers 0 to 4
'''
List Methods & Syntax
‼️ This material is in scope for the Unit 1 assessment.
Append Method
lst.append(item) Adds an item to the end of the list. Try it

Accepts one parameter item: the item you would like to add to the list
Example Usage:
'''

# Example 1: Add an integer to the list
lst = [1, 2, 3, 4]
lst.append(5)
print(lst) # Prints [1, 2, 3, 4, 5]
'''
Sort Method
lst.sort() Sorts the list in ascending order. Try it

Does not have any required parameters
Does not return any value
Example Usage:
'''

# Example 1: List of integers
lst = [4, 2, 1, 3]
lst.sort()
print(lst) # Prints [1, 2, 3, 4]


# Example 2: List of strings
lst = ['b', 'a', 'd', 'c']
lst.sort()
print(lst) # Prints ['a', 'b', 'c', 'd']

'''
Bonus Functions & Syntax
The following syntax is nice to know and may improve your code readability or help you solve certain problems more easily. However, they are not required to solve any of the problems in this unit. These are not in scope for the Unit 1 assessment, and you do not need to memorize them! Click on the function to read more about how to use it.
'''

lst.insert(x, item) # Inserts item into list at index x
lst.remove(item) # Removes item from list
lst.pop(x) # Removes element at index x from list
lst.copy() # Creates a copy of a list
abs(x) # Returns the absolute value of a number x.
enumerate() # Returns indices and values of list as pairs. Helpful for looping over indices and values of a list simultaneously!
