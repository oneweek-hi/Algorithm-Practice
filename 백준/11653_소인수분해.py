n=int(input())
i=2
result=[]

while i < n+1:

    if n ==1:
        break

    if n%i == 0:
        n=n//i
        result.append(i)
        continue

    i += 1


for i in range(len(result)):
    print(result[i])



