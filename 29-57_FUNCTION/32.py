# Prime number using function
def check_prime(num):
    if num<=1:
        return False
    
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True




num=int(input("Enter a num:"))

if check_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")


































