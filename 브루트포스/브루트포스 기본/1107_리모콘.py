#맨 처음 생각
#주어진 숫자와 가장 작은 차이가 나게 숫자를 구한다
#그 다음 차이값을 구한다음 누른 버튼 수 + 차이값으로 계산한다.

def possible(c):
    if c == 0: # 나머지 계산이 안되는 경우 거르기
        if broken[0]:
            return 0
        else:
            return 1
    l = 0 #각 자리 수마다 다 일치하는 지 확인
    while c > 0:
        if broken[c%10]:
            return 0
        l += 1
        c //= 10
    return l


n = int(input())
m = int(input())
broken = [False] * 10
if m > 0:
    a = list(map(int,input().split()))
else:
    a = []
for x in a:
    broken[x] = True

ans = abs(n-100)# 기본 셋이 이해가 안됨
for i in range(0, 1000000+1):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c-n)
        if ans > l + press: #이동한 숫자와 +/- 버튼을 추가로 구해서 더해준 경우
            ans = l + press
print(ans)



