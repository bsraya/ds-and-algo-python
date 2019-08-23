def recursive_print(n):
    if n == 0:
        return 0
    else:
        print(n)
        return recursive_print(n - 1)


recursive_print(6)
