n = int(input())

# int 숫자 두개 받기
n,m = map(int,input().split())

#한줄받기
a=list(map(int, input().split()))

#2차원 배열 입력 받기
a=[list(map(int,input().split())) for _ in range(n)]
a=[list(map(int,list(input()))) for _ in range(n)] #이방식으로 받으면 값에 0이 있어도 받아진다.

#빈 이차원 어레이 할당
empty2arr=[[0]*n for _ in range(n)] #앞쪽이 y 뒤쪽이 ㅌ
emptyArr= [0]*n

d = list(range(n)) #0~n 까지 리스트를 만들어줌 3을 넣으면, [0,1,2] 이런식으로

#a는 리스트로 받겠다는 의미
n, *a = list(map(int,input().split()))

#리스트 출력을 '3 4 5 6'이런 식으로할때
print(' '.join(map(str, a)))
print(' '.join(map(str,a)))

#그냥 줄바꿈 할때
print()

#프린트 하기
for i in range(n):
    print(' '.join(map(str, arr[i])))

#거꾸로 방문하기
def printtool(n, m):
    if n != m:
        printtool(n, place[m])
    print(m, end=" ")

printtool(n, m)


# extend와 append차이를 알아놔야 겠다

from collections import defaultdict

info= defaultdict(list)
for s1, s2 in friends:
    info[s1].append(s2)
    info[s2].append(s1)





