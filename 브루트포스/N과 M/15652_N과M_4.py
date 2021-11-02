n,m = map(int, input().split())
select = [0,0,0,0,0,0,0,0,0,0] #고른 숫자들 넣는 것

def NandM (index, start, n, m):
    if index == m:
        for i in range(m):
            print(select[i], end=" ")
        print("")
        return

    for i in range (start ,n+1):
        select[index]=i
        NandM(index+1, i, n ,m)

NandM (0, 1, n, m)

# 비오름차순 + 중복허락
# N과M_2에서 중복이 가능 할 수 있도록
# start를 자신을 포함해서 살 수 있도록 한다!