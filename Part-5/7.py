def min_coins(coins, value):
    dp = [float('inf')] * (value + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, value + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[value]

coin = [1, 2, 5]
value = 11
result = min_coins(coin, value)
print(f"minimum{result}coin")