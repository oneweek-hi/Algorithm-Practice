import sys
sys.setrecursionlimit(1000000)
s = int(sys.stdin.readline())

for i in range(s):
    n,m = map(int,sys.stdin.readline().split()) # 정점의 갯수, 간선의 갯수
    a = [[] for _ in range(n+1)] #인접리스트

    check = [0] * (n+1)
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        a[u].append(v)
        a[v].append(u)


    def dfs(node, c):
        # print("dfs:", node, c)
        global check
        check[node] = c
        for y in a[node]:
            # print("확인하는 숫자:",y)
            if check[y] == 0:
                # print("처음 방문")
                if not dfs(y, 3 - c):
                    return False
            elif check[y] == c:
                # print("이분 그래프가 아닐 경우")
                return False
        # print("맞을 경우")
        return True

    ans = True
    for i in range(n):
        if check[i] == 0:
            if not dfs(i, 1):
                ans = False
    print('YES' if ans else 'NO')