# Fibonacci series using function


def fabonacci(num):
    a=0
    b=1
    for i in range(1,num+1):
        print(a,end=" ")
        a,b=b,a+b

fabonacci(10)
