n=int(input())
start_num=10**(n-1)
end_num= 10**n-1

check = [True]*(end_num+1)
check[0] = check[1] = False

for i in range(2, end_num+1):
    if check[i]:
        j = 2*i
        while j<=end_num:
            check[j] = False
            j +=i

def is_prime(x):
    if x<2:
        return False
    i=2
    while i*i<=x: #x를 루트하는 것보다 i를 제곱해줌
       if (x%i==0):
           return False
       i +=1

    return True

result=[]
while start_num <= end_num:
    if check[start_num]:
        inside = start_num//10
        count =0
        for i in range(n):
            if not check[inside]:
                break;
            else:
                count +=1
                inside = inside//10
        if count == n-1:
            result.append(start_num)
    start_num +=1

for i in range(len(result)):
    print(result[i])