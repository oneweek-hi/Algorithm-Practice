def go(sum, goal):
    if sum > goal: return 0 #합이 n보다 큰 경우(불가능한 경우)
    if sum == goal: return 1 # 한개의 정답을 찾은 경우
    now =0
    for i in range(1,4): #1~3까지의 경우의 수를 구하기 위해
        now += go(sum+i, goal) #총 정답의 갯수를 여기서 구함
    return now


n= int(input())
for i in range(n):
    a = int(input())
    print(go(0,a))
