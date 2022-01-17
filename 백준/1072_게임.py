all, win = map(int, input().split())

start = 0
end = 1000000000
firstwinRate= (win*100//all)

if 99 <= firstwinRate:
    print(-1)
else:
    while(start <= end):
        mid = (start + end)//2
        # print(start, end, mid)
        winRate = (win+mid)*100//(all+mid)
        if winRate > firstwinRate:
            end = mid - 1

        else:
            start= mid +1

    print(start)