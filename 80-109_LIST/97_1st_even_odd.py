list1 = [1, 3, 5, 7, 4, 1, 6, 8]

for i in list1:
    if i % 2 == 0:
        print("First Even: ",i)
        break
    
for i in list1:
    if i % 2 != 0:
        print("First odd: ",i)
        break
