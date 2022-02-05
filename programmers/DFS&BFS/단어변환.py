from collections import deque

#2번째 버전
def solution(begin, target, words):
    wordlen = len(begin)
    d = [0] * len(words)
    q = deque()
    q.append((begin, 0))

    while q:
        word, value = q.popleft()
        for i in range(len(words)):
            count = 0
            for j in range(wordlen):
                if words[i][j] != word[j]:
                    count += 1
            if count == 1 and d[i] == 0:
                d[i] = value + 1
                if words[i] == target:
                    return d[i]
                q.append((words[i], d[i]))
    return 0


#1번째 버전
def wordchecker(word, compare):
    count = 0
    for i in range(len(word)):
        if word[i] == compare[i]:
            count += 1
    if count == len(word) - 1:
        return True
    return False


def solution(begin, target, words):
    beginlen = len(begin)
    if not target in words:
        return 0

    weight = [-1] * len(words)

    q = deque()
    for i in range(len(words)):
        if wordchecker(begin, words[i]):
            weight[i] = 1
            q.append(i)

    while q:
        new = q.popleft()
        word = words[new]
        if word == target:
            return weight[new]

        for i in range(len(words)):
            if wordchecker(word, words[i]) and weight[i] == -1:
                weight[i] = weight[new] + 1
                q.append(i)

    return 0