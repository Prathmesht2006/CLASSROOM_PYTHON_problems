# Frequency of elements in list of lists

lst = [[1, 2, 3, 2],
       [4, 5, 6, 2],
       [7, 8, 9, 5]]

freq = {}

for sublist in lst:
    for item in sublist:

        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

print(freq)