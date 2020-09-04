sum = 0
a = 0
b = 1
n = int(input("enter a number:"))
for i in range(n - 1):
    sum = a + b
    a, b = b, sum

print(sum)
