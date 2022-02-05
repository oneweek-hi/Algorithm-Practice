from collections import defaultdict
from collections import deque


def solution(n, computers):
    d = [[0] * n for _ in range(n)]
    info = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                info[i].append(j)

    q = deque()
    q.append((0, 0))
    count = 1
    for i in range(n):
        for j in range(n):
            while q:
                x, y = q.popleft()
                print(info[x])
                for k in range(len(info[x])):
                    if d[x][info[x][k]] == 0:
                        d[x][info[x][k]] = 1
                        q.append((info[x][k], x))

            if d[i][j] != computers[i][j]:
                d[i][j] = 1
                q.append((i, j))
                count += 1

    return count



import collections

def solution(n, computers):
    deq = collections.deque()
    check = [0] * (n)
    count = 0
    while 0 in check:
        deq.append(check.index(0))
        while len(deq) != 0:
            current = deq.popleft()
            for j in range(n):
                if computers[current][j] == 1 and check[j] == 0:
                    check[j] = 1
                    deq.append(j)
        count += 1
    return count