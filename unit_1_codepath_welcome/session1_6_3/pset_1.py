
#! Problem 1:Hello World!
class Problem1:

    def print_function(self,input):
        print(input)   
    
    def solve(self):
        print(f"Expected: Hello World")
        print(f"Actual: ",end= "")
        self.print_function('Hello World')
        

Problem1().solve()

#! Problem 2: Today's Mood

class problem_2:

    def todays_mood():
        mood = " Feeling like a boss"
        print("Today's mood:" + mood)

    def solve(self):
        print("Expected: Today's mood: Feeling like a boss")
        print(f"Actual: ",end= "")
        
todays_mood()

#! Problem 3 Lunch Menu
def print_menu(menu):
    print("Lunch today is: " + menu)

print("Salad")

# #! Problem 4: Sum of Two Integers
# def sum_double(a, b):
#     return 2 * (a + b)

# print(sum_double(5, 2))

# #! Problem 5: Product of Two Integers
# def product(a, b):
#     return a * b

# print(product(5, 234))

# #! Problem 6: Classify Age
# def classify_age(age):
#     print("child" if age < 18 else "adult")

# classify_age(13)

# #! Problem 7: What time is it?
# def what_time_is_it(hour):
#     result = ""
#     if hour == 2:
#         result = "taco time"
#     elif hour == 12:
#         result = "peanut butter jelly time"
#     else:
#         result = "nap time"
#     print(result)

# what_time_is_it(12)

# #! Problem 8: Blackjack
# def black_jack(score):
#     result = ""
#     if score < 17:
#         result = "Hit me!"
#     if score >= 17 and score < 21:
#         result = "Nice hand!"
#     if score == 21:
#         result = "Blackjack!"
#     elif score > 21:
#         result = "Bust!"
#     print(result)

# black_jack(23)

# #! Problem 9: First Item
# def get_first(lst):
#     return (lst[0])

# input = [1, 2, 3, 4, 5]
# print(get_first(input))

# #! Problem 10: Last Item
# def get_last(lst):
#     return (lst[-1])

# print(get_last(input))

# #! problem 11: Counter
# def counter(stop):
#     for i in range(1, stop + 1):
#         print(i)
# counter(7)

# print("Test")

# #! Problem 12:Sum of 1 to 10
# def sum_ten():
#     num = 0
#     for i in range(1,11):
#         num += i
#     print(num)
    
# sum_ten()

# #! Problem 13:Total Sum
# def sum_postive_numbers(input):
#     num = 0
#     for i in range(1,input + 1):
#         num += i
#     print(num)
    
# sum_postive_numbers(6)

# #! Problem 14:Total Sum in range
# def sum_range(start,stop):
#     num = 0
#     for i in range(start,stop+1):
#         num += i
#     print(num)
    
# print("\n")
# sum_range(3,9)

# #! Problem 15:Negative Numbers
# def print_negatives(lst):
#     counter = []
#     for i in lst:
#         if i < 0:
#             print(i)
#     return counter

# test_list = [3,-2,2,1,-5]
# print_negatives(test_list)
