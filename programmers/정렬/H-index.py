#가져오기
#고민을 얼마나 했을지 궁금하다. 이해하는데 시간이 오래걸리긴 했지만 획기적인 방법이다.
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


#위의 문제에 대한 프로그래머스 설명 댓글
# 1) min(index,value) 부분은 가능할 수 있는 모든 h-index를 추출하는 부분
# 2) max(~) 값은 가능할 수 있는 모든 h-index 중 가장 큰 값을 추출하는 부분
#
# 예를들어 [6, 5, 4, 1, 0]의 경우에선
# min~ 부분은 min(1, 6), min(2, 5), min(3, 4), min(4, 1), min(5, 0)
# 즉 해당 인용수 이상의 논문개수와 해당 논문의 인용수 중 더 작은 숫자를 고르는 작업을 하고
# (h-index로 가능한 숫자 추출)
# max~부분은 앞에서 골라진 (1, 2, 3, 1, 0) 중 가장 큰 숫자를 뽑아 실제 h-index를 구하는 방법


#성공 1단계
#다른 것에 비해 상당히 쉽게 풀었다.
#n과 h가 헷갈려서 인용수를 리턴하는 줄 알았는데 그게 아니라 갯수가 중요했었다.
def solution(citations):
    citations.sort()
    for i in range (len(citations)):
        if citations[i] >= len(citations)-i:
            return len(citations)-i
    return 0

