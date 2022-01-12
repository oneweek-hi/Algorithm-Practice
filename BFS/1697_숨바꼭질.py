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
        break
    for nxt in [now+1, now-1, now*2]:
        if -1<nxt<max and not check[nxt]:
            q.append(nxt)
            check[nxt] = True
            dist[nxt] = dist[now]+1


