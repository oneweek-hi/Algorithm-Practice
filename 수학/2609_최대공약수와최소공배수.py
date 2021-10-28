a,b = map(int, input().split())

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

# def lmc(g,x,y):
#     return g*(x/g)*(y/g)

x = gcd(a,b)
print(x)
print(a*b//x) #함수를 따로 만들지 않고 이렇게 바로 구할 수 있다.
# print(int(lmc(x,a,b)))

#유클리드 호제법
#a를 b로 나눈 나머지를 r이라고 했을 때
#최대공약수: GCD(a,b) = GCD(b,r)과 같다.
#최소공배수: LCM(a,b) = G*(A/G)*(B/G)
