def isArraySorted(array):
    if len(array) == 1:
        return True
    else:
        return array[0] <= array[1] and isSorted(array[1:])


def isSorted(array):
    if array == sorted(array):
        return True
    else:
        return False


A = [9, 6, 3, 1]
B = [1, 2, 3, 4]
print(isArraySorted(A))
print(isArraySorted(B))
