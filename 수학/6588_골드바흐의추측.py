MAX = 1000000;
check = [0]*(MAX+1)
check[0] = check[1] = True
prime = []

for i in range(2, MAX+1):
    if not check[i]:
        prime.append(i)
        j = 2*i
        while j<=MAX:
            check[j] = True
            j +=i

prime =prime[1:]
while True:
    n = int(input())
    if n == 0:
        break
    for p in prime:
        if check[n-p] == False:
            print("{0} = {1} + {2}".format(n, p, n-p))
            break

#출력결과가 입력과 번갈라 나와도 통과가 되는걸 새로 배웠다!
#먼저 소수를 구하고
#그 다음에 받는 값을 빼서 소수인지 확인하는 방식!