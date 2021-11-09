n,m = map(int,input().split()) # 정점의 갯수, 간선의 갯수
a = [[] for _ in range(n+1)] #인접리스트


check = [False] * (n+1)
for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)

def dfs(x):
    global check
    check[x] = True
    for y in a[x]:
        if check[y] == False:
            dfs(y)

count = 0
for i in range(1,n+1):
    if not check[i]:
        count +=1
        dfs(i)

print(count)
