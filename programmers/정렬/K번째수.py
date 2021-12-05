#성공 2단계
#한번에 i,j,k를 받아서 할 수가 있다!
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer


#성공 1단계
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = array[(commands[i][0])-1:commands[i][1]]
        temp.sort()
        answer.append(temp[commands[i][2]-1])

    return answer