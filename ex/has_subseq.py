def has_subseq(n, seq) :
    if seq > n :
        return False
    if seq == n :
        return True
    if seq < n and n % 10 == seq % 10:
        return has_subseq(n//10, seq//10)
    return has_subseq(n//10, seq)
