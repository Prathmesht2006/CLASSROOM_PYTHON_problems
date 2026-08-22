list1 = [0, 3, 4, 7, 9]
start = min(list1)
end = max(list1)
total = 0

for i in range(start, end + 1):
    if i not in list1:
        total += i

print("Sum of missing numbers:", total)
