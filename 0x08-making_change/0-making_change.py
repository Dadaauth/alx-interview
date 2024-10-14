#!/usr/bin/python3
"""ALXSWE Change project using Dynamic programming
"""


def makeChange(coins, total):
    """, determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    st_coins = sorted(coins, reverse=True)
    remainder = total
    count = 0
    idx = 0
    n = len(coins)

    while remainder > 0:
        if idx >= n:
            return -1
        if remainder - st_coins[idx] >= 0:
            remainder -= st_coins[idx]
            count += 1
        else:
            idx += 1
    return count
