from collections import deque
dx =[0,0,1,-1]
dy =[1,-1,0,0]
ans=[]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    check[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            calx = x +dx[i]
            caly = y +dy[i]
            if 0<= calx <n and 0 <= caly < m:
                if a[calx][caly] ==1 and check[calx][caly] == 0:
                    queue.append((calx, caly))
                    check[calx][caly] = check[x][y] + 1


n,m = map(int,input().split())
a=[list(map(int,list(input()))) for _ in range(n)]
check=[[0]*m for _ in range(n)]
bfs(0,0)
print(check[n-1][m-1])
# for i in range(n):
#     print()
#     for j in range(m):
#         print(check[i][j], end=" ")