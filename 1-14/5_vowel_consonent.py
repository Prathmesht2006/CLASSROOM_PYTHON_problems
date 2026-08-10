ch=input("enter a character: ")
ch=ch.lower()

if ch.isalpha():
    if ch in "aeiou":
            print("VOWEL")
    else:
        print("COSNONENT")
            
else:
    print("invalid character")
    


# for i in range(97,123):
#     if chr(i) in "aeiou":
#         print(f"{chr(i)} is vowel")
#     else:
#         print(f"{chr(i)} is consonent")
