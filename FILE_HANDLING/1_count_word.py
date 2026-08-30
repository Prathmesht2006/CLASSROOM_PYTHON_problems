
# def count_word(word):
        
#     count=0
#     with open("demo.txt","r") as f:
#         data=f.read()
#         list=data.split(" ")
#         print(list) 
#         for i in list:
#             if i==word:
#                 count+=1

#         print(count)

# count_word("hello")


with open("file.txt", "r") as f:
    text = f.read().lower()
    words = text.split()

    word_count={}
    for w in words:
        word_count[w]=word_count.get(w,0)+1

print(word_count)


















# word_count = {}

# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# print(word_count)
