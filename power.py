def solution(xs):
    # Your code here

    if (len(xs) == 1):
        return str(xs[0])

    total = 1

    xs = filter(lambda x: x != 0, xs)

    negatives = filter(lambda x: x < 0, xs)

    if (len(negatives) % 2 == 1):
        xs.remove(max(negatives))

    if len(xs) == 0:
        return str(0)

    for x in xs:
        total = total * x

    return str(total)


print(solution([-1]))
