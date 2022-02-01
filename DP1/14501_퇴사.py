#이해하기 정말 어려웠당...
#day1 부터 7까지 간다음에 거기서 부터 꺼꾸로 계산하면서 거슬러 올라온다..
inf = 10**9
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
d = [-1]*(n+1)
for i in range(1, n+1):
    t[i],p[i] = map(int,input().split())
ans = 0
def go(day):
    if day == n+1: #크기가 넘겼을때
        return 0
    if day > n+1: # day 넘어가는 날짜 나왔을 때 0 아니게 하려고
        return -inf

    if d[day] != -1: #메모리 쓰려고!
        return d[day]

    # print("day: ,",day,"d: ", d)
    t1 = go(day+1) # x
    # print("day1111: ,", day, "d: ", d, "t1: ," ,t1)
    t2 = p[day] + go(day+t[day]) # o
    # print("day22222: ,", day, "d: ", d)
    d[day] = max(t1,t2)
    # print("day33333: ,", day, "d: ", d)
    return d[day]

print(go(1))
print(d)


#그냥 재귀로 푼 경우
# inf = -10**9
# n = int(input())
# t = [0]*(n+1)
# p = [0]*(n+1)
# for i in range(1, n+1):
#     t[i],p[i] = map(int,input().split())
# ans = 0
# def go(day, s):
#     global ans
#     if day == n+1:
#         ans = max(ans, s)
#         return
#     if day > n+1:
#         return
#     go(day+1, s)
#     go(day+t[day], s+p[day])
#
# go(1, 0)
# print(ans)