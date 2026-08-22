# Largest odd number in list

lst = [0, 9, 2, 4, 5, 6]

odd_numbers = []

for i in lst:
    if i % 2 != 0:
        odd_numbers.append(i)

print("Largest Odd Number =", max(odd_numbers))