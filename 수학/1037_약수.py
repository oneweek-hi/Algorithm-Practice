n = int(input())
aliquot = list(map(int,input().split()))

print(min(aliquot) * max(aliquot))

# 1, n을 제외한 나머지 모든 약수를 가지고 n을 찾는 문제
# 모든 숫자는 루트n를 기준으로 짝지어져 있다.
# 그렇기 때문에 가장 큰 수와 가장 작은 숫자를 서로 짝지을 수 있다.
# 두개를 곱하면 n을 구할 수 있는 것.