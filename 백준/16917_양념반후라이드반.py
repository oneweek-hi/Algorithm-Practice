a, b, c, x, y = map(int,input().split())
#기본값
defalut = a*x + b*y
min=min(x, y)
max=max(x, y)

#반반을 섞었을때 최소값
cal =  c * min * 2 + a * (x-min) +b * (y-min)
if defalut > cal:
    defalut = cal

#반반으로만 했을 때
if defalut <(c*max*2):
    print(defalut)
else:
    print(c*max*2)


