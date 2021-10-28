while True:
    try:
        n = int(input())
    except:
        break

    num =0
    i = 1

    while True:
        num = (num * 10 + 1) % n
        if num == 0:
            print(i)
            break
        i +=1

# 그냥 단순히 나누면 숫자가 너무 커질 수도 있기 때문에
# (A+B)%M = (A%M + B%M) % M 공식을 사용해서 배수는 작게 만들지 않는다.
# 11= (1 x 10 + 1) %7 = ((1%7)x10 +1)%7 = 11 %7 = 4
# 111=(11 x 10 +1) % 7 = ((11%7)x10+1)%7 = 41%7 = 6 ...
