#근의 공식을 활요해서 푼 것
import math
def solution(brown, yellow):
    answer = []
    b = (-(brown - 4)) / 2;
    x = (math.sqrt(b * b - 4 * yellow) - b) / 2;
    y = yellow / x;

    answer.append(x + 2);
    answer.append(y + 2);
    return answer