def flippingMatrix(matrix):
    n = len(matrix) // 2
    max_sum = 0

    for i in range(n):
        for j in range(n):
            max_sum += max(
                matrix[i][j],
                matrix[i][2 * n - 1 - j],
                matrix[2 * n - 1 - i][j],
                matrix[2 * n - 1 - i][2 * n - 1 - j]
            )

    return max_sum


print(flippingMatrix([
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]))