with open("demo.txt","w") as f:
    f.write("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")

with open("demo.txt","r") as f:  
    odd=[]
    data=f.read()
    list=data.split(" ")
    for i in list:
        if int(i)%2!=0:
            odd.append(i)
                

print(odd)

