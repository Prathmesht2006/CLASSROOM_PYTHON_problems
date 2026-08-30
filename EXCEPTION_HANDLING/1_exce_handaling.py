# 1. ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 2. FileNotFoundError
try:
    open("abc.txt")
except FileNotFoundError:
    print("File not found!")

# 3. ValueError
try:
    int("abc")
except ValueError:
    print("Invalid value!")

# 4. TypeError
try:
    print(5 + "hi")
except TypeError:
    print("Type error!")

# 5. IndexError
try:
    l = [1, 2, 3]
    print(l[10])
except IndexError:
    print("Index out of range!")












try:
    # 1. ZeroDivisionError
    print(10 / 0)

    # 2. FileNotFoundError
    open("abc.txt")

    # 3. ValueError
    int("abc")

    # 4. TypeError
    print(5 + "hi")

    # 5. IndexError
    l = [1, 2, 3]
    print(l[10])

except ZeroDivisionError:
    print("Cannot divide by zero!")

except FileNotFoundError:
    print("File not found!")

except ValueError:
    print("Invalid value!")

except TypeError:
    print("Type error!")

except IndexError:
    print("Index out of range!")