#!/usr/bin/python3
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque()
for _ in range(n):
    cmd, *val = input().split()
    if cmd == 'push':
        num = int(val[0])
        queue.append(num)
    elif cmd == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)


#!/usr/bin/python3   #어레이를 활용해서 인덱싱으로 구현
import sys
input = sys.stdin.readline
n = int(input())
queue = [0]*n
begin = 0
end = 0
for _ in range(n):
    cmd, *val = input().split()
    if cmd == 'push':
        num = int(val[0])
        queue[end] = num
        end += 1
    elif cmd == 'front':
        if begin == end:
            print(-1)
        else:
            print(queue[begin])
    elif cmd == 'size':
        print(end-begin)
    elif cmd == 'empty':
        if begin == end:
            print(1)
        else:
            print(0)
    elif cmd == 'pop':
        if begin == end:
            print(-1)
        else:
            print(queue[begin])
            begin += 1
    elif cmd == 'back':
        if begin == end:
            print(-1)
        else:
            print(queue[end-1])
