n = int(input())
arr =list(map(int, input().split()))
d=[0]*n
d[0] = arr[0]

for i in range(1,n):
    d[i] = arr[i]
    for j in range(i+1):
        if d[i] <= d[j]+arr[i] and arr[j] < arr[i]:
            d[i] = d[j]+arr[i]

print(max(d))