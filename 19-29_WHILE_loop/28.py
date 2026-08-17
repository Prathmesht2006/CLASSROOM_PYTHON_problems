# Count occurrence of element in array

arr = [10, 20, 30, 20, 40, 20]

num = int(input("Enter number: "))

i = 0
count = 0

while i < len(arr):
    if arr[i] == num:
        count += 1
    i += 1

print("Number present", count, "times")