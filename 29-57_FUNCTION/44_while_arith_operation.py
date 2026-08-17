while True:
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    if choice == 1:
        print("Result =", a + b)
    elif choice == 2:
        print("Result =", a - b)
    elif choice == 3:
        print("Result =", a * b)
    elif choice == 4:
        print("Result =", a / b)
    else:
        print("Invalid choice")
