
def rev_str_mul4(s):
    if len(s)%4==0:
        return s[::-1]
    else:
        return s


print(rev_str_mul4(input("enter string:")))