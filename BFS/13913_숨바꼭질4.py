from collections import deque
max=200000
a,b = map(int,input().split())
check=[False]*max
dist=[0]*max
place=[0]*max
result=[]

q = deque()
q.append(a)
check[a] = True
while q:
    now = q.popleft()
    if now == b:
        print(dist[b])
        break
    for nxt in [now+1, now-1, now*2]:
        if -1<nxt<max and not check[nxt]:
            q.append(nxt)
            check[nxt] = True
            dist[nxt] = dist[now]+1
            place[nxt] = now

result.append(b)
next = b
while next !=a:
    result.append(place[next])
    next = place[next]

for i in range(len(result)-1,-1,-1):
    print(result[i], end=' ')



# from collections import deque
# import sys
# MAX = 200000
# sys.setrecursionlimit(MAX)
# check = [False]*(MAX+1)
# dist = [-1]*(MAX+1)
# place = [0]*(MAX+1)
# n,m = map(int,input().split())
# check[n] = True
# dist[n] = 0
#
# def printtool(n, m):
#     if n != m:
#         printtool(n, place[m])
#     print(m, end=" ")
#
# q = deque()
# q.append(n)
# while q:
#     now = q.popleft()
#     for nxt in [now-1, now+1, now*2]:
#         if 0 <= nxt <= MAX and check[nxt] == False:
#             check[nxt] = True
#             dist[nxt] = dist[now] + 1
#             place[nxt] = now
#             q.append(nxt)
#
# print(dist[m])
# printtool(n,m)