from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
m, n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
q = deque()
dist = [[-1]*m for _ in range(n)] #체크배열을 다 -1로 시작..!
for i in range(n):
    for j in range(m): #거리배열에 시작점을 0으로하고, 큐에 넣어줌 => BFC!! 이게 중요 더 큰경우를 가려내지 않아흑
        if a[i][j] == 1:
            dist[i][j] = 0
            q.append((i,j))
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m: #해당 범위인지 확인
            if a[nx][ny] == 0 and dist[nx][ny] == -1: #아직 닿지 않은 토마토들
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1

ans = max([max(row) for row in dist])
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and dist[i][j] == -1: #차마 익지 못한 토마토 가려내기
            ans = -1
print(ans)