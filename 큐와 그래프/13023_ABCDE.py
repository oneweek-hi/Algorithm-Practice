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

#어렵다..
#생각을 해보면 DFS로 depth구하는 방법밖에 안떠오른다. 근데 이것도 코드로 구현하자니..아찔..!


# https://security-nanglam.tistory.com/531