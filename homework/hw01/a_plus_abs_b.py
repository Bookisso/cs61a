from operator import add, sub


def a_plus_abs(a, b) :
    if b < 0 :
        f = sub
    else :
        f = add
    return f(a, b)