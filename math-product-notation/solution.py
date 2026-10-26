def product(f, lo, hi):
    prod = 1
    for i in range(lo, hi+1):
        prod*=f(i)
    return prod
