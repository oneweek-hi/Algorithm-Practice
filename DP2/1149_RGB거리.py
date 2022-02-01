n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

d= [[0]*3 for _ in range(n+1)]
d[1][0]=arr[0][0]
d[1][1]=arr[0][1]
d[1][2]=arr[0][2]

# for i in range(n+1):
#     print(' '.join(map(str, d[i])))

for i in range(2,n+1):
    d[i][0]= arr[i-1][0]+min(d[i-1][1],d[i-1][2])
    d[i][1]= arr[i-1][1]+min(d[i-1][0],d[i-1][2])
    d[i][2]= arr[i-1][2]+min(d[i-1][0],d[i-1][1])

print(min(d[n]))


