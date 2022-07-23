line1 = int(input())

lst = []

result = 0

for i in range(line1):
    line = input()
    lst.append(line)



for i in range(line1):
    for j in range(len(lst[i])):
        if lst[i][j] == "W":
            if lst[j][i] != "L":
                result = 1
        if lst[i][j] == "L":
            if lst[j][i] != "W":
                result = 1
        if lst[i][j] == "D":
            if lst[j][i] != "D":
                result = 1

                
if result == 0:
    print("correct")
else:
    print("incorrect")