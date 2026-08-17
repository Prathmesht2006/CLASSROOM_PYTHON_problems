places = [' ', 'Pune', 'Kolhapur', ' ', 'Satara', ' ']

result=list(filter(lambda x: True if " " is in x ,places))
print(result)


# places = [' ', 'Pune', 'Kolhapur', ' ', 'Satara', ' ']

# result = list(filter(lambda x: x.strip() != "", places))

# print(result)
