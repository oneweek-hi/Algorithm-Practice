n,m = map(int, input().split())
arr=[list(map(str,list(input()))) for _ in range(n)]
check=[["."]*m for _ in range(n)]
result=[]
max = max(n,m)
dx=[1,-1,0,0]
dy=[0,0,1,-1]


#십자가 찾기
for i in range(1,n-1):
    for j in range(1,m-1):
        if arr[i][j] == "*":
            count = 1
            while count < max:
                circle = 0
                for k in range(4):
                    i += dx[k]*count
                    j += dy[k]*count
                    if -1 < i < n and -1 < j < m:
                        if arr[i][j] == "*":
                            circle += 1
                    i -= dx[k]*count
                    j -= dy[k]*count

                if circle == 4:
                    result.append([i+1, j+1, count])
                else:
                    break
                count += 1



#결과값으로 check 어레이 만들기
for i in range(len(result)):
    x =result[i][0]-1
    y =result[i][1]-1
    count = result[i][2] +1
    check[x][y] = "*"
    for j in range(1, count):
        for k in range(4):
            x += dx[k] * j
            y += dy[k] * j
            check[x][y] = "*"
            x -= dx[k] * j
            y -= dy[k] * j


#두 어레이가 같은지 확인하기
printResult = True
for i in range(n):
    for j in range(m):
        if arr[i][j] != check[i][j]:
            printResult = False
            break



#결과 프린트 하기
if printResult:
    print(len(result))
    # 정렬은 선택
    result.sort(key=lambda x: (x[0], x[1],-x[2]))
    for i in range(len(result)):
        print(' '.join(map(str, result[i])))

else:
    print(-1)






