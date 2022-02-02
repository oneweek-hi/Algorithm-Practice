n = int(input())
d = [0]*(n+1)
d[0] = 1
for i in range(2, n+1, 2):
    d[i] = d[i-2] * 3
    count = 4
    while count <= i:
        d[i] += (d[i - count] * 2)
        count += 2
print(d[n])

#짝수개로 늘어난다. 4, 6, 8. ...

#정답지 코드
n = int(input())
d = [0]*(n+1)
d[0] = 1
for i in range(2, n+1, 2):
    d[i] = d[i-2] * 3
    for j in range(i-4, -1, -2):
        d[i] += d[j] * 2
print(d[n])


# n =int(input())
# arr=[0]*(n+1)
# arr[1]=1
# if n > 1:
#     arr[2]=3
# if n > 2:
#     for i in range(3, n+1):
#         arr[i] = arr[i-1]
#         count = 2
#         while count < i:
#             arr[i] +=  (arr[i - count] *2)
#             count+=2
# print(arr[n])

