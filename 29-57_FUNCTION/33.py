# Power series using function

def series(n):

    for i in range(n):
        print(2 ** i, end=" ")

n = int(input("Enter number of terms: "))
series(n)