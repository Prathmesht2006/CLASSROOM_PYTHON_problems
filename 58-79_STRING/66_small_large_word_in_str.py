s="prathmesh dilip tambekar"
s=s.split()

smallest=s[0]
largest=s[0]

for i in s :
    if len(i)<len(smallest):
        smallest=i

    if len(i)>len(largest):
        largest=i


print(smallest)
print(largest)
print(s)