def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Pointer j for the position of the next unique element
    j = 1
    
    # Iterate through the array with i
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            print(f"j: {j}, i: {i}, nums: {nums}")
            j += 1
     
    nums[:] = nums[:j]

            
    return j  # The new length after removing duplicates
    

nums = [1,1,2,3,4,4,4,5]
print(nums)
print("Starting function")
print(remove_duplicates(nums))
print("Final")
print(nums) # same list