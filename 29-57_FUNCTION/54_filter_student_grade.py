students = [
 {"name": "ABC", "age": 18, "grade": 97},
 {"name": "PQR", "age": 16, "grade": 92},
 {"name": "XYZ", "age": 17, "grade": 90},
 {"name": "TEST", "age": 16, "grade": 94},
]

result = list(filter(lambda s: s["grade"] >= 95, students))

print(result)
