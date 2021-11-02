n,m,k = map(int, input().split())
value = [list(map(int,input().split())) for _ in range(n)]

vx=[0,0,1,-1] # 오, 왼, 아래, 위
vy=[1,-1,0,0]
result = 0

def cal(depth):
    for i in range(n):
        for j in range(m):
            for p in range(4):
                if value[i+vx[p]][j+vy[p]]

