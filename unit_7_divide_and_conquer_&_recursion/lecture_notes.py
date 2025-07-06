def recursice_sum(num):
    if num <= 1:
        return num
    return num + recursive_sum(num-1)

result = recursive_sum(5)
print(result)   

def recursive_sum(num):
    if num <= 1:
        return num
    return num + recursive_sum(num - 1)



def iterative_sum_while(num):
    total = 0
    while num > 0:
        total += num
        num -= 1
    return total



    def print_tree(node):
    if node:
        print(node.value)
        print_tree(node.left)
        print_tree(node.right)

def print_tree(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.value)
        current = current.right

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)












Given a string s consisting of lowercase and/or uppercase English letters and digits, return all possible strings that can be formed by changing the case of the letters in s. You may not alter the order of characters in the string, and digits should remain unchanged.
Input: s = "a1b2"
Output: ["a1b2", "A1b2", "a1B2", "A1B2"]
Input: s = "3z4"
Output: ["3z4", "3Z4"]
Input: s = "12345"
Output: ["12345"]
