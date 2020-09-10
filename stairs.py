def solution(n):
    # Your code here

    memoization = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    memoization[0][0] = 1

    for height in range(1, n+1):
        for bricks in range(0, n+1):
            memoization[height][bricks] = memoization[height - 1][bricks]

            if bricks >= height:
                memoization[height][bricks] += memoization[height -
                                                           1][bricks - height]

    return memoization[n][n] - 1


print(solution(5))
