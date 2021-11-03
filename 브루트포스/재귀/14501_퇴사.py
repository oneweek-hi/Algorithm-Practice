n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

result = 0
def go(day, sum):
    global result
    if day == n:
        if sum > result: # 이걸 완성 된 경우에만 해야한다. 정답을 찾은 경우만
            result = sum #모든 경우에서 다하니깐 에러가 나는 것! # result = max(result, sum)
        return
    if day > n:
        return

    go(day+a[day][0] , sum + a[day][1])#상담을 할경우
    go(day + 1 , sum)#상담을 안할 경우

go(0, 0)
print(result)