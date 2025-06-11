
#! Problem 1: Mountain Peak
'''
if list is less than 3 elements, return error
iterate thru list
set max_val and idx_max_val
use max_val to find highest element 

return index of max_val
'''


def peak_index_in_mountain_list(lst):
    if len(lst) < 3:
        return None
    max_val = 0
    idx_max_val = 0
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            idx_max_val = i
    return idx_max_val


def peak_index_in_mountain_list2(lst):
    for i in range(1, len(lst)-1):
        if lst[i] > lst[i+1]:
            return i


lst = [0, 3, 8, 0]
# print(peak_index_in_mountain_list2(lst))


#! Problem 2: Build Inventory
def build_inventory(product_names, product_prices):
    result = {}
    for i in range(len(product_names)):
        result[product_names[i]] = product_prices[i]
    return result


product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]

# print(build_inventory(product_names,product_prices))

#! Problem 3: Update or warn
'''
if key in records
    update and print message
else print error message
'''


def update_or_warn(records, item, update_value):
    if item in records:
        print(f"{item} found, dictionary updated")
        records[item] = update_value
    else:
        print(f"{item} not found")
    return records


records = {"apple": 1, "banana": 2, "orange": 3}

# print(update_or_warn(records, "banana", 5))

# print(update_or_warn(records, "grape", 4))


#! Problem 4: Attendance Rate
'''
create counter variable 
iterate thru attendance list
counter += 1 if present
return counter/total students
'''


def attendance_rate(attendance_list):
    counter = 0
    for value in attendance_list.values():
        if value == "Present":
            counter += 1

    return counter/len(attendance_list) * 100


attendance_list = {
    "Bluey": "Present",
    "Bingo": "Absent",
    "Snickers": "Present",
    "Winton": "Absent"
}

# print(attendance_rate(attendance_list))

#! Problem 5: Average Book Ratings

'''
init new dictionary 

'''


def average_book_ratings(book_ratings):
    result = {}
    for book in book_ratings:
        result[book] = sum(book_ratings[book]) / len(book_ratings[book])
    return result


book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}
# print(average_book_ratings(book_ratings))

#! Problem 6: Odd Keys Even Values
'''

'''


def is_odd(num):
    return num % 2


def is_even(num):
    return (num % 2) - 1


def odd_keys_even_values(dictionary):
    result = []
    for key, value in dictionary.items():
        if is_odd(key) and is_even(value):
            result.append(key)
    return result


dictionary = {0: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
# print(final_list)

#! Problem 7: Best Team
'''
init score_sum dict
create game frequency dict by team
insert key and value into score_sum
    if key not there then init key and value
    else we add the key and the value 

use max_val iterator thru score_sum dict to find average by team
store high avg team name in string

return team name 
'''

def team_with_best_average_score(games):
    score_sums = {}
    game_freqs = {}
    
    for game in games:
        team_name = game['team_name']
        team_score = game['score']
        if team_name not in score_sums:
            score_sums[team_name] = team_score
            game_freqs[team_name] = 1
        else:
            score_sums[team_name] += team_score
            game_freqs[team_name] += 1
    
    highest_avg_team = ""
    highest_avg = 0
    for key in score_sums:
        curr_avg = score_sums[key]/game_freqs[key]
        if curr_avg > highest_avg:
            highest_avg = curr_avg
            highest_avg_team = key
            
    return highest_avg_team


games = [
    {"team_name": "Lions",
     "score": 23
     },
    {"team_name": "Tigers",
     "score": 30
     },
    {"team_name": "Lions",
     "score": 27
     },
    {"team_name": "Bears",
     "score": 20
     },
    {"team_name": "Tigers",
     "score": 24
     },
    {"team_name": "Bears",
     "score": 22
     }
]

#print(team_with_best_average_score(games))
'''
init result dict
iterate thru lista then listb
if item in lista is not in listb
    key for item is true 
    append to result 
if item in listb is not in lista
    key for item is false
    append to result 
return result dict 
'''
#! Problem 8: First Unique Items
def find_unique_items(list_a,list_b):
    result = {}
    for item in list_a:
        if item not in list_b:
            result[item] = True
    for item in list_b:
        if item not in list_a:
            result[item] = False
    return result

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]

print(find_unique_items(list_a,list_b))

