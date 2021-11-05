import sys
n = 20
m = int(sys.stdin.readline())
s = 0
for _ in range(m):
    op, *num = sys.stdin.readline().split()
    if len(num) > 0:
        x = int(num[0])-1
    if op == 'add':
        s = (s | (1 << x))
    elif op == 'remove':
        s = (s & ~(1 << x))
    elif op == 'check':
        res = (s & (1 << x))
        if res >   0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif op == 'toggle':
        s = (s ^ (1 << x))
    elif op == 'all':
        s = (1 << n) - 1
    else:
        s = 0

#여기서는 그냥 하면 안된다
#비트마스크 써야한다
#sys 공부를 좀 더 해야겠따