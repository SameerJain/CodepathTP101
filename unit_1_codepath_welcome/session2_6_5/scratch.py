'''
init total
iterate thru dict values
if % 2 == 0 
    add to total
'''
def sum_even_values(dictionary):
    total = 0
    for value in dictionary.values():
        if value % 2 == 0:
            total += value    
    return total


dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))
