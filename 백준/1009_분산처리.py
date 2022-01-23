
n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    a = arr[i][0]**arr[i][1]
    print(a%10)