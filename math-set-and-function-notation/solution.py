def is_subset(a, b):
    c = 0
    for i in a:
        if i in b:
            c+=1
    return bool(c==len(a))


def argmax(values):
    m = -1*float("inf")
    index = 0
    for i in range(len(values)):
        if m>values[i]:
            continue
        elif m<values[i]:
            m=values[i]
            index = i
    return index
