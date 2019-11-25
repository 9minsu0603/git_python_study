def binary_search_sub(a, x, start, end):

    if start > end:
        return -1

    mid = (start + end) // 2

    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_sub(a, x, mid + 1, end)
    else:
        return binary_search_sub(a, x, start, mid - 1)
    return -1


def binary_search(a, x):
    return binary_search_sub(a, x, 0, len(a) - 1)


d = [5, 8, 15, 45, 58, 72, 85, 90, 99]

print(binary_search(d, 15))

print(binary_search(d, 50))