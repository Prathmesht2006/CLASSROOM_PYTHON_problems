# n=int(input("enter no: "))

# a=0
# b=1
# while a<=n:
#     print(a,end=" ")
#     a,b=b,a+b


# Q12
# Pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4

rows = 4

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()