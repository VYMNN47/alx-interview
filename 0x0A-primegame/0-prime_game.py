#!/usr/bin/python3
"""Module for Prime Game."""


def isWinner(x, nums):
    """Determines the winner of the Prime Game."""

    def sieve_of_eratosthenes(n):
        """Generate a list indicating prime numbers up to n."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    def prime_count_up_to(n, primes):
        """Returns a list of prime counts up to each index <= n."""
        prime_counts = [0] * (n + 1)
        count = 0
        for i in range(n + 1):
            if primes[i]:
                count += 1
            prime_counts[i] = count
        return prime_counts

    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_counts = prime_count_up_to(max_num, primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        prime_count = prime_counts[n]
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
