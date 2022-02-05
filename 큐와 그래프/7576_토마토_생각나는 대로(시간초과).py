from collections import deque
dx =[0,0,1,-1]
dy =[1,-1,0,0]


#초반 아이디어 생각을 잘못해서
#스파게티 코드가 되었다.
#최단 거리 문제는 무조건 DFS&BFS, 제대로 된 DFS&BFS!!!!
#이 문제는 시작점이 여러군데에 있으니, 일단 모두 큐에 넣고 시작하는게 맞았고,
#-1로 둘러싸일 경우에는 의도치 않게 check 배열에서 0이 발생할 수 있다.
#뒤늦게 예외 처리를 하면 이렇게 시간 초과가 걸리게 된다...ㅠㅠ흑흑
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    check[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            calx = x +dx[i]
            caly = y +dy[i]
            if 0<= calx <n and 0 <= caly < m: #범위 설정
                if a[calx][caly] == -1:
                    check[calx][caly] =-1

                elif check[calx][caly] > check[x][y] + 1: #보다 가까운 쪽
                    queue.append((calx, caly))
                    check[calx][caly] = check[x][y] + 1

                elif a[calx][caly] == 0 and check[calx][caly] == 0: #안 익어 있는 토마토,
                    queue.append((calx, caly))
                    check[calx][caly] = check[x][y] + 1


m,n = map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
check=[[0]*m for _ in range(n)]

do= False
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            do = True
        if a[i][j] == -1:
            check[i][j] =-1

if do:
    for i in range(n):
        for j in range(m):
            if a[i][j]==1 and check[i][j]==0:
                bfs(i,j)


    ans = max([max(row) for row in check]) -1
    for i in range(n):
        for j in range(m):
            if check[i][j] == 0:
                # print("check")
                ans = -1
else:
    ans= 0
print(ans)
