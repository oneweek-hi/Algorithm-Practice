#항상 배열을 돌때, 어디서 부터 어디까지 도는지 제대로 확인하자
#i와 j를 항상 제대로 확인해서 알맞는 타이밍에 업데이트 되는지 확인해야 한다.
#놓치는 부분이 없는지 확인하는게 제일 중요!


n = int(input())
a = [list(input()) for _ in range(n)]

def check(a):
    ans=1
    for i in range(n):
        cnt = 1
        dnt = 1
        for j in range(n-1):
            # print("[{}],[{}] 에서 <가로> => a[{}][{}]와 a[{}][{}] 비교, 현재 cnt={}".format(i, j, i, j, i, j+1, cnt))
            if a[i][j] == a[i][j+1]:
                cnt +=1
                # print("    같아서 들어옴, 현재 cnt={}".format(cnt))
                if cnt > ans:
                    ans= cnt
            else:
                # print("    달라서, cnt=1로 초기화")
                cnt =1

            # print()
            # if j==0:
            #     print("[{}],[{}] 에서 <세로> => a[{}][{}]={}와 a[{}][{}]{} 비교, 현재 dnt={}".format(i, j, i, j, a[i][j], i+1, j, a[i+1][j], dnt))

        for j in range(n - 1):
            if a[j][i] == a[j+1][i]:
                dnt +=1
                # if j == 0:
                #     print("    같아서 들어옴, 현재 dnt={}".format(dnt))
                if dnt > ans:
                    ans= dnt
            else:
                # if j == 0:
                #     print("    달라서, dnt=1로 초기화")
                dnt =1
            # print()

    return ans



#main
ans = 0
for i in range(n):
    for j in range(n):
        if j+1 < n:
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
            value = check(a)
            # print(i,j,value)
            if value> ans:
                # print(check(a))
                ans = value
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]

        if i + 1 < n:
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
            # print("second",i, j, check(a))
            if check(a)> ans:
                # print(check(a))
                ans = check(a)
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]

print(ans)

# 5
# YCPZY
# CYZZP
# CCPPP
# CYYZC
# CPPZZ


# print(check(a))

