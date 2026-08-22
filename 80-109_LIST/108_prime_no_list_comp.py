# Prime numbers using list comprehension

start = 1
end = 20

prime = [num for num in range(start, end + 1)
         if num > 1 and all(num % i != 0 for i in range(2, num))]

print(prime)