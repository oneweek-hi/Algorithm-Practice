n,m,k = map(int, input().split())
value = [list(map(int,input().split())) for _ in range(n)]
check = [[False]*10 for _ in range(10)]
dx=[0,0,1,-1] # 오, 왼, 아래, 위
dy=[1,-1,0,0]
result = -2147483547 #정답
# go(cnt, sum) cnt: 선택한 칸의 갯수, sum: 선택한 칸의 합

def go(startX, startY, cnt, sum):
    global result #로컬에서 쓸려면 global선언을 해줘야 한다.
    if cnt == k: #재귀 탈출조건, 선택한 갯수와 선택해야하는 갯수가 같을 때!
        if result < sum:
            result = sum
        return
    for x in range(startX,n): #중복을 없애기 위해 X열 부터!
        for y in range((startY if x==startX else 0),m): #X열의 어느 부분인 Y부터 시작하기 위해
            if check[x][y]: continue #뽑혔는지 안뽑혔는지 확인하는 것
            ok = True
            for i in range(4):
                nx = x +dx[i]
                ny = y +dy[i]
                if 0 <= nx and nx < n and 0 <= ny and ny<m: #범위기 넘어가는지 아닌지
                    if check[nx][ny]:
                        ok = False #Ok는 선택 가능한 것인지 아닌지를 체크하는 것
            if ok:
                check[x][y] = True
                go(x,y,cnt+1, sum+value[x][y])
                check[x][y] = False

go(0,0,0,0)
print(result)

# 고민을 했지만, 어려워서 설명을 듣고도 코드 구현을 하지 못했던 문제
# 코드를 보면 이해는 가지만 처음부터 스스로 짜는 연습이 필요할듯 하다.