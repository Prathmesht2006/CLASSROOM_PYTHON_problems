data = input("Enter some text: ")

with open("file.txt", "w") as f:
    f.write(data)
