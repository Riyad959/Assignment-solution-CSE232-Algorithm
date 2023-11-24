def min_coin(coins, amount):
    MAX_VALUE = 10**9
    bag = [MAX_VALUE] * (amount + 1)
    bag[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            bag[i] = min(bag[i], bag[i - coin] + 1)

    return bag[amount] if bag[amount] != MAX_VALUE else -1

denominations = [1, 5, 10]
target_amount = 12
result = min_coin(denominations, target_amount)
print(f"ninimum num {result}")