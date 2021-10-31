num=[]
for i in range(9):
    a = int(input())
    num.append(a)

one = 0
two = 0
value = sum(num)

for i in range (9):
    for j in range(9):
        if (value-(num[i]+num[j]) == 100):
            one =i
            two =j
            break


del num[one]
del num[two]
num.sort()
for i in range(7):
    print(num[i])




