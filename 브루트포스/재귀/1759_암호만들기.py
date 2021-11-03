n,m = map(int,input().split())
a = list(map(str, input().split()))
a.sort()

def check(password): #모음이 한개 이상, 자음이 두개 이상인걸 체크하기 위해
    ja=0
    mo=0
    for x in password:
        if x in 'aeiou':
            mo +=1
        else:
            ja +=1
    return ja >= 2 and mo >= 1

def go(length, alpha, pw, i):
    if len(pw) == length: #길이가 똑같으면 끝날 조건
        if check(pw):
             print(pw)
        return
    if i == alpha: #절대 답이 안나올 경우
        return 0

    go(n, alpha, pw + a[i], i + 1)#선택
    go(n, alpha, pw, i+1)#선택 안했을 때


go(n,m,"",0)