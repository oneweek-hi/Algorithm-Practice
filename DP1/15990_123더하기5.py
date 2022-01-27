n=int(input())
numbers= [0]*n
for i in range(n):
    numbers[i]=int(input())

m = int(max(numbers))
arr=[[0]*(m+1) for _ in range(3)]

arr[0][1] = 1
arr[1][1] = 1
arr[2][1] = 1
# for i in range(n):
#     print(' '.join(map(str, arr[i])))
print(arr[1][-2])
for i in range(2,m+1):
    arr[0][i]=arr[1][i-2]+arr[2][i-3]
    arr[1][i]=arr[0][i-1]+arr[2][i-3]
    arr[2][i]=arr[0][i-1]+arr[1][i-1]

for i in range(n):
    print(' '.join(map(str, arr[i])))


for i in range(n):
    print(arr[2][numbers[i]]+arr[0][numbers[i]]+arr[1][numbers[i]])