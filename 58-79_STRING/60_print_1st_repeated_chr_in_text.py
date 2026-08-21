text=input("Enter text: ")
temp=""

for i in text:
    if i in temp:
        print(f"1st repeated character is:{i}")
        break
    else:
        temp=temp+i

print(temp)