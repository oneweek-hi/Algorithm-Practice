n=int(input())
memo =[0]*(n+1)
for i in range(2, n+1):
    memo[i] = memo[i-1] + 1
    if i % 2 == 0:
        temp = memo[i // 2] + 1
        if memo[i] > temp:
            memo[i] = temp

    if i % 3 == 0:
        temp = memo[i // 3] + 1
        if memo[i] > temp:
            memo[i] = temp

print(memo[n])