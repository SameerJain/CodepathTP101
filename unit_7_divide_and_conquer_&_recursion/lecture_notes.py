def recursice_sum(num):
    if num <= 1:
        return num
    return num + recursive_sum(num-1)

result = recursive_sum(5)
print(result)   