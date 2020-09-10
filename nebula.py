from collections import defaultdict


def gen_next_state(c1, c2, n):
    a = c1 & ~(1 << n)
    b = c2 & ~(1 << n)
    c = c1 >> 1
    d = c2 >> 1
    return (a & ~b & ~c & ~d) | (~a & b & ~c & ~d) | (~a & ~b & c & ~d) | (~a & ~b & ~c & d)


def get_successors(n, nums):
    successors = defaultdict(set)
    nums = set(nums)

    for i in range(2 ** (n+1)):
        for j in range(2 ** (n+1)):
            next_state = gen_next_state(i, j, n)

            if next_state in nums:
                successors[(next_state, i)].add(j)

    return successors


def solution(g):
    # transpose
    g = list(zip(*g))
    ncols = len(g[0])

    num_representation = [sum([2 ** i if col else 0 for i, col in enumerate(row)])
                          for row in g]

    possible_successors = get_successors(ncols, num_representation)

    previous_columns = {i: 1 for i in range(2 ** (ncols+1))}
    for col in num_representation:
        next_columns = defaultdict(int)

        for c1 in previous_columns:
            for c2 in possible_successors[(col, c1)]:
                next_columns[c2] += previous_columns[c1]

        previous_columns = next_columns

    ret = sum(previous_columns.values())
    return ret


print(solution([[True, False, True], [
      False, True, False], [True, False, True]]))
