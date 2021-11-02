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
        # if check[i]: continue #이미 사용되었는지 체크
        # check[i] = True
        select[index]=i
        NandM(index+1, n ,m)
        # check[i] = False


NandM (0, n, m)

#N과M1 에서 중복 처리 하는 부분만 없애주면 된다.