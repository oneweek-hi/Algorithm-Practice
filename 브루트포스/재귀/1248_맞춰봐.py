n=int(input())
s=(input())
sign=[[0]*n for _ in range(n)]
cnt=0
ans= [0]*n
for i in range(n): #입력받은 값을 2차원 배열에 0, 1,-1 바꾸어서 저장 하는 함수
    for j in range(i,n): # continue를 안쓰더라도 이렇게 할 수 있다
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt +=1

def check(index): #정말 뭐하는 건지 잘 모르겠다! # 뒤에서 부터 구하면 합을 누적해서 구할 수 있다는데,,
    R = 0
    for i in range(index, -1, -1): #index부터 0까지 계산하는 것.
        print("ans[i]: ", ans[i])
        R += ans[i]
        if sign[i][index] == 0 :
            if R !=0:
                return False
        elif sign[i][index] < 0:
            if  R >=0:
                return False
        elif sign[i][index] > 0:
            if R <= 0:
                return False
    return True

def ok():
    for i in range(n):
        s =0
        for j in range(i,n): #i 부터 j의 합을 나타내는 것
            s += ans[j]
            if sign[i][j] ==0:
                if s != 0:
                    return False
            elif sign[i][j] > 0:
                if s <= 0:
                    return False
            elif sign[i][j] < 0:
                if s >= 0:
                    return False
    return True

#1-n의 수를 중복 가능하게 M개의 자리에 채우는 것
def go (index):
    if index == n:
        return ok()

    if sign[index][index] == 0:
        ans[index] =0
        return check(index) and go(index+1)

    for i in range(1, 11):
        ans[index] = sign[index][index]*i #부호 정해주려고 이렇게 한다!
        if check(index) and go(index+1):
            return True
    return False


go(0)
print(' '.join(map(str,ans)))


#이거는 다시 풀어야 한다. 이해가 안됨
