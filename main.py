from timeit import timeit
from random import randint


def find_coins_greedy(amount, available_coins):
    result = {}
    for coin in sorted(available_coins, reverse=True):
        while amount >= coin:
            result[coin] = result.get(coin, 0) + 1
            amount -= coin
    return result


def find_min_coins(amount, available_coins):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in available_coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float("inf"):
        return {}

    result_coins = {}
    i = amount
    while i > 0:
        for coin in available_coins:
            if i - coin >= 0 and dp[i] == dp[i - coin] + 1:
                result_coins[coin] = result_coins.get(coin, 0) + 1
                i -= coin
                break

    return result_coins


def print_timing(algorithm_name, sample_size, execution_time):
    print(f"{algorithm_name} ({sample_size} samples): {execution_time:.6f} seconds")


if __name__ == "__main__":
    # base test
    coins = [50, 25, 10, 5, 2, 1]
    amount = 113
    print(find_coins_greedy(amount, coins))
    print(find_min_coins(amount, coins))
    # performance test
    for amount in [
        randint(100000, 1000000),
        randint(1000000, 10000000),
        randint(10000000, 100000000),
    ]:
        print_timing(
            "Greedy",
            amount,
            timeit(
                "print(find_coins_greedy(amount, coins))", globals=globals(), number=1
            ),
        )
        print_timing(
            "Dynamic",
            amount,
            timeit("print(find_min_coins(amount, coins))", globals=globals(), number=1),
        )