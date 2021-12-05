#성공 4단계
#로직은 같은데 더 간단하게 풀 수 있는 방법
def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
            dic2[g] = p
        else:
            dic1[g].append((i, p))
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]: #두개까지만 나오도록 슬라이싱
            answer.append(i)
    return answer

#성공 3단계
#그나마 익숙해 지려고 소팅하는 부분만 가져와서 추가해본 코드
# from collections import defaultdict
# from operator import itemgetter
# def solution(genres, plays):
#     answer = []
#     dict = {}
#     playlist = {}
#     for i in range(len(genres)): #장르 가장 인기많은 것과 장르 목록을 dict으로 만드는 것
#         if genres[i] in dict:
#             dict[genres[i]] += plays[i]
#             playlist[genres[i]].append([int(plays[i]),i])
#         else:
#             dict[genres[i]] = plays[i]
#             playlist[genres[i]] = [[int(plays[i]),i]]

#     sDict = sorted(dict, key=lambda x: dict[x], reverse=True) #소트해서 저장
#     answer = []
#     for genre in sDict:
#         one_genre_list = sorted(playlist[genre], key=itemgetter(0), reverse=True)
#         print(one_genre_list)
#         print(one_genre_list)
#         if len(one_genre_list) > 1:
#             answer.append(one_genre_list[0][1])
#             answer.append(one_genre_list[1][1])
#         else:
#             answer.append(one_genre_list[0][1])
#     return answer

#성공 2단계 정답을 찾고 싶어서 블로그 가서 찾아봄. 가장 작은 숫자 1,0을 찾는데 소팅을 사용했다.
#다양한 라이브러리를 많이 사용해서 새로운 걸 많이 배웠지만 당장 적용 시키기에는 어렵게 느껴짐.
# from collections import defaultdict
# from operator import itemgetter #다중 수준 정렬
# def solution(genres, plays):
#     genre_play_dict = defaultdict(lambda: 0) #딕셔너리 기본값 설정
#     for genre, play in zip(genres, plays): #장르별 재생횟수 찾기
#         genre_play_dict[genre] += play
#
#     genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=itemgetter(1), reverse=True)]
#     final_dict = defaultdict(lambda: [])
#
#     for i, genre_play_tuple in enumerate(zip(genres, plays)): # enumerate: 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
#         final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))
#     # for문 값이 이렇게 넘어온다.
#     # 0('classic', 500)
#     # 1('pop', 600)
#     # 2('classic', 150)
#     # 3('classic', 800)
#
#     answer = []
#     for genre in genre_rank:
#         one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True) #다중
#         if len(one_genre_list) > 1:
#             answer.append(one_genre_list[0][1])
#             answer.append(one_genre_list[1][1])
#         else:
#             answer.append(one_genre_list[0][1])
#     return answer


    # 실패 1단계
    # 노답코드... 나도 노답인거 알고 그냥 계속 짰는데 그마저도 답조차 다 통과 하지 못한다.
    # 빠드린 경우의 수를 아직 못찾겠다. 추가를 계속하더라도 1,2,4,8,9,11,12,15를 통과하지 못한다.
    #
    # answer = []
    # dict = {}
    # playlist = {}
    # for i in range(len(genres)): #장르 가장 인기많은 것과 장르 목록을 dict으로 만드는 것
    #     if genres[i] in dict:
    #         dict[genres[i]] += plays[i]
    #         playlist[genres[i]].append([i, int(plays[i])])
    #     else:
    #         dict[genres[i]] = plays[i]
    #         playlist[genres[i]] = [[i, int(plays[i])]]
    #
    # sDict = sorted(dict, key=lambda x: dict[x], reverse=True) #소트해서 저장
    #
    # for p in sDict: #인덱스을 찾기 위한 for문
    #     first = 0
    #     first_index = 0
    #     second = 0
    #     second_index = 0
    #     for d in playlist[p]:
    #         if d[1] > first:  # 1보다 큰 경우: 1/2 둘다 바꾸기
    #             second = first  # 2값을 1값으로
    #             first = d[1]  # 1값을 새로운 값으로
    #             second_index = first_index  # 인덱스도 마찬가지
    #             first_index = d[0]
    #
    #         elif d[1] == first and d[1] == second:  # 셋다 같은 경우
    #             if d[0] < first_index:  # 첫번째 인덱스보다 작을 경우
    #                 second_index = first_index
    #                 first_index = d[0]
    #
    #             elif d[0] < second_index:
    #                 second_index = d[0]
    #
    #         elif d[1] < first and d[1] > second:  # 중간인 경우
    #             second = d[1]
    #             second_index = d[0]
    #
    #         elif d[1] == second:  # 2와 해당 값이 같을 경우
    #             if d[0] < second_index:
    #                 second_index = d[0]
    #
    #     answer.append(first_index)
    #     answer.append(second_index)
    #
    # return answer
