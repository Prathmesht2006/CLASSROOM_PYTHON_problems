# Search element in array

arr = [10, 20, 30, 40, 50]

num = int(input("Enter number to search: "))

i = 0
flag = 0

while i < len(arr):
    if arr[i] == num:
        flag = 1
        break
    i += 1

if flag == 1:
    print("Number Found")
else:
    print("Number Not Found")