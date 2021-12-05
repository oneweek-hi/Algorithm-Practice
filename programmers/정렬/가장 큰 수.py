#이건 이해가 잘안된다..
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

#성공 2단계 더 깔끔하게 풀려면 이렇게 하는게!
def solution(numbers):
    #0. key point
    # 1. 사전 값으로 정렬하기
    numbers_str = [str(num) for num in numbers]
    # 2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    numbers_str.sort(key=lambda num: num*3, reverse=True)

    return str(int(''.join(numbers_str)))

# #성공 1단계
# #그래도 num *3하는 것을 찾아 봐서 풀수 있었다.
# def solution(numbers):
#     answer = ''
#     string = [""] * len(numbers)
#     for i in range(len(numbers)):
#         string[i] = str(numbers[i])
#
#     # 소팅 기준이 바뀌는 거지 내용이 바뀌진 않음
#     string.sort(key=lambda num: num * 3, reverse=True)
#
#     for word in string:
#         answer += word
#     if int(answer) == 0:
#         return "0"
#
#     return answer