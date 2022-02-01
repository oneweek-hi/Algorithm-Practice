n= int(input())
arr=[[1]*10 for _ in range(n+1)]
if n == 1:
    print(10)
else:
    for i in range(2,n+1):
        for j in range(1,10):
            # arr[i][j] = arr[i-1][j]%10007 + arr[i][j-1]%10007
            arr[i][j]=(sum(arr[i-1][:j+1]))%10007

    print((sum(arr[n]))%10007)
    for i in range(n+1):
        print(' '.join(map(str, arr[i])))




