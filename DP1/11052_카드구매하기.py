n= int(input())
arr=list(map(int, input().split()))
result =[0]*(n+1)
result[1] = arr[0]
for i in range(n):
    