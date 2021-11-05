def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

while True:
    n, *a = list(map(int,input().split()))
    if n == 0:
        break
    d = [0] * 6 + [1] * (n - 6)
    while True:
        ans =[]
        for i in range (n):
            if d[i]==0:
                ans.append(int(a[i]))
        for i in range(5):
            print(ans[i], end=" ")
        print(ans[5])
        if not next_permutation(d):
            print() #이렇게 쓸 수 있는 것을 새로 배웠다
            break


#망할 출력 형식..
#아래 방법도 있는데 아직 익숙지 않다.
# while True:
#     n, *a = list(map(int,input().split()))
#     if n == 0:
#         break
#     d = [0]*(n-6)+[1]*6
#     ans = []
#     while True:
#         cur = [a[i] for i in range(n) if d[i] == 1]
#         ans.append(cur)
#         if not next_permutation(d):
#             break
#     ans.sort()
#     for v in ans:
#         print(' '.join(map(str,v)))
#     print()