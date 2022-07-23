import itertools

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))

lst = []

lst2 = []

result = 0

l = range(2)

for i in range(line1[1]):
    line = list(map(int, input().split()))
    lst.append(line)

lst2 = list(itertools.product(l, repeat=line1[0]))
    
for i in lst2:
    tmp = 0
    count = 0
    for j in range(len(i)):
        if i[j] == 1:
            count = count + 1
            tmp = tmp + line2[j]
            for k in lst:
                if k[0] == count:
                    tmp = tmp + k[1]
        else:
            count = 0
    
    if result < tmp:
        result = tmp

print(result)