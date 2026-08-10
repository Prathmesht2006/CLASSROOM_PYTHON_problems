from array import array
arr=array("i",[1,2,3,4,5,6,7,8,9,10])
largest=arr[0]
second_l=arr[0]
# count_even=0
# for i in arr:
#     if i%2==0:
#         count_even+=1

# print(count_even)

for i in range(0,9):
    if arr[i]>largest:
        second_l=largest
        largest=arr[i]


print(second_l)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               