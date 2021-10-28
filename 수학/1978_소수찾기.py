def is_prime(x):
    if x<2:
        return False
    i=2
    while i*i<=x:
       if (x%i==0):
           return False
       i +=1

    return True

test = int(input())
testcase = list(map(int, input().split()))
result =0
for i in range(test):
    if is_prime(testcase[i]):
        result +=1

print(result)

#소수를 찾을 때는 2~루트N 까지만 살펴 보면 된다.
#그걸 기준으로 함수를 만들어서 적용!
