n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
ans =  100000000
for i in range((1<<n)):# 전체 집합 돌기
    first = []
    second = []
    for j in range(n): #모든 경우의 수를 다 넣고
        if (i&(1<<j)) > 0:
            first += [j]
        else:
            second += [j]
    if len(first) != n//2: #여기서 길이가 안되면 컨티뉴로 다시 처음!
        continue
    t1 = 0
    t2 = 0
    for l1 in range(n//2): #여기서 각 팀의 능력치를 계산해줌
        for l2 in range(n//2):
            if l1 == l2:
                continue
            t1 += s[first[l1]][first[l2]]
            t2 += s[second[l1]][second[l2]]
    diff = abs(t1-t2)
    if ans > diff:
        ans = diff
print(ans)


#비트마스크로 풀었다고 시간이 단축되거나 그러지는 않았다.
