# 4. WAP to find the two numbers whose product is maximum among all the pairs in a given set
# of numbers?

s = {1, 10, 2, 6, 5}

lst = list(s)
max_product = 0
pair = ()

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] * lst[j] > max_product:
            max_product = lst[i] * lst[j]
            pair = (lst[i], lst[j])

print("Pair:", pair)
print("Maximum Product:", max_product)
