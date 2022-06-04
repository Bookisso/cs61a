def sum_digits(n):
    """Return the sum of the digits of positive integer n.
>>> sum_digits(6)
6
>>> sum_digits(2021)
5
"""
    if n > 10 :
        last = n % 10
        extra = n // 10
        return sum_digits(extra) + last
    return n