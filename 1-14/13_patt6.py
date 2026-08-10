 
# Q13
# Pattern:
# A
# B B
# C C C
# D D D D

rows = 4
ch = 65   # ASCII value of A

for i in range(1, rows + 1):
    for j in range(i):
        print(chr(ch), end=" ")
    ch += 1
    print()