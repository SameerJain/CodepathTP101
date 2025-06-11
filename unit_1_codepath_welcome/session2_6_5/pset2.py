# #! Problem 1:Convert Temperature
# def convertTemp(celsius):
#     kelvin = celsius + 273.15
#     fahrenheit = celsius * 1.80 + 32.00
#     return kelvin, fahrenheit
# print(convertTemp(23.00))
# #! Problem 2: Average Score
# def average(scores):
#     sum_val = 0
#     amount_of_scores = 0
#     for score in scores:
#         sum_val += score
#         amount_of_scores += 1
#     calculated_average = sum_val / amount_of_scores
#     return calculated_average

# scores = [84,73,92,95,88]
# print(average(scores))
# #! Problem 3: Increment by 1
# def increment_values(lst):
#     for i in range(len(lst)):
#         lst[i] += 1
#     return lst
# test_lst1 = [3,5,8,2]
# # print(increment_values(test_lst1))
# #! Problem 4: Check for number
# def check_num(lst,num):
#     for ele in lst:
#         if ele == num:
#             return True
#     return False
# print(check_num(test_lst1,5))
# print(check_num(test_lst1,28))

# #! Problem 5: Missing Number
# def find_missing(nums):
#     """
#     Finds missing numbers in sequence
#     Args:
#         nums (list): given input of unsorted list
#     Returns:
#         list of missing numbers in sorted sequence
#     """
#     if len(nums) < 2:
#         return []
    
#     nums.sort()
#     missing = []
    
#     for i in range(len(nums) - 1):
#         current = nums[i]
#         next_num = nums[i + 1]
#         if next_num - current > 1:
#             for missing_sum in range(current + 1,next_num):
#                 missing.append(missing_sum)
    
#     return missing

# nums = [2,4,1,0,5]
# missing_num = find_missing(nums)
# print(f"Orginal: {nums}")

#! Problem 6: Reverse List
def reverse_list(lst):
    result = []
    for i in range(len(lst)-1,-1,-1):
        result.append(lst[i])
    return result
test_lst1 = [1,2,3,4]
#print(reverse_list(test_lst1))


#! Problem 7: Get Odd Numbers
def get_odds(nums):
    result = []
    for num in nums:
        if num % 2 == 1:
            result.append(num)
    return result

# print(get_odds([5,1,5,2,3,222]))
#! Problem 8: Multiplication Table
def multiplication_table(num):
    for i in range(1,11):
        print(num * i)
        
# multiplication_table(7)
#! Problem 9: Create Number 
'''
figure out how many numbers in digits

'''
def list_to_number(digits):
    result = 0
    multiplier_value = len(digits) - 1
    for i in range(len(digits)):
        result += digits[i] * 10 ** multiplier_value
        multiplier_value -=1
        print(result)
        
    return result

digits = [1,0,3,4,4,1,4,9]
# print("hello", list_to_number(digits))
#! Problem 10: Move Zeros 
'''
-iterate through list
-check how many non-zeroes there are
-iterate thru list again 
-remove its a zero in a temp var
-append temp var to the end
-once we reach arr[num of non-zeroes] we know we are done
'''
def move_zeroes(nums):
    temp_var = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            temp_var = nums[i]
            nums.remove(nums[i])
            nums.append(temp_var)
    return nums

test_nums = [1,0,2,3,0,0,0,123123,0,0,0,4]


#! Problem 11: Odd Indices
def print_odd_indices(nums):
    for i in range(len(nums)):
        if i % 2 == 1:
            print(i, nums[i])
print_odd_indices([1,2,3,4,5])

#! Problem 12: List Occurrences
lst = [1,2,6,5,2,1,3,2,2]

def find_all_occurrences(lst,target):
    result = []
    for i in range(len(lst)):
        if lst[i] == target:
            result.append(i)
    return result

print(find_all_occurrences(lst,2))
    
