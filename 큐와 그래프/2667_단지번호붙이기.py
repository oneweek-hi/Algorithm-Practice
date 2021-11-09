from collections import deque
dx =[0,0,1,-1]
dy =[1,-1,0,0]
ans=[]

def bfs(x,y,cnt):
    queue = deque()
    queue.append((x,y))
    check[x][y] = cnt
    count= 0
    while queue:
        x,y = queue.popleft()
        count +=1
        for i in range(4):
            calx = x +dx[i]
            caly = y +dy[i]
            if 0<= calx <n and 0<= caly < n:
                if a[calx][caly] ==1 and check[calx][caly] ==0:
                    queue.append((calx, caly))
                    check[calx][caly] = cnt
    ans.append(count)


n = int(input())
a=[list(map(int,list(input()))) for _ in range(n)]
check=[[0]*n for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        if a[i][j]==1 and check[i][j]==0:
            cnt += 1
            bfs(i,j,cnt)


ans.sort()
print(cnt)
print('\n'.join(map(str,ans)))