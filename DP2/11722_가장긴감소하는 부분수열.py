n = int(input())
arr =list(map(int, input().split()))
d=[0]*n
d[0] = 1

for i in range(1,n):
    d[i]=1
    for j in range(i+1):
        if  arr[i] < arr[j] and d[i] < d[j] +1:
            d[i] = d[j] +1

print(max(d))