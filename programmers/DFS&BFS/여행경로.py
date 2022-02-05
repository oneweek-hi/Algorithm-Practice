from collections import defaultdict
from collections import deque
#스택으로 푼 문제, 보고 풀었음
def solution(tickets):
    d = defaultdict(list)
    result = []
    for city1, city2 in tickets:
        d[city1].append(city2)
    for citys in d:
        d[citys].sort(reverse=True)

    stack = ["ICN"]
    while stack:
        city = stack[-1]
        if d[city] != []:
            stack.append(d[city].pop())
        else:
            result.append(stack.pop())

    print(result)
    return result[::-1]

#되기는 하지만 비효율적인 버전
# def solution(tickets):
#     d = defaultdict(list)
#     result=[]
#     for city1, city2 in tickets:
#         d[city1].append(city2)
#     for citys in d:
#         d[citys].sort(reverse=True)
#
#     q=deque()
#     q.appendleft("ICN")
#     while q:
#         city= q.popleft()
#         if city in d and d[city]:
#             q.appendleft(city)
#             q.appendleft(d[city].pop())
#         else:
#             result.append(city)
#
#
#     print(result)
#     return result[::-1]


#실패한 버전
# def solution(tickets):
#     d = defaultdict(list)
#     result=[]
#     for city1, city2 in tickets:
#         d[city1].append(city2)
#     for citys in d:
#         d[citys].sort(reverse=True)
#
#     q=deque()
#     q.appendleft("ICN")
#     while q:
#         city= q.popleft()
#         if city in d and d[city]:
#             q.appendleft(d[city].pop())
#         else:
#             print(q)
#             result.append(city)
#
#     print(result)
#     return result


# 첫번째 버전... 두개가 통과가 안됨.
# from collections import defaultdict
# from collections import deque
#
# def solution(tickets):
#     d = defaultdict(list)
#     result=["ICN"]
#     for city1, city2 in tickets:
#         d[city1].append(city2)
#     for citys in d:
#         d[citys].sort(reverse=True)
#
#     q=deque()
#     q.appendleft(("ICN", d["ICN"][-1]))
#
#     while q:
#         before, after = q.popleft()
#         d[before].pop()
#         result.append(after)
#         if len(d[after]) !=0:
#             q.appendleft((after, d[after][-1]))
#
#     return result