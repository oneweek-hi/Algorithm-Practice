n = int(input())
arr = list(map(int, input().split()))
d=[1]*n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(max(d))
# print(d)

