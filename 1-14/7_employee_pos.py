# Program to display employee position

exp = float(input("Enter years of experience: "))

if exp==0:
    print("Position: Fresher")

elif exp==1:
    print("Position: Senior")

elif exp>=2:
    print("Position: Team Lead")

else:
    print("Invalid experience")