# 7. WAP to find the longest common prefix of all strings in given set
s = {"flower", "flow", "flight"}

prefix = ""
shortest = min(s, key=len)

for i in range(len(shortest)):
    if all(word[i] == shortest[i] for word in s):
        prefix += shortest[i]
    else:
        break

print("Longest common prefix:", prefix)
