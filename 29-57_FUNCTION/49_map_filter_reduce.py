from functools import reduce

nums = []
for i in range(5):
    nums.append(int(input("Enter number: ")))

squares = list(map(lambda x: x * x, nums))
odd_squares = list(filter(lambda x: x % 2 != 0, squares))
sum_odd_square = reduce(lambda a, b: a + b, odd_squares)

print("Squares:", squares)
print("Odd Squares:", odd_squares)
print("Sum of odd squares:", sum_odd_square)


# print(type(sum_odd_square))
