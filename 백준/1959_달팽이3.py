n,m = map(int, input().split())
count = result= 0

while n>2 and m>2:
    n -=2
    m -=2
    count +=1
    result += 4

x = y = count+1

#아래 처럼 하면 for문을 돌리지 않아도 되서 시간을 단축할 수 있다.
# d = (min(n, m) - 1) // 2
# ans = 4*d
# row = 1+d
# col = 1+d
# n -= 2*d
# m -= 2*d

if n == 1:
    y += (m-1)

elif m == 1:
    result +=1
    x +=( n-1)

elif n == 2:
    result += 2
    x +=1

elif m == 2:
    result +=3
    x +=1



print(result)
print(x,y)