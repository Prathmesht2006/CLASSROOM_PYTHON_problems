# cities = [("Pune", 24), ("Mumbai", 30), ("Nagpur", 22), ("Delhi", 28)]

# result = list(filter(lambda x: x[1] < 25, cities))

# for city in result:
#     print(city[0])

cities = {
  "Pune": 24,
  "Mumbai": 30,
  "Nagpur": 22, 
  "Delhi": 28,
  }

result = list(filter(lambda x: cities[x] < 25, cities))


print(result)

