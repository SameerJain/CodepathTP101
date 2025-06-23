
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


student_names = ["Ada Lovelace", "Tu Youyou",
                 "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]

# print(student_dictionary(student_names))

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
    total = 0
    for value in dictionary.values():
        if value % 2 == 0:
            total += value
    return total


dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
# print(sum_even_values(dictionary))

#! Problem 5: Merge Catalogs
'''
iterate thru catalog 2:
insert all catalog 2 entries into result 
return result 
'''


def merge_catalogs(catalog_1, catalog_2):

    for key, value in catalog_2.items():
        catalog_1[key] = value
    return catalog_1


catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}

# print(merge_catalogs(catalog1,catalog2))

#! Problem 6: Items to Restock
'''
if products is empty, return empty list 
iterate thru products
if key value is less than threshold, append key to result list
return list 
'''


def items_to_restock(products, restock_threshold):
    result = []
    if not products:
        return []
    for key, value in products.items():
        if value < restock_threshold:
            result.append(key)
    return result


products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5

# print(items_to_restock(products,restock_threshold))

#! Problem 7: Best Movie Genre
'''
create dict for running sum 
create another dict for amount per genre using the same key 
insert movie ratings and amount based off genre
use max_val iterator to find highest average, keeping track of key 
find whichever value for final average is highest 
'''


def most_popular_genre(movies):
    genre_sums = {}
    genre_frequency = {}
    for movie in movies:
        if movie['genre'] not in genre_sums:
            genre_sums[movie['genre']] = movie['rating']
            genre_frequency[movie['genre']] = 1
        else:
            genre_sums[movie['genre']] += movie['rating']
            genre_frequency[movie['genre']] += 1

    highest_average = 0
    highest_genre = ""

    for genre, genre_sum in genre_sums.items():
        genre_avg = genre_sum / genre_frequency[genre]
        if genre_avg > highest_average:
            highest_average = genre_avg
            highest_genre = genre
    return highest_genre


movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 0.8
     },
    {"title": "The Matrix",
     "genre": "Science Fiction",
     "rating": 8.7
     },
    {"title": "Pride and Prejudice",
     "genre": "Romance",
     "rating": 7.8
     },
    {"title": "Sense and Sensibility",
     "genre": "Romance",
     "rating": 7.7
     }
]

print(most_popular_genre(movies))

#! Problem 8: Quality Control

'''
create result dictionary
iterate thru product dict
add keys to result
if the value is less than theshold
    set the value of that key in result to fail, pass otherwise

return result 
'''
def quality_control(product_score,threshold):
    result = {}
    
    for key,value in product_score.items():
        if value < threshold:
            result[key] = "fail"
        else:
            result[key] = "pass"
    
    return result

scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60

print(quality_control(scores,threshold))
