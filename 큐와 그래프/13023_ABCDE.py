import sys
n,m = map(int,input().split())
edges = [] #간선 리스트 (모든 간선의 목록)
a = [[False]*n for _ in range(n)] #인접행렬
g = [[] for _ in range(n)] #인접리스트

#값 채우기
for _ in range(m):
    u, v = map(int,input().split())
    edges.append((u,v))
    edges.append((v,u))
    a[u][v] = a[v][u] = True
    g[u].append(v)
    g[v].append(u)
m *= 2
for i in range(m):
    for j in range(m):
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not a[B][C]:
            continue
        for E in g[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            sys.exit(0)
print(0)


#DFS로 푼문제
import sys

n, m = map(int, input().split())
arr = [[] for i in range(n)]
visited = [False] * n

# 그래프를 인접 리스트 방식으로 표현하였습니다.
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(idx, number):
    if number == 4:
        print(1)
        exit()
    for i in arr[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False

# 노드를 순서대로 방문하며 dfs를 수행합니다.
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)