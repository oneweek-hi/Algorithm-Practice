import itertools
min=1000000000
max=-1000000000
n = int(input())
num=list(map(int, input().split()))
booho=list(map(int, input().split()))
result=[]

for i in range(booho[0]):
    result.append("+")
for i in range(booho[1]):
    result.append("-")
for i in range(booho[2]):
    result.append("*")
for i in range(booho[3]):
    result.append("/")

permu_booho=list(map(''.join, itertools.permutations(result, n-1)))
for x in permu_booho:
    cal=num[0]
    for i in range(1,n):
        if x[i-1] == "+":
            cal += num[i]
        elif x[i-1] == "-":
            cal -= num[i]
        elif x[i-1] == "*":
            cal *= num[i]
        elif x[i-1] == "/":
            cal /= num[i]
        cal = int(cal)

    if cal > max:
        max = int(cal)
    if cal < min:
        min = int(cal)


print(max)
print(min)


