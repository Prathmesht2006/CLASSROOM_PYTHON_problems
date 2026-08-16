n=10
for i in range(n+1):
    for j in range(65,65+n-i):
        print(chr(j),end=" ")
    print()