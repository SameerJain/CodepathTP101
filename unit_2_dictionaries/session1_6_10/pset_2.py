
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
            return False
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
def student_dictionary(student_names):
    result = {}
    for i in range(len(student_names)):
        result[student_names[i]] = i + 1
    return result
student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]

print(student_dictionary(student_names))
    
#! Problem 3: Dictionary Description

def get_description(info, keys):
    for key in keys:
        if key in info:
            print(info[key])
        else:
            print("None")

info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
# get_description(info,keys)


#! Problem 4: Sum even values 
def sum_even_values(dictionary):
    total += 0
    for value in dictionary.values():
        if value % 2 == 0:
            total += value
    return total

sum_even_values(dictionary):
    
#! Problem 5: Merge Catalogs
#! Problem 6: Items to Restock 
#! Problem 7: Best Movie Genre 
#! Problem 8: Quality Control 

