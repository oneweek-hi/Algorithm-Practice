n=int(input())
numbers= [0]*n
for i in range(n):
    numbers[i]=int(input())

m = int(max(numbers))
arr = [0]*(m+1)

arr[1]=1
if m > 1:
    arr[2]=2
if m > 2:
    arr[3]=4
if m > 3:
    for i in range(4,m+1):
        arr[i]= (arr[i-1]+arr[i-2]+arr[i-3]) % 1000000009

for i in range(n):
    print(arr[numbers[i]])