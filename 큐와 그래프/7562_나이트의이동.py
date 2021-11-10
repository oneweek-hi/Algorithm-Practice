from collections import deque
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]

n = int(input())
for i in range(n):
    s = int(input())
    a1, a2 =map(int,input().split())
    b1, b2 = map(int, input().split())
    check = [[-1] * s for _ in range(s)]

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        check[x][y] = 0
        while queue:
            x,y = queue.popleft()
            for i in range(8):
                calx = x +dx[i]
                caly = y +dy[i]
                if 0 <= calx < s and 0 <= caly < s:
                    if check[calx][caly] == -1:
                        queue.append((calx, caly))
                        check[calx][caly] = check[x][y] + 1

    bfs(a1, a2)
    print(check[b1][b2])

#최단 거리 문제를 풀때는 그냥 check에 있는게 답이다!
#그리고 처음 배열을 -1로 하는 것도 좋은 방법 인것 같다!


# 1
# 8
# 0 0
# 7 0


# 1
# 100
# 0 0
# 30 50