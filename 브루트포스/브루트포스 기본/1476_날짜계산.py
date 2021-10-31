E, M, S = map(int, input().split())
e=0
m=0
s=0
i=1
while True:
    e+=1
    m+=1
    s+=1
    if(e==16):
        e=1
    if(m==29):
        m=1
    if(s==20):
        s=1

    if e==E and m==M and s==S:
        print(i)
        break

    i+=1
