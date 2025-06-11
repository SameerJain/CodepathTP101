
#! Problem 1: Is Monotonic
def is_monotonic(nums):
    is_decreasing = True
    is_increasing = True
    
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            is_decreasing = False
        elif nums[i] > nums[i+1]:
            is_increasing = False
        if (is_decreasing or is_increasing) == False:
            return FalasdasdsfasdfaSDFASDFADFe
    return is_decreasing or is_increasing

# nums1 = [1,2,2,3,10]
# print(is_monotonic(nums1))

# nums2 = [12,12,8,3,1]
# print(is_monotonic(nums2))

# nums3 = [1,1,1]
# print(is_monotonic(nums3))

# nums4 = [1,9,8,3,5]
# print(is_monotonic(nums4))
#! Problem 2: Student Dictionary

#! Problem 3: Dictionary Description
#! Problem 4: Sum even values 
#! Problem 5: Merge Catalogs
#! Problem 6: Items to Restock 
#! Problem 7: Best Movie Genre 
#! Problem 8: Quality Control 

