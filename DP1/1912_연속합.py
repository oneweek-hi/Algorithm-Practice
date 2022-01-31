n = int(input())
arr = list(map(int, input().split()))
d=[0]*n
d[0]=arr[0]

for i in range(1,n):
    if d[i-1]+arr[i] < arr[i]:
            d[i] = arr[i]
    else:
        d[i] = d[i-1]+arr[i]

print(max(d))