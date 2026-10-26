def factorial(n):
    fac = 1
    for i in range(2, n+1):
        fac*=i
    return fac


def n_choose_k(n, k):
    return factorial(n)//((factorial(k)*(factorial(n-k))))
