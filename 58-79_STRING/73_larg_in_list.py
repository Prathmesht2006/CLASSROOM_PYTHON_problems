list=["mumbai","delhi","kolkata"]

def large_small(l):
    large=l[0]
    small=l[0]
    for i in l:
        if len(i)<len(small):
            small=i
        if len(i)>len(large):
            large=i
    return large,small

a,b=large_small(list)
print(a,b)