def change_coin(coins, amount):
    way = [0] * (amount + 1)
    way[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            way[i] += way[i - coin]

    return way[amount]

scan = input("enter coin").split()
coins = [int(x) for x in scan]
amount = int(input("amount"))
result = change_coin(coins, amount)
print(f"number of way is{result}")