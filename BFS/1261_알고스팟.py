from collections import deque

n,m = map(int, input().split())
arr = [list(map(int,list(input()))) for _ in range(m)]
check =[[0]*n for _ in range(m)]
check[0][0]=1

print(check)
print(arr)
dx=[1,0,-1,0]
dy=[0,1,0,-1]

x = deque()
y = deque()
x.append(0)
y.append(0)

while x:
    nowX = x.popleft()
    nowY = y.popleft()
    # print(nowX, nowY)
    for i in range(4):
        # print("check11")
        nxtX = nowX + dx[i]
        nxtY = nowY + dy[i]
        if -1< nxtX < m and -1< nxtY<n and check[nxtX][nxtY] == -1:
            if arr[nxtX][nxtY] == 0: #벽이 없을때
                check[nxtX][nxtY] = check[nowX][nowY]
                x.appendleft(nxtX)
                y.appendleft(nxtY)

            else:
                check[nxtX][nxtY] = check[nowX][nowY]+1
                x.append(nxtX)
                y.append(nxtY)


print(check[m-1][n-1])
for i in range(m):
    print(' '.join(map(str, check[i])))