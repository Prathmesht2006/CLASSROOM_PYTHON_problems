names = ["Amit", "Suresh", "Om", "Isha", "Raj", "Uday"]

vowels = ('A', 'E', 'I', 'O', 'U')

result = list(filter(lambda x: x.startswith(vowels), names))

print(result)
