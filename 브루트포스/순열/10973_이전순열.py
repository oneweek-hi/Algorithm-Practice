n = int(input())
a = list(map(int, input().split()))


def find_next(a):
    # i 정하기 계속 작아지다가 갑자기 커지는 것
    i = len(a) - 1
    while i > 0 and a[i - 1] <= a[i]: #여기랑
        i -= 1
    if i <= 0:   # 0보다 작으면 마지막이라는 뜻이니깐 False 리턴
        return False

    # j 정하기
    j = len(a) - 1
    while a[j] >= a[i - 1]: #여기랑 부등호 방향 차이 밖에 없음..ㅠㅠ 어렵네..
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    # 마지막으로 뒤집어 주기
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


if find_next(a):
    print(' '.join(map(str, a)))
else:
    print(-1)
