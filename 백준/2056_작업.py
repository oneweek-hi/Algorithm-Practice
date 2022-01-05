n=int(input())
time = [0]*n #각 번호의 길이
for i in range(n):
    a = list(map(int, input().split()))
    alen = len(a)
    if i == 0 :
        time[i] = a[0]

    else:
        big = 0
        for j in range(2, alen):
            if time[a[j]-1] > big:
                big = time[a[j]-1]
        time[i] = big + a[0]

print(max(time))

