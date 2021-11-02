n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    M = a[i][0]
    N = a[i][1]
    X = a[i][2]
    Y = a[i][3]
    result = (X-1)
    while result < N*M:
        if(result % N == (Y-1)):
            print(result+1)
            break
        result += M
        # print(result)
    else:
        print(-1)

# 모든 경우의 수는 NM인데 너무 크다.
# x:y의 값들에 마이너스 1을 하면 나머지 관련 방법으로 풀 수 있다
# 그럼 O(N)의 방법으로 풀 수 있다.
# x의 값을 고정 시키고 푸는 것!



    # result=0
    # x=0
    # y=0
    # while True:
    #     result +=1
    #     x += 1
    #     y += 1
    #     if x == X and y == Y:
    #         print(result)
    #         break
    #
    #     if(result > 1000000):
    #         print(-1)
    #         break
    #
    #     if (x == M):
    #         x = 0
    #     if (y == N) :
    #         y = 0

