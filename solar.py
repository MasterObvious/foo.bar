from math import sqrt


def solution(area):

    remainder = area
    result = []
    while (remainder > 0):

        next_square = int(sqrt(remainder))
        next_square = next_square * next_square
        remainder = remainder - next_square

        result.append(next_square)

    return result


print(solution(15324))
