a=int(input("enter first no: "))
b=int(input("enter second no: "))
c=int(input("enter third no: "))

if a<=0 or b<=0 or c<=0:
    print("enter valid nos")
else:
    print("average: ",(a+b+c)/3)
    