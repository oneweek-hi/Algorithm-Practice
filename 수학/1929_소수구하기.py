MAX = 1000000;
check = [0]*(MAX+1)
check[0] = check[1] = True

##에라토스테네스의 체 만들기
for i in range(2, MAX+1):
    if not check[i]:
        j = 2*i
        while j<=MAX:
            check[j] = True
            j +=i  #자기를 계속더하면 자기로 나눠짐

a,b = map(int, input().split())
for i in range(a, b+1):
    if not check[i]:
        print(i)







#에라토스테네스의 체
#2부터 N 까지의 모든 수를 써 놓는다.
#아직 지워지지 않는 수 중에서 가장 작은 수를 찾는다.
#그 수는 아직 소수이다.
#이제 그 수의 배수를 모두 지운다.
