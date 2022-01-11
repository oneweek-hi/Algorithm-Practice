n,m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
dx=[0,1,0,-1] #우, 하, 좌, 상
dy=[1,0,-1,0]

x = y = mode = count = result = 0
arr[0][0]=1


while count != n*m-1:
    if -1< x+dx[mode] <n and -1< y+dy[mode] <m:
        if arr[x+dx[mode]][y+dy[mode]] != 0:
            mode = (mode + 1) % 4
            result += 1

        x += dx[mode]
        y += dy[mode]
        arr[x][y] = 1
        count += 1

    # 범위에 안들어가면 방향바꾸기
    else:
        mode = (mode+1)%4
        result +=1


print(result)