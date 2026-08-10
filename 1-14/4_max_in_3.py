a=int(input("enter 1st no: "))
b=int(input("enter 2nd no: "))
c=int(input("enter 3rd no: "))

if a>b and a>c:
    print("max: ",a)
elif b>c:
    print("max: ",b)
else:
    print("max: ",c)


# def max(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c


# print("max: ",max(a,b,c))