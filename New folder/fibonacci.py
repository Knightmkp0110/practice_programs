n = 10
a = 0
b = 1
temp = b  
count = 1

while count <= n:
    print(temp, end=" ")
    count += 1
    a, b = b, temp
    temp = a + b
print()