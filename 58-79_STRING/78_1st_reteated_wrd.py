l="hello hello word hello word python"
l=l.split(" ")

temp=[]

for i in l:
        if i in temp:
            print(i)
            break
        else:
            temp.append(i)

