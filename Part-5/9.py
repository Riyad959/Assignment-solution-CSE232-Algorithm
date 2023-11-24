def knapsake(items, values, weights, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    max_value = dp[n][capacity]
    return max_value

items = ['A', 'B', 'C']
values = [6, 10, 12]
weights = [2, 4, 6]
knapsake_capacity = 8
result = knapsake(items, values, weights, knapsake_capacity)
print(f"Maximum Value: {result}")