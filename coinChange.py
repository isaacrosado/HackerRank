import sys

def makeCombinations(coins, n, includedCoins, memo):
    if n == 0:
        return 1
    if n < 0 or includedCoins <= 0:
        return 0
    if (n, includedCoins) in memo:
        return memo[(n, includedCoins)]
    combinationAmount = makeCombinations(coins, n, includedCoins - 1, memo) + \
                        makeCombinations(coins, n - coins[includedCoins - 1], includedCoins, memo)
    memo[(n, includedCoins)] = combinationAmount
    return combinationAmount


def make_change(coins, n):
    includedCoins = len(coins)
    memo = {}
    return makeCombinations(coins, n, includedCoins, memo)


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))