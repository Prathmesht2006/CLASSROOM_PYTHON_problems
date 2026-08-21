l="hello hello word hello word python"
l=l.split(" ")

temp=[]

for i in l:
    count=0
    for j in l:
        if j==i:
            count+=1
    
    if i in temp:
        continue
    else:
        print(i,"=",count)
        temp.append(i)




# -----------------------------------

# s="mumbai"
# temp=""

# for i in s:
#     if i in temp:
#         continue
#     else:
#         print(i,":",s.count(i))
#         temp=temp+i




# ----------------
# l=["hello","hello","word","hello","word","python"]
# for i in l:
#     temp=""
#     print(i,"=",end=" ")
#     for j in i:
#         if j in temp:
#             continue
#         else:
#             print(f"({j}:{i.count(j)})",end="  ")
#             temp=temp+j
#     print()
