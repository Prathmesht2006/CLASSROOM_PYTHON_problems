# Find pairs having difference of 3

lst = [0, 3, 4, 7, 9]

result = []

for i in lst:
    for j in lst:
        if j - i == 3:
            result.append([i, j])

print(result)