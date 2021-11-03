n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
result =100000000
def go(index,first,second):
    global result
    if index == n:
        t1 =0
        t2 =0
        if len(first) == n//2:
            for i in range(n//2):
                for j in range(n//2):
                    if i==j: continue
                    t1 += a[first[i]][first[j]]
                    t2 += a[second[i]][second[j]]
            result = min(result, abs(t1-t2))
            return

    if len(first)> n//2:
        return
    if len(second)> n//2:
        return

    if index < n:
        go(index+1,first+[index],second)
        go(index+1,first, second+[index])

go(0,[], [])
print(result)
