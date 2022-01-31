n= int(input())
arr=[[0]*10 for _ in range(n+1)]
arr[1][1]=arr[1][2]=arr[1][3]=arr[1][4]=arr[1][5]=arr[1][6]=arr[1][7]=arr[1][8]=arr[1][9]= 1

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            arr[i][j] = arr[i-1][1] % 1000000000
        elif j == 9:
            arr[i][j] = arr[i-1][8]% 1000000000
        else:
            arr[i][j] = (arr[i-1][j+1] + arr[i-1][j-1]) % 1000000000

#
# for i in range(n):
#     print(' '.join(map(str, arr[i])))

print(sum(arr[n]) % 1000000000)