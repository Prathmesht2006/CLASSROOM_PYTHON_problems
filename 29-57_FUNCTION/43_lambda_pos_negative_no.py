check = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")

num = int(input("Enter number: "))
print(check(num))
