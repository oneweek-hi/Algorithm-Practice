n = int(input())

result = 0;
check =1
place=0

while n >= check:
    check *= 10
    place += 1
    if n > check-1: #10, 100, 1000 .. 보다 큰 경우 작은 자리수의 값을 계산
        result += ((check-1) - (check//10) + 1) * place
    else: #작은 경우 나머지 값 계산
        result += (n - (check//10)+1) * place
        print(result)
        break


#자릿수만 알아내면 되는 문제
#(1~9)*1 + (10~99)*2 + (100~999)*3 ... + 나머지
#를 구하는 방법으로 한다!
