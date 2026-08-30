with open("demo.txt", "r") as f:
    data = f.read().split()

for item in data:
    if item.isdigit():
        print(item)
