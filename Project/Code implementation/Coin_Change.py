def min_coin_change(coins, amount):

    min_coins = [amount + 1] * (amount + 1)
    min_coins[0] = 0


    for coin in coins:
        for i in range(coin, amount + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[amount] if min_coins[amount] <= amount else -1

# Example usage
coins = [1, 5, 6, 8]
amount = 11
result = min_coin_change(coins, amount)
print(result)


