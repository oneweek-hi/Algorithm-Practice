n=int(input())

head = ['2','3','5','7']
tail = ['1','3','5','7','9']

def is_prime(x):
    if x<2:
        return False
    i=2
    while i*i<=x: #x를 루트하는 것보다 i를 제곱해줌
       if (x%i==0):
           return False
       i +=1

    return True

def find_prime(x):
    if len(x) == n:
        print(x)
        return

    for i in range(5):
        if is_prime(int(x+tail[i])):
             find_prime(x+tail[i])

for i in range(4):
    find_prime(head[i])



