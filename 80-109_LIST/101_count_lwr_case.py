# Count lowercase letters

words = ["Red", "Green", "Blue", "White"]

count = 0

for word in words:
    for ch in word:
        if ch.islower():
            count += 1

print("Count is", count)