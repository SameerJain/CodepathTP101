# Problem 5: Missing Number
'''
sort list
two pointers to compare
if value2 is more than 1 greater than value1
loop between the two values 
append missing values to result list 
'''
def find_missing(nums):
    nums.sort()
    result = []
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            for j in range(nums[i]+1,nums[i+1]):
                result.append(j)
    return result

nums = [2,4,1,0,9]
# 0 1 2 4 5 
print(find_missing(nums))
