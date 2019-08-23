# source:
# https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/


def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from %s to %s" % (from_rod, to_rod))
        return
    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk %d from %s to %s" % (n, from_rod, to_rod))
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


print(towerOfHanoi(3, "A", "C", "B"))

