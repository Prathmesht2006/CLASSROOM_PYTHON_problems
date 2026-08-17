# Fibonacci Series using while loop

n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 1

while count <= n:
    print(a, end=" ")

    a,b =b,a+b
    
    count += 1