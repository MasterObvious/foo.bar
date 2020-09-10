def solution(x, y):
    # Your code here
    count = 0
    x = int(x)
    y = int(y)

    while (x != 1 or y != 1):

        if x == 1:
            return str(count + y - 1)

        if y == 1:
            return str(count + x - 1)

        if x < y:
            if y % x == 0:
                return "impossible"

            n = y / x
            count = count + n
            y = y - x * n

        else:
            if x % y == 0:
                return "impossible"

            n = x / y
            count = count + n
            x = x - y * n

    return str(count)


print(solution(1000, 9997))
