def prime_factors(n):
    """Print the prime factors of n in non-decreasing order

        >>> prime_factors(8)
        2
        2
        2
        >>> prime_factors(9)
        3
        3
        >>> prime_factors(11)
        11
        >>> prime_factors(12)
        2
        2
        3
        >>> prime_factors(858)
        2
        3
        11
        13
        """

    while n>1:
        smallest_prime = 2
        while n % smallest_prime != 0:
            smallest_prime = smallest_prime + 1
        n = n//smallest_prime
        print(smallest_prime)