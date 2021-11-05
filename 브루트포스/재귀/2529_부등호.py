n=int(input())
a = list(map(str, input().split()))
ans =[]
check =[False] *10

# def ok(num):
#     for i in range(n):
#         if a[i] == '<': # 조건을 반대로 써서 알맞지 못한 경우 False를 리턴 하도록 하였다.
#             if num[i] > num[i+1]: #내 생각과는 다르게 직전 값들만 알맞은지 확인하면 다 차례대로 맞다.
#                 return False
#         elif a[i] == '>':
#             if num[i] < num[i+1]:
#                 return False
#     return True

def good (x ,y, op):
    #이때 비교를 숫자로써 하는게 아니라 문자열로 비교하는 것 같다.
    if op == "<":
        if x > y : return False
    if op == ">":
        if x < y : return False
    return True

def go(index, num):
    if index == n+1:
        # if ok(num): #항상 통과 하기 전에 조건을 마지막으로 확인해 준다.
        # print("here")
        ans.append(num)
        return

    for i in range(10): #0~까지 다 넣을려고
        if check[i]: #중복이 안되는지 확인하기 위해
            continue
        if index == 0 or good(num[index-1], str(i), a[index-1]): # 스트링으로 형변환
            # print(index)
            check[i] = True
            go(index + 1, num +str(i))
            check[i] = False


go(0,"")
ans.sort()
# print(ans)
print(ans[-1]) #최댓값 출력
print(ans[0]) #최소값 출력


#1단계로 통과했을 때
#머리가 안돌아가서 그냥 인강보고 했다
#브루트포스 형식은 똑같은 것 같다.
#끝나는 조건과 함수 호출을 하는 조건을 설정하고
#끝날 때 문제의 조건을 한번더 확인하고 마친다.


#2단계로 통과했을 때
#1단계에서 불필요한 부분들을 없애기 위해 34번째 줄을 추가하였다
#비교할때 문자열로 비교하는 것이라서 str()로 i를 바꾸어줘야 한다
#-'0' 씨에서는 이렇게 하는데... 그걸 고새 까먹어서..ㅠㅠㅋㅋㅋ
#뭐하는건지 이해 하느라 시간이 걸렸다