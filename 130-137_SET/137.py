# 8. Perform all the methods set.

A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)
print("Difference B-A:", B - A)
print("Symmetric Difference:", A ^ B)

A.add(6)
print("After add:", A)

A.remove(2)
print("After remove:", A)

A.discard(10)   # no error
print("After discard:", A)

A.pop()
print("After pop:", A)

A.clear()
print("After clear:", A)
