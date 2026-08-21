text=input("enter a text: ")
text=text.lower()
count=0
for i in text:
    if i in "aeiou":
        count+=1

print(f"no of vowels in {text}:{count}")