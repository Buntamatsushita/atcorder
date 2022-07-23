line1 = int(input())

lst = []



for i in range(line1):
    line = input()
    if line not in lst:
        print(line)
    else:
        x = 0
        tmp = line
        while line in lst:
            x = x + 1
            line = tmp + "(" + str(x) + ")"
        print(line)
    lst.append(line)

print(lst)
