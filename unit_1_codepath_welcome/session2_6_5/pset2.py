# Problem 1:Convert Temperature
def convertTemp(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return kelvin, fahrenheit
print(convertTemp(23.00))
# Problem 2: Average Score
def average(scores):
    sum_val = 0
    amount_of_scores = 0
    for score in scores:
        sum_val += score
        amount_of_scores += 1
    calculated_average = sum_val / amount_of_scores
    return calculated_average

scores = [84,73,92,95,88]
print(average(scores))
# Problem 3: Increment by 1
def increment_values(lst):
    for i in range(len(lst)):
        lst[i] += 1
    return lst
test_lst1 = [3,5,8,2]
# print(increment_values(test_lst1))
# Problem 4: Check for number
def check_num(lst,num):
    for ele in lst:
        if ele == num:
            return True
    return False
print(check_num(test_lst1,5))
print(check_num(test_lst1,28))

# Problem 5: Missing Number
def find_missing(nums):
    """
    Finds missing numbers in sequence
    Args:
        nums (list): given input of unsorted list
    Returns:
        list of missing numbers in sorted sequence
    """
    if len(nums) < 2:
        return []
    
    nums.sort()
    missing = []
    
    for i in range(len(nums) - 1):
        current = nums[i]
        next_num = nums[i + 1]
        if next_num - current > 1:
            for missing_sum in range(current + 1,next_num):
                missing.append(missing_sum)
    
    return missing

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(f"Orginal: {nums}")

# Problem 6: Reverse List
def reverse_lis
# Problem 7: Get Odd Numbers
# Problem 8: Multiplication Table
# Problem 8: Create Number 
# Problem 10: Move Zeros 
# Problem 11: Odd Indices
# Problem 12: List Occurrences
