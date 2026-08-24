# 3. WAP to generate and print a dictionary that contains a number (between 1 and n) in the 
# form {1:12, 2:22,…..n}.i.e {1:1,2:4,3:9,…..} 

n = 5
d = {}

for i in range(1, n+1):
    d[i] = i*i

print(d)
