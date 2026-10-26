def summation(f, lo, hi):
    s = 0
    for i in range(lo, hi+1):
        s+=f(i)
    return s
