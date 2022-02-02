n = int(input())
arr=[0]*n
for i in range(n):
    arr[i]= int(input())
d=[0]*n
if n ==1:
    print(arr[0])
elif n ==2 :
    print(arr[1]+arr[0])
# elif n ==3 :
#     print(max(arr[1]+arr[0], arr[1]+arr[2], arr[2]+arr[0]))
#     #왜 안해도 되는 걸까? #파이썬이라서 -1값이 들어가도 0이기 때문에 괜찮은 것이다!
else:
    d[0] = arr[0]
    d[1] = arr[1]+arr[0]
    # d[2] = max(arr[1]+arr[0], arr[1]+arr[2], arr[2]+arr[0])

    for i in range(2,n):
        print(d[i-3])
        d[i]= max(d[i-1], d[i-2]+arr[i],d[i-3]+arr[i-1]+arr[i])

    print(d[n-1])





# 이차원 배열로 푼 경우
# d=[[0]*3 for _ in range(n+1)]
# for i in range(1,n+1):
#     d[i][0]=max(d[i-1][0],d[i-1][1],d[i-1][2])
#     d[i][1] =d[i-1][0]+arr[i-1]
#     d[i][2] =d[i-1][1]+arr[i-1]
#
# print(max(d[n]))