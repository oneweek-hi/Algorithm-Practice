n = int(input())
arr = list(map(int, input().split()))
d=[1]*n
f=[-1]*n

def bprint(i):
    if f[i] != -1:
        bprint(f[i])
    print(arr[i],end=" ")

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            f[i] = j


result = max(d)
check=0
for i in range(n):
    if d[i] == result:
        check=i
        break

print(result)
bprint(check)





# 16
# 277 730 790 994 242 185 633 545 830 557 194 994 44 28 755 661