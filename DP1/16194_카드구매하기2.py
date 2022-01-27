n= int(input())
arr=list(map(int, input().split()))
result =[100000000]*(n+1)
result[0] = 0

for i in range(1,n+1):
    for j in range(1,i+1):
        result[i] = min(result[i], result[i-j]+arr[j-1])

print(result[n])

