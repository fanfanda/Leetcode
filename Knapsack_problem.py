def Knapsack(w, v, capacity):
    memo = [[0 for j in range(capacity + 1)] for i in range(len(w) + 1)]
    # for i in range(len(memo)):
    #     memo[i][0] = 0
    # for i in memo:
    #     print(i)
    for i in range(1, len(w) + 1):
        for j in range(1, capacity + 1):
            if j < w[i - 1]: memo[i][j] = memo[i - 1][j]
            else: memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - w[i - 1]] + v[i - 1])
            print(memo[i][j], end = ' ')
        print()
    return memo[len(w)][capacity]
# def Knapsack(w, v, capacity):
#     memo = [float('-inf') for i in range(capacity + 1)]
#     memo[0] = 0
#     for i in range(1, len(w) + 1):
#         for j in range(capacity, w[i - 1] - 1, -1):
#             memo[j] = max(memo[j], memo[j - w[i - 1]] + v[i - 1])
#     return memo[capacity]

v = [12, 3, 10, 3, 6]
w = [5, 4, 7, 2, 6]
capacity = 15
print(Knapsack(w, v, capacity))