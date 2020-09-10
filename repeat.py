def to_dec(n, b):
    result = 0

    n = n[::-1]

    for i in range(0, len(n)):
        result = result + (b ** i) * int(n[i])

    return result


def to_base(n, b, k):
    result = ['0'] * k
    for i in range(0, k):
        result[i] = str(n % b)
        n = n / b

    return ''.join(result)[::-1]


def solution(n, b):
    # Your code here

    seen = []
    k = len(n)

    while (n not in seen):
        seen.append(n)

        x_string = ''.join(sorted(n))
        y_string = ''.join(sorted(n, reverse=True))

        x = to_dec(x_string, b)
        y = to_dec(y_string, b)
        z = y - x
        n = to_base(z, b, k)

    return len(seen) - seen.index(n)
