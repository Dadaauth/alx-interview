#!/usr/bin/python3
"""ALXSWE Prime game Project
"""


def isWinner(x, nums):
    """determines who the winner of the gane Prime Game.
    """
    if x < 1 or not nums:
        return None
    mariaWins, benWins = 0, 0
    n = max(nums)

    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for f, is_prime in enumerate(primes, 1):
        if f == 1 or not is_prime:
            continue
        for m in range(f + f, n + 1, f):
            primes[m - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        benWins += primes_count % 2 == 0
        mariaWins += primes_count % 2 == 1
    if mariaWins == benWins:
        return None
    return 'Maria' if mariaWins > benWins else 'Ben'
