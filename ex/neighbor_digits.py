
def neighbor_digits(num, pre_digit=-1) :
        if num < 10 :
            return num == pre_digit
        rest = num // 10
        last = num % 10
        return int(pre_digit == last or rest % 10 == last) + neighbor_digits(rest, last) 