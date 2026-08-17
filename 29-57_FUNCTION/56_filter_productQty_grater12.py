products = [
 ("Tables", 13),
 ("Chairs", 9),
 ("Bottles", 23),
 ("Pens", 3),
 ("Bags", 15),
]

result = list(filter(lambda p: p[1] > 12, products))

print(result)


# products = {
#  "Tables": 13,
#  "Chairs": 9,
#  "Bottles": 23,
#  "Pens": 3,
#  "Bags": 15
# }

# result = list(filter(lambda p: products[p] > 12, products))

# print(result)
