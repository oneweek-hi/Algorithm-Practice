n,m = map(int, input().split())
check = [False]*10 #이전에 쓰였는지 안쓰였는지 체크하는 배열
select = [0,0,0,0,0,0,0,0,0,0] #고른 숫자들

def NandM (index, n, m):
    if index == m:
        for i in range(m):
            print(select[i], end=" ")
        print("")
        return

    for i in range (1,n+1):
        if check[i]: continue #이미 사용되었는지 체크
        check[i] = True
        select[index]=i
        NandM(index+1, n ,m)
        check[i] = False


NandM (0, n, m)

#결정: 위치가 중요하다
#같은 숫자를 뽑아도 순서에 따라서 다양한 답이 나오기 때문이다.
