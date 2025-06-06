# #Problem 1: Hello User!
# def greet_user(name):
#     #Name too small or big
#     if not name or len(name) >= 100:
#         raise ValueError("Invalid Name Length: " + str(len(name)))
    
#     #Name only contains whitespace 
#     if not name.strip():
#         raise ValueError("Name must have characters")

#     print("Hello" + " " + name)

# #Problem 2: Calculate Difference
# def difference(a,b):
#     return a - b

# diff = difference(3,8)
# print(diff)

# #Problem 3: List Concatenation
# def concatenate_list(nums):
#     #for i in range(len(nums)):
#     #    nums.append(nums[i])
#     return nums + nums
    
# print(concatenate_list([1,2,3,4]))

# #Problem 4: Sleep Assessment
# def sleep_assessment(hours):
#     if hours < 8:
#         print("Oof, go back to bed!")
#     if hours >= 8 and hours <= 10:
#         return print("You got a good night's rest!")
#     if hours > 10:
#         return print("You're a sleep prodigy")
# sleep_assessment(10)
# sleep_assessment(4)
# sleep_assessment(12)
# sleep_assessment(9)
# #Problem 5: Calculate Tip
# def calculate_tip(bill,service_quality):
#     tip_amount = 0
#     if service_quality == "poor":
#         tip_amount = 0.1
#     elif service_quality == "average":
#         tip_amount = 0.15
#     elif service_quality == "excellent":
#         tip_amount = 0.2 
#     else:
#         return None
#     return bill * tip_amount

def calculate_tip1(bill,service_quality):
    rates = {"poor":0.1,"average":0.15,"excellent":0.2}
    return bill * rates.get(service_quality)
    
tip1 = calculate_tip1(44.53, "average")
print(tip1)
tip2 = calculate_tip1(44.53, "poor")
print(tip2)
tip3 = calculate_tip1(44.53, "excellent")
print(tip3)
#Problem 6: Rock,Paper,Scissors
def rock_paper_scissors(player1,player2):
    if player1 == player2:
        print("It's a tie!")
    if (player1 == "rock" and player2 == "scissors") or (player1 =="paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
        #print(f"player1: {player1}, player2: {player2}")
        print("Player 1 wins")
    elif (player2 == "rock" and player1 == "scissors") or (player2 =="paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper"):
        print("Player 2 wins")
rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")     
#Problem 7: Unscramble and Divide


def halve_lst(lst):
    result = []
    for number in lst:
        halved = number/2
        result.append(halved)
    return result
print(halve_lst([2,4,6,8]))

'''

g. def halve_lst(lst):
a. result = []
b. for number in lst:
d. halved = number/2
c. result.append(halved)
f. return result
e. halve_list([2,4,6,8])








'''
#Problem 8: Above the The Threshold

def above_threshold(lst,threshold):
    result = []
    for i in lst:
        if i > threshold:
            result.append(i)
    return result

lst = [8,2,13,11,4,10,14]
new_lst = above_threshold(lst,10)
print(new_lst)
#Problem 9: Countdown
def countdown(m,n):
    for i in range(m,n-1,-1):
        print(i)
countdown(52,44)

#Problem 10: Calculate Power
def power(base,exponent):
    if exponent == 1:
        return base
    return base * power(base,exponent - 1)
print("\n\n\n\n\n")
print(power(3,3))
#Problem 11: Length of List
def list_length(lst):
    list_counter = 0
    for i in lst:
        list_counter += 1
        pass
    return list_counter
test_list = [213,32,12,3]
print(list_length(test_list))

#Problem 12: Calculate Factorial
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)
print("\n\n\n\n" + str(factorial(6)))
#Problem 13: Calculate the Squares
def squares(nums):
    for i in range(len(nums)):
        nums[i] *= nums[i]
    return nums

#print(squares(test_list))
        
#Problem 14: Multiply List 
def multiply_lst(lst,multiplier):
    for i in range(len(lst)):
        lst[i] *= multiplier
    return lst

print(multiply_lst(test_list,3))
#Problem 15: Count Evens 
def count_evens(lst):
    evens_counter = 0
    for num in lst:
        if num % 2 == 0:
            evens_counter += 1
    return evens_counter
print("\n\n\n\n\n\n")
print(count_evens([2,4,6,8]))
