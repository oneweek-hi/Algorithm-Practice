n = int(input())
d = [0]*(n+1)
for i in range(1, n+1):
    d[i] = i #여기서 초기화
    j = 1
    while j*j <= i:
        if d[i] > d[i-j*j]+1:
            d[i] = d[i-j*j]+1
        j += 1
print(d[n])



# n=int(input())
# d=[0]*(n+1)
# if n ==1:
#     print(1)
# elif n==2:
#     print(2)
# elif n ==3:
#     print(3)
# else:
#     d[1]=1
#     d[2]=2
#     d[3]=3
#
#     for i in range(4,n+1):
#         count=1
#         number=[]
#         while count**2 <= i:
#             number.append(d[i-count**2]+1)
#             count +=1
#         d[i]=min(number)
#     print(d[n])

