n = int(input())
#벗뜨 파이썬은 재귀로 문제를 풀면 안된다....
memo = [0]*(n+1)

def go(n):
    if n == 1:
        return 0

    elif memo[n] > 0:
        return memo[n]

    else:
        memo[n] = go(n-1) + 1
        if n%2 == 0:
            temp = go(n//2)+1
            if memo[n] > temp:
                memo[n] = temp

        if n%3 == 0:
            temp = go(n//3)+1
            if memo[n] > temp:
                memo[n] = temp

        return memo[n]


print(go(n))
