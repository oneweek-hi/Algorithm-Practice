n = int(input())
a=[]

def find(a):
    if a == 1:
        return 1
    if a == 2:
        return 2
    if a == 3:
        return 4
    else:
        return find(a-1) + find(a-2) + find(a-3)

for i in range(n):
    value = int(input())
    print(find(value))

#재귀로 어떻게 풀어야 했는지 몰랐는데,
#점화식을 세워서 더하는 방식으로 풀면 되었다!
#다음부턴 각각의 경우의 수를 더 잘 계산해보자!