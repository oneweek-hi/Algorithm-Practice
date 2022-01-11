#실패 코드
n,m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
print(n*m)
print(arr)

x=0
y=0
count =0

for i in range(n*m):
    print("here")
    #맨위
    if x == 0:
        arr[x][y]=1
        if y == m-1:
            x+=1
            count += 1
        else:
            y+=1

    #맨 오른쪽
    elif y == m-1:
        print("222222222222222")
        arr[x][y]=1
        if x == n-1:
            y -=1
            count += 1

        else:
            x += 1

    #맨 아래
    elif x == n-1:
        print("33333333333333")
        arr[x][y] = 1
        if y == 0:
            x -= 1
            count += 1

        else:
            y -=1

    #맨 왼쪽
    elif y==0:
        print("444444444")
        arr[x][y] = 1
        if  arr[x-1][y] == 1:
            y += 1
            count +=1
        else:
            x -=1

    #상,좌
    elif arr[x-1][y] == 1 and arr[x][y-1] == 1:
        print("5555555555")
        arr[x][y] = 1
        if arr[x][y+1] == 1:
            print("check111")
            x +=1
            count +=1
        else:
            print("check22222")
            y +=1

    #상, 우
    elif arr[x-1][y] == 1 and arr[x][y+1] == 1:
        print("666666666")
        arr[x][y] = 1
        if arr[x+1][y] == 1:
            y +=1
            count +=1
        else:
            x +=1

    #하, 우
    elif arr[x+1][y] == 1 and arr[x][y+1] == 1:
        print("77777777777")
        arr[x][y] = 1
        if arr[x][y-1] == 1:
            x -=1
            count +=1
        else:
            y -=1

    #하, 좌
    elif arr[x+1][y] == 1 and arr[x][y-1] == 1:
        print("888888888")
        arr[x][y] = 1
        if arr[x+1][y] == 1:
            y -=1
            count +=1
        else:
            y+=1

    # else:
        # print("check:" ,i)

print(count)

for i in range(n):
    print(' '.join(map(str, arr[i])))


