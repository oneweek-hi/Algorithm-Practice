n = int(input())
b = int(input())
broken = [False] * 10
if b > 0 :
    numbers = list(map(int, input().split()))
else:
    numbers =[]

for i in numbers:
    broken[i]=True


#그 채널로 이동이 가능한지 아닌지를 체크하는 함수!
def checker(a):
    if a == 0:
        if broken[a]:
            return 0 # 이동이 불가능하면 0
        else:
            return 1 # 이동이 가능하면 버튼 누르는 갯수 리턴

    result = 0
    cal = a
    while cal > 0:
        if broken[cal%10]:
            return 0
        else:
            cal//=10
            result += 1
    return result


# main
ans = abs(n-100)
for i in range(1000000):
    press = checker(i)
    if press > 0:
        if ans > abs(n-i) + press:
            ans = abs(n-i) + press

print(ans)


#이동할 채널 c를 구한다
#c에 포함되어 있는 숫자 중에 고장난 버튼이 있는지 확인한다
#고장난 버튼이 없으면 절대값을 구해서 +/-를 계산한다.


# 이해가 어려웠던 부분
# 딱 맞는 최소한의 값을 구하는게 아니라 백만 가지 숫자를 각각 다 최소값을 구해서
# 그 중에 제일 잘 맞는 값을 구하는 것이다!!!!!~~~!!


#직전 위에도 잘못 이해했음...
#그냥 갈 수 있는 채널을 다 찾아서 그중에서 제일 조금 움직이는 걸로 가는거임...
#바보야 변수이름좀 잘 확인하자..제발...