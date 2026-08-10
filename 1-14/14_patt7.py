

# Q14
# Pattern:
# *
# * * *
# * * * * *
# * * * * * * *

rows = 4

for i in range(1, rows + 1):
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
