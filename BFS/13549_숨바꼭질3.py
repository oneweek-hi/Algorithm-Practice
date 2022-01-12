from collections import deque
max=200000
a,b = map(int,input().split())
check=[False]*max
dist=[0]*max

q = deque()
q.append(a)
check[a] = True

while q:
    now = q.popleft()
    if now ==b:
        print(dist[b])

    if -1< now*2 < max:
        if not check[now * 2]:
            q.appendleft(now*2)
            check[now * 2] = True
            dist[now * 2] = dist[now]

    if -1< now +1 < max:
        if not check[now+1]:
            q.append(now+1)
            check[now+1] = True
            dist[now+1] = dist[now]+1

    if -1< now-1 < max:
        if not check[now - 1]:
            q.append(now - 1)
            check[now - 1] = True
            dist[now - 1] = dist[now] + 1
