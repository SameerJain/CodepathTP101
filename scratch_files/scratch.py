lst = [1,2,3,4,5]
x = lst.copy()
x[1] = 5000

for num in x[:]:
    x.remove(num)
    print(x, "num:",num)
print(x)