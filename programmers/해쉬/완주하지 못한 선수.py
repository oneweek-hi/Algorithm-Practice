def solution(participant, completion):
    # 성공 4단계_ 길이가 하나밖에 차이가 안난다는 점이 중요점으로 작용했다!
    # python 카운터도 공부해야겠다.
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

    # 성공 3단계_ 딕셔너리의 value값을 이용해서 중복문제 해결
    #     dict = {}
    #     for name in participant:
    #         if dict.get(name):
    #             dict[name] += 1
    #         else:
    #             dict[name] = 1

    #     for name in completion:
    #         dict[name] -= 1

    #     for key in dict:
    #         if dict[key] > 0:
    #             return key


    # 실패 2단계_ 아래로직을 똑같이 딕셔너리로 만들었는데 왜 안되는지 이해가 안됐다
    #           하지만, 딕셔너리는 중복키가 안되어서 삭제한다는 게 다 삭제되는 것이기 때문에
    #           아래 처럼 풀수가 아예 없는 것이다 => 아예 잘못된 방법
    #     dictionary = {string : 0 for string in completion}
    #     for someone in participant:
    #         if someone in dictionary.keys():
    #             del dictionary[someone]
    #         else:
    #             ans = someone

    # 실패 1단계_ 한번 그냥 생각나는 대로 바로 풀었다. 정답은 맞지만 효율성 통과 못함
    # for someone in participant:
    #     if someone in completion:
    #         completion.remove(someone)
    #     else:
    #         ans = someone
    #
    # return ans