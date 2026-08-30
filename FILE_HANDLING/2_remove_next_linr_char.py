
with open("file.txt", "r") as f:
    text = f.read()

text = text.replace("\n", " ")

with open("output.txt", "w") as f:
    f.write(text)
