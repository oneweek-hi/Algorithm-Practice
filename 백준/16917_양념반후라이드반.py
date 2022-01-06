a, b, c, x, y = map(int,input().split())
defalut = a*x + b*y
min=0
max=0
if x>y:
    max =x
    min =y
else:
    max =y
    min =x

#기준
for i in range(1, min+1):
    cal = 0
    cal += c * i * 2
    cal += a * (x-i)
    cal += b * (y-i)
    if defalut > cal:
        defalut = cal

if defalut <(c*max*2):
    print(defalut)
else:
    print(c*max*2)


