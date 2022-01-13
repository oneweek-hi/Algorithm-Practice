from collections import deque
n = int(input())
arr = [list(map(str, list(input()))) for _ in range(n)]
check=[[-1]*n for _ in range(n)]
check2=[[-1]*n for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

q=deque()
count =0
for i in range(n):
    for j in range(n):
        if check[i][j] == -1:
            count += 1
            q.append((i,j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nxtX = x + dx[k]
                    nxtY = y + dy[k]
                    if -1 < nxtX < n and -1 < nxtY < n:
                        if check[nxtX][nxtY] == -1 and arr[x][y] == arr[nxtX][nxtY]:
                            check[nxtX][nxtY] = 1
                            q.append((nxtX, nxtY))

for i in range(n):
    for j in range(n):
        if arr[i][j]== "R":
            arr[i][j] = "G"

q2=deque()
count2 =0
for i in range(n):
    for j in range(n):
        if check2[i][j] == -1:
            count2 += 1
            q2.append((i,j))
            while q2:
                x, y = q2.popleft()
                for k in range(4):
                    nxtX = x + dx[k]
                    nxtY = y + dy[k]
                    if -1 < nxtX < n and -1 < nxtY < n:
                        if check2[nxtX][nxtY] == -1 and arr[x][y] == arr[nxtX][nxtY]:
                            check2[nxtX][nxtY] = 1
                            q2.append((nxtX, nxtY))

print(count,count2)











