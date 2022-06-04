def cascade(n) :
    if n >= 10 :
        cascade(n//10)
        print(n)
    else :
        print(n)
    print(n)
