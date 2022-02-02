n = int(input())
arr = list(map(int,input().split()))
d1 = [0]*n
d2 = [0]*n

#가장긴 증가하는 수열
for i in range(n):
    d1[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and d1[i] < d1[j] + 1:
            d1[i] = d1[j] + 1
# print(d1)

for i in range(n-1, -1, -1):
    d2[i] = 1
    for j in range(i+1, n):
        if arr[i] > arr[j] and d2[j]+1 > d2[i]:
            d2[i] = d2[j]+1

d = [d1[i]+d2[i]-1 for i in range(n)]
# print(d2)
# print(d)
print(max(d))