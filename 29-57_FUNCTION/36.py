# Occurrence using arbitrary arguments

def occurrence(search, *nums):

    count = 0

    for i in nums:
        if i == search:
            count += 1

    print("Occurrence =", count)


occurrence(20, 10, 20, 30, 20, 40, 20, 50, 60, 20, 70)