from collections import deque
n,m,start = map(int,input().split())
a = [[] for _ in range(n+1)] #인접리스트


check = [False] * (n+1)
for _ in range(m):
    u,v = map(int,input().split()) #인접리스트에 각각의 값 넣어주기
    a[u].append(v)
    a[v].append(u)
for i in range(1, n+1):
    a[i].sort()

def dfs(x): #스텍 방법을 샤용하기 때문에 재귀를 사용한다.
    global check
    check[x] = True
    print(x, end=' ')
    for y in a[x]:
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n+1)
    q = deque()
    q.append(start)
    check[start] = True
    while q: #큐가 비어 있을 때 까지
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]: #a[x]에 들어있는 값을 모두 방문
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()