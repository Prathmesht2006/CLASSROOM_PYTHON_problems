# Longest word in list

lst = ["Apple", "Computer", "Python", "Programming"]

longest = [word for word in lst if len(word) == max(len(w) for w in lst)]

print(longest)