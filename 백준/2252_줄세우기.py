from collections import deque
from collections import defaultdict
n,m = map(int, input().split())

a=[list(map(int,input().split())) for _ in range(m)]
check=[0]*n
dict = defaultdict(list)
fdict = defaultdict(list)

q = deque()

for i in range(m):
    if not a[i][1] in dict:
        dict[a[i][1]] = [a[i][0]]
        fdict[a[i][0]] = [a[i][1]]

    else:
        dict[a[i][1]].append(a[i][0])

result = []
# print(dict)
for k in list(dict):
    if check[k-1] == 0 and len(result) != n :
        q.append(k)
        while q:
            val = q.popleft()
            for i in range(len(dict[val])):
                if check[dict[val][i]-1] == 0:
                    check[dict[val][i]-1] = 1
                    q.appendleft(dict[val][i])
            result.append(val)

# print(result)
for i in range(len(result)-1,-1,-1):
    print(result[i], end=" ")

