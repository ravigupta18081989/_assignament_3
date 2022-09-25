str="1234abcd"

def reverse(str):
    revstr=' '
    for i in str:
        revstr = i + revstr
    return revstr

print("original str: ",str)
print("reverse str: ",reverse(str))