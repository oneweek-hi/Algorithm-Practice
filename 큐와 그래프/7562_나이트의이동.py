from collections import deque
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]



n = int(input())
for i in range(n):
    s = int(input())
    a1, a2 =map(int,input().split())
    b1, b2 = map(int, input().split())
    print("s: ", s, "a1, a2: ",a1,a2,"b1,b2: ", b1,b2)
    check = [[0] * n for _ in range(n)]

    count =0
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        check[x][y] = 1
        while queue:
            x,y = queue.popleft()
            global count
            count += 1
            for i in range(8):
                calx = x +dx[i]
                caly = y +dy[i]
                if calx == b1 and caly == b2:
                    count += 1
                    print("here")
                    break
                if 0<= calx <n and 0 <= caly < n:
                    if check[calx][caly] == 0:
                        queue.append((calx, caly))
                        check[calx][caly] = check[x][y] + 1

    bfs(a1, a2)
    print(count)

# 1
# 8
# 0 0
# 7 0


# 1
# 100
# 0 0
# 30 50