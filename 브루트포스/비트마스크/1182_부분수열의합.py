n,m = map(int,input().split())
a=list(map(int, input().split()))

ans = 0
#포함했는지 안했는지 그 자체를 확인하려고 각 숫자가 아니라 비트를 활용해서 전체 집합을 확인하는 것!
for i in range(1, (1<<n)): # 1부터 전체 집합까지 하나씩 증가
    sum = 0;
    for k in range(n):
        if i&(1<<k): #특정값이 현재 집합에 포함 되어있는지 확인하는 것
            sum += a[k]
    if sum == m:
        ans +=1

print(ans)
