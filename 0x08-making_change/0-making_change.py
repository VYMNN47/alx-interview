#!/usr/bin/python3
"""Module for make_change"""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet a given total"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    used_coins = []

    for coin in coins:
        while total >= coin:
            used_coins.append(coin)
            total -= coin

    if total != 0:
        return -1

    return len(used_coins)
