n=int(input())
f=int(input())
i=j=n//2

arr =[[0]*n for _ in range(n)]

count = 1
while count < (n*n+1):
    arr[i][j]=count

    #맨 윗줄
    if i ==0 and j < n-1:
        j +=1
    #맨 오른쪽
    elif i < n-1 and j == n-1:
        i +=1
    #맨 아래쪽
    elif i == n-1 and j>0:
        j -=1
    #맨 왼쪽
    elif j == 0 and i >0:
        i -=1

    #달팽이 그리기
    elif 0<i<n and 0<j<n:
        up = arr[i-1][j]
        down = arr[i+1][j]
        right = arr[i][j+1]
        left = arr[i][j-1]

        if count == 1:
            i -= 1
        elif up != 0:
            if right != 0:
                j -= 1
            elif left != 0:
                i += 1
            else:
                j -= 1
        elif down != 0:
            if right != 0:
                i -= 1
            elif left != 0:
                j += 1
            else:
                j += 1
        elif right != 0:
            i -= 1
        elif left != 0:
            i += 1

    count +=1

#출력
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
        if arr[i][j] == f :
            x = i
            y = j
    print(" ")

print(x+1,y+1)


