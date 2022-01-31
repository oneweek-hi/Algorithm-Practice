n=int(input())
arr=[[0]*2 for _ in range(n+1)]

if n ==1:
    print(1)
elif n ==2:
    print(1)

elif n ==3:
    print(2)

else:
    arr[1][1] =1
    arr[2][0] =1
    arr[3][0] =1
    arr[3][1] =1

    for i in range(4, n+1):
        arr[i][0] = arr[i-1][0] + arr[i-1][1]
        arr[i][1] = arr[i-1][0]

    print(sum(arr[n]))