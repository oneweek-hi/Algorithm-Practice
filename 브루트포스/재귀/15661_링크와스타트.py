n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
result =100000000
def go(index,first,second):
    global result
    if index == n:
        t1 =0
        t2 =0
        lenfirst = len(first)
        lensecond =len(second)
        if lenfirst >1 and lensecond>1:
            for i in range(lenfirst):
                for j in range(lenfirst):
                    if i==j: continue
                    t1 += a[first[i]][first[j]]

            for i in range(lensecond):
                for j in range(lensecond):
                    if i == j: continue
                    t2 += a[second[i]][second[j]]
            result = min(result, abs(t1-t2))
            return

    if index < n:
        go(index+1,first+[index],second)
        go(index+1,first, second+[index])

go(0,[], [])
print(result)
