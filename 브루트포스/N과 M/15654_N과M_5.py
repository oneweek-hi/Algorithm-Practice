n,m = map(int, input().split())
number=list(map(int, input().split()))
number.sort()
check=[False]*n
select = [0,0,0,0,0,0,0,0,0] #고른 숫자들

# print(check)
def NandM (index, n, m):
    if index == m:
        for i in range(m):
            print(select[i], end=" ")
        print("")
        return

    for i in range (n):
        if check[i]: continue #이미 사용되었는지 체크
        check[i] = True
        select[index]=number[i]
        NandM(index+1, n ,m)
        check[i] = False


NandM (0, n, m)


#1과 거의 비슷하지만, 인덱스로 푸는게 아니라
#n의 종류가 입력된다는 차이점이 있다.
#그냥 Selected에 넣어주는 값만 바꾸어서 넣어주면 문제가 풀림!