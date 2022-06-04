def luhn_sum(n) :
    """Returns the Luhn sum for the positive number N.
    >>> luhn_sum(2)
    2
    >>> luhn_sum(32)
    8
    >>> luhn_sum(5105105105105100)
    20
    """
    if n < 10 :
        return n
    else :
        last = n % 10
        all_but_last = n // 10
        return last + luhn_sum_double(all_but_last)

def luhn_sum_double(n) :
    last = n % 10
    all_but_last = n // 10
    return sum_digits(last * 2) + luhn_sum(all_but_last)


def sum_digits(n):
    """Return the sum of the digits of positive integer n.
>>> sum_digits(6)
6
>>> sum_digits(2021)
5
"""
    if n >= 10 :
        last = n % 10
        extra = n // 10
        return sum_digits(extra) + last
    return n