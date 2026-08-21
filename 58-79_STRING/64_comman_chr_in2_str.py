str1="abcdefgh"
str2="acdegh"

result=""

for i in str1:
    if i not in str2:
        continue
    else:
        result+=i

print(result)