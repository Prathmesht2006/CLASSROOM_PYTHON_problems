
import numpy as np
import pandas as pd

# arr = np.array([[1, 2, 3],[9,7,8]])
# print(arr)

# friends1={
#     "name":["prathmesh","rahul","pg","raj"],
#     "marks":[89,88,57,68]
# }

# df1=pd.DataFrame(friends1)
# print(df1)
# df1.to_csv("friends1.csv",index=False)

# print(df.head(2))#print starting 2 rows
# print(df.tail(2))#print ending 2 rows

# print(df.describe())#descibe numeric colomns like count,min,max-----

friends2={
    "name":["prathmesh","rahul","pg","raj"],
    "marks":[89,88,57,68],
    "city":["murgud","chandagad","gadhinglaj","kolhapur"]
}
df2=pd.DataFrame(friends2)
df2.to_csv("friends2.csv",index=False)
f=pd.read_csv("friends2.csv")
# print(f)

# print(f["name"])#print name colomn

f.index=["frist","second","third","fourh"]#update index names
# print(f)

print()
