# n = int(input())
# a=[list(map(int,input().split())) for _ in range(n)]
# result = 2147483647
# ans=[]
#
# # 4 1 2 3
# def go(index,ans, num):
#     global result
#     if index == n: #종료 조건
#         if not a[ans[index-1]][ans[0]] == 0: #마지막에서 처음으로 가는 것
#             num += a[ans[index-1]][ans[0]]
#             if num < result:
#                 result = num
#         return
#
#     if len(ans) == 0:
#         go(index + 1, ans + [0], num)
#         return
#
#     for i in range(1,n):
#             if a[ans[index-1]][i] != 0:
#                 if i not in ans: # 중복체크
#                     go(index+1, ans+[i], num+a[ans[index-1]][i])
#
#
# go(0, ans, 0)
# print(result)
#
# #기본 방식을 기반으로 문제를 풀었다
# #간과한점
# # 1. 연결 관계가 0일 경우를 생각못함
# # 2. 마지막에서 처음으로 연결 하는 경우 생각 못함
# # 3. 마지막에서 처음으로 연결 하는 경우가 0일 수도 있다는 생각을 못함
# # 4. ans의 중복 검사를 안함
# # 근데 이건 브루트 포스 이긴 하지만, 순열 방법으로 푼게 아니다..!

#순열로 풀면 시간이 짧게 걸리지만 아래의 함수가 항상 필요하다!
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

n = int(input())
w = [list(map(int,input().split())) for _ in range(n)]
d = list(range(n))
ans = 2147483647
while True:
    if d[0] != 0: break
    ok = True
    s = 0
    for i in range(0, n-1):
        if w[d[i]][d[i+1]] == 0: #주어진 순열이 이동 가능 한지 확인
            ok = False
            break
        else:
            s += w[d[i]][d[i+1]]
    if ok and w[d[-1]][d[0]] != 0: #이동 가능하고 마지막에서 처음으로 갈때도 0인지 확인
        s += w[d[-1]][d[0]]
        ans = min(ans, s)
    if not next_permutation(d): #이렇게 조건문에 사용해도 다음것으로 자연스럽게 실행되는게 신기하다
        break
print(ans)