with open("demo.txt", "r") as f:
    text = f.read()

newline_count = text.count("\n")
tab_count = text.count("\t")

print("Newlines:", newline_count)
print("Tabs:", tab_count)
