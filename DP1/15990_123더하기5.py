n=int(input())
numbers= [0]*n
for i in range(n):
    numbers[i]=int(input())

m = int(max(numbers))
arr=[[0]*(m+1) for _ in range(3)]

arr[0][1] = 1
arr[0][3] = 1
arr[1][2] = 1
arr[1][3] = 1
arr[2][3] = 1

for i in range(4,m+1):
    arr[0][i]=(arr[1][i-1]+arr[2][i-1]) % 1000000009
    arr[1][i]=(arr[0][i-2]+arr[2][i-2]) % 1000000009
    arr[2][i]=(arr[0][i-3]+arr[1][i-3]) % 1000000009


# for i in range(n):
#     print(' '.join(map(str, arr[i])))


for i in range(n):
    print((arr[2][numbers[i]]+arr[0][numbers[i]]+arr[1][numbers[i]])%1000000009)

# 파이썬은 정수의 길이에 한정이 없어서 중간에 한번씩 나누어 줘야한다.
# 또한 마지막에도 필수로 나눠줘야 한다...!

