list=["hello","hello","hello"]
string=input("enter a string to search:  ")
flag=0

for i in list:
    if i==string:
        flag=1
        continue
    else:
        print(f"all values in list are not equal to: {string}")
        break

if flag==1:
    print(f"all values in list are equal to: {string}")