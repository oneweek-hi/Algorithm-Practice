def solution(clothes):
    answer = 1
    dict = {}
    for something in clothes:
        if something[1] in dict:
            dict[something[1]] += 1
        else:
            dict[something[1]] = 1

    for value in dict.values():
        answer *= (value + 1)

    return answer - 1

# 저번에 지희랑 지원이랑 알고리즘 스터디 할때
# 풀었었는데 기억이 하나도 안나더라
# 각각 옷 갯수에 1더해주고 곱한다음에 1빼면 된다
# 그 종류의 옷을 안입을 수도 있으니깐 1더해주고, 아예 안입는 경우 1빼주고!