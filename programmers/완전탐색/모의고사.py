#가져오기
#사이클 함수를 쓰면 알아서 돌려주나 보다..!
from itertools import cycle
def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]


#성공 1단계
#일단 풀어서 다행이다.. 그거면 됐다.
#간단하게 풀었다
def solution(answers):
    num1 = "12345"
    num2 = "21232425"
    num3 = "3311224455"
    count = [0] * 3

    for i, some in enumerate(answers):
        if num1[i % 5] == str(some):
            count[0] += 1

        if num2[i % 8] == str(some):
            count[1] += 1

        if num3[i % 10] == str(some):
            count[2] += 1

    sd = max(count)
    answer = []
    for i, some in enumerate(count):
        if some == sd:
            answer.append(i + 1)

    return answer