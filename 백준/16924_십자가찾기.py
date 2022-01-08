n,m = map(int, input().split())
arr=[list(map(str,list(input()))) for _ in range(n)]
check=[[False]*m for _ in range(n)]
result=[]
max = max(n,m)
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(1,n-1):
    for j in range(1,m-1):
        # print(i,j)
        if arr[i][j] == "*":
            count = 1
            while count < max:
                circle = 0
                for k in range(4):
                    i += dx[k]*count
                    j += dy[k]*count
                    if -1 < i < n and -1 < j < m:
                        if arr[i][j] == "*":
                            circle += 1
                    i -= dx[k]*count
                    j -= dy[k]*count

                if circle == 4:
                    result.append([i+1, j+1, count])
                count += 1


if len(result) ==0 :
    print(-1)
else:
    print(result)






