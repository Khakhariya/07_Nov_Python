str = input ("enter the string name :")

length = len (str)

if length % 4 == 0 :
    length -= 1
    for i in range (length,-1,-1):
        print(str [i],end="")
else :
    print (str)