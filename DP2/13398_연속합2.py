n = int(input())
arr = list(map(int, input().split()))
d1=[0]*n
d1[0]=arr[0]
d2=[0]*n
d2[n-1]=arr[n-1]
d=[0]*n

if n == 1:
    print(arr[0])
else:
    for i in range(1,n):
        if d1[i-1]+arr[i] < arr[i]:
                d1[i] = arr[i]
        else:
            d1[i] = d1[i-1]+arr[i]

    for i in range(n-2, -1, -1):
        if d2[i+1]+arr[i] > arr[i]:
                d2[i] = d2[i+1]+arr[i]
        else:
            d2[i] = arr[i]

    for i in range(n):
        if i == 0:
            d[0]=d2[1]
        elif i == n-1:
            d[n-1]=d1[n-2]
        else:
            d[i] = d1[i-1]+d2[i+1]

    # print(d1)
    # print(d2)
    print(max(max(d1),max(d)))
    # print(max(d))

#
# n = int(input())
# a = list(map(int,input().split()))
# d = [0]*n
# dr = [0]*n
# for i in range(n):
#     d[i] = a[i]
#     if i == 0:
#         continue
#     if d[i] < d[i-1] + a[i]:
#         d[i] = d[i-1] + a[i]
# for i in range(n-1, -1, -1):
#     dr[i] = a[i]
#     if i == n-1:
#         continue
#     if dr[i] < dr[i+1] + a[i]:
#         dr[i] = dr[i+1] + a[i]
# ans = max(d)
# for i in range(1, n-1):
#     if ans < d[i-1] + dr[i+1]:
#         ans = d[i-1] + dr[i+1]
# print(ans)
#
