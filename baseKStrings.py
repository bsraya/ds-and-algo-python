def range_to_list(k):
    result = []
    for i in range(0, k):
        result.append(str(i))
    return result


# print(range_to_list(5))
def baseKStrings(n, k):
    if n == 0:
        return []
    if n == 1:
        return range_to_list(k)
    return [
        digit + bitstring
        for digit in baseKStrings(1, k)
        for bitstring in baseKStrings(n - 1, k)
    ]


print(baseKStrings(4, 3))

