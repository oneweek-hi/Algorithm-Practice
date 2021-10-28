MAX = 1000000;
d = [1]*(MAX+1) #각 숫자가 가진 약수의 합
s = [0]*(MAX+1) #누적해서 약수의 합을 더할 어레이

#d를 다 구하는 for문
for i in range(2, MAX+1):
    j = 1
    # 약수의 반대는 배수다. 그렇기 때문에 그 수보다 작은 배수를 각각 다 더해준다.
    while i*j <= MAX:
        d[i*j] += i
        j += 1

#이전 값에 새로운 값을 합쳐서 결과값 만들기
for i in range(1, MAX+1):
    s[i] = s[i-1] + d[i]

test = int(input())
testCase = []
for i in range (test):
    a = int(input())
    testCase.append(a)

for num in testCase:
    print(s[num])


#프린트를 이렇게 해도 된다.
# for _ in range(test):
#     a = int(input())
#     testCase.append(s[a])
#
# print('\n'.join(map(str, testCase)) + '\n')

#왜 pypy3로 하면 골인되고, 아니면 패스일까?