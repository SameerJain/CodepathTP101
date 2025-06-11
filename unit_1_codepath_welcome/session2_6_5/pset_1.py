#! Problem 1:Print List
def print_list(lst):
    for ele in lst:
        print(ele)

print_list(["pika", "char", "lucario"])

#! Problem 2:Print Doubled List


def doubled(lst):
    for ele in lst:
        print(ele * 2)
# doubled([1,2,3])
#! Problem 3:Return Doubled List


def doubled2(lst):
    for i in range(len(lst)):
        lst[i] *= 2
    return lst


print(doubled2([1, 2, 3]))

#! Problem 4:Flip Signs


def flip_sign(lst):
    for i in range(len(lst)):
        lst[i] *= -1
    return (lst)


#! Problem 5:Max Difference
def max_difference(lst):
    return max(lst) - min(lst)


def max_difference2(lst):
    min_val, max_val = lst[0], lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i

    return max_val - min_val


test_list = [11, 2, 3, 4]
print(max_difference2(test_list))

#! Problem 6:Below Threshold
def count_less_than(numbers,threshold):
    less_counter = 0
    for ele in numbers:
        if ele < threshold:
            less_counter+=1
    return less_counter

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)
print("\n\n\n")
#! Problem 7:Evens List
def get_evens(lst):
    result = []
    for ele in lst:
        if ele % 2 == 0:
            result.append(ele)
    return result
lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)
#! Problem 8: Multiples of Five
def multiples_of_five():
    for ele in range(1,101):
        if ele % 5 == 0:
            print(ele)
# multiples_of_five()
#! Problem 9: Divisors
def find_divisors(n):
    result = []
    for ele in range(1,n+1):
        if n % ele == 0:
            result.append(ele)
    return result
lst = find_divisors(6)
print(lst)
#! Problem 10: FizzBuzz
def fizzbuzz(n):
    for i in range(1,n+1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if result == "":
            print(i)
        else:
            print(result)
fizzbuzz(45)


#! Problem 11: Print the Index
def print_indices(lst):
    for i in range(len(lst)):
        print(i)
print_indices(test_list)
print("\n\n\n\n\n")
#! Problem 12: Linear Search
def linear_search(lst,target):
    for idx,ele in enumerate(lst):
        if ele == target:
            return idx
    return -1

lst = [1,4,5,2,8]
position = linear_search(lst,10)
print(position)
