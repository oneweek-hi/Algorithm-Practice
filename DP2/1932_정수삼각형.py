n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
d=[[0]*n for _ in range(n)]
d[0][0]=arr[0][0]
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            d[i][j] = arr[i][j] + d[i-1][j]
        elif j == len(d[i-1])-1:
            d[i][j] = arr[i][j] + d[i-1][j-1]
        else:
            d[i][j]= arr[i][j] + max(d[i-1][j-1],d[i-1][j])

print(max(d[n-1]))

