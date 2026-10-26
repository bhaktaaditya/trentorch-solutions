def count_comparisons_linear_search(arr, target):
    c = 0
    found = False
    for i in arr:
        c+=1
        if i==target:
            found = True
            break
        else:
            continue
    # TODO: Implement a left-to-right linear scan, counting comparisons.
    return found, c


def count_comparisons_binary_search(arr, t):
    c = 0
    while len(arr) > 0:
        c+=1
        mid = len(arr) // 2
        if arr[mid] == t:
            return True, c
        elif arr[mid] > t:
            arr = arr[:mid]
        else:
            arr = arr[mid + 1:]

    return False, c
