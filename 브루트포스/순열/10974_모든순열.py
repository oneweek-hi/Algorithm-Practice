n = int(input())
a = list(range(1,n+1))


def find_next(a):
    # i 정하기
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:  # 0보다 작으면 마지막이라는 뜻이니깐 False 리턴
        return False

    # j 정하기
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    # 마지막으로 뒤집어 주기
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


while True:
    print(' '.join(map(str, a)))
    if not find_next(a):
        break
