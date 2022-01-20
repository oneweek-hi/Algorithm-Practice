from collections import defaultdict
n = int(input())
arr = list(map(int, input().split()))
start = 0
dict = defaultdict(list)

for i in range(n):
    #딕셔너리 값채우기
    na3= 0
    if arr[i]%3 == 0:
        na3 = arr[i]//3
        if na3 in arr and not na3 in dict:
            dict[na3] = arr[i]
    kob2 = arr[i]*2

    if kob2 in arr and not kob2 in dict:
        dict[kob2] = arr[i]

    #처음 시작값 찾기
    if not na3 in arr and not kob2 in arr:
        start = arr[i]


#딕셔너리에서 거꾸로 프린트하기
def printtool(llen, n, m):
    if llen != n:
        printtool(llen,n+1, dict[m])
    print(m, end=" ")

printtool(n,1,start)