def solution(phone_book):
    # 성공 4단계_ zip를 이용해서 두개씩 한번에 하는 방법
    phone_book.sort()
    for p1, p2 in zip( phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

#     성공 3단계 _코드보고옴 발생의 전환으로
#     긴거에서 하나씩 뺀게 짧은 거랑 같나를 확인함.. 신박하다
#     phone_book.sort()
#     dict = {}
#     for num in phone_book:
#         dict[num]=0

#     for number in dict:
#         temp=""
#         for p in number:
#             temp += p
#             if temp in dict and temp != number:
#                 return False
#     return True

# 실패 2단계
#     phone_book.sort()
#     real = len(phone_book)
#     for i in range(real):
#         dict = {}
#         check = len(phone_book[i])
#         for j in range(i+1,real):
#             dict[phone_book[j][0:check]] = 0

#         if phone_book[i] in dict:
#             return False
#     return True

# 실패 1단계
# answer = True
# for i in range(len(phone_book)):
#     check= len(phone_book[i])
#     compare=phone_book[i]
#     for j in range(len(phone_book)):
#         if (compare!=phone_book[j]):
#             if compare == phone_book[j][0:check]:
#                 return False
# return True