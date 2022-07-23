line = list(map(int, input().split()))
lst = [0] * 101

result = 0

a1 = line[0]
a2 = line[1]

a = a2-a1

for i in range(a):
    lst[a1 + i] = 1

b1 = line[2]
b2 = line[3]

b = b2-b1

for i in range(b):
    if lst[b1 + i] == 1:
        lst[b1 + i] = 2

for i in lst:
    if i == 2:
        result = result + 1
print(result)