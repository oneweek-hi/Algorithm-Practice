# n,m = map(int, input().split())
# select = [0,0,0,0,0,0,0,0,0,0] #고른 숫자들 넣는 것
#
# def NandM (index, start, n, m):
#     if index == m:
#         for i in range(m):
#             print(select[i], end=" ")
#         print("")
#         return
#
#     for i in range (start ,n+1):
#         select[index]=i
#         NandM(index+1, i+1, n ,m)
#
# NandM (0, 1, n, m)

#위의 코드 설명
#아까 것이랑 거의 비슷하지만, 오름차순으로 설정하기 위해
#이전 다음부터 시작 하도록 index+1를 설정하는 것이다!
#인덱스를 설정해 주었기 때문에, 중복된 결과가 나올 수가 없어서 체크를 없앴다.


n,m = map(int, input().split())
a = [0,0,0,0,0,0,0,0,0,0] #고른 숫자들 넣는 것

def NandM (index, selected, n, m):
    if selected == m:
        for i in range(0, m):
            print(a[i], end=" ")
        print("")
        return
    if index > n: return

    a[selected] = index
    #선택했을 경우
    NandM(index+1, selected+1, n, m)
    # a[selected] =0 ->없어도 되는 코드
    #선택하지 않았을 경우
    NandM(index+1, selected,n,m)


NandM (1, 0, n, m) # 그 위치를 선택했냐 안헀냐기 때문에 1 부터 시작!
#바로 직전 코드 설명
#여기서는 선택을 했냐 안했냐가 중요하다
#즉, 오름차순이기 때문에
#뽑은 숫자는 순서가 바뀌지 않고 오름차순으로 그대로 쓰인다
#재귀함수가 숫자를 선택 했을 경우, 안했을 경우로 나누어서 호출하여
#문제를 해결한다.
