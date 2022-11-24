str = input("enter the string :- ")

if len(str) < 2 :
    print ("empty string")
else :
    x = str[:2]
    y = str[-2:]

print (f"string is : {x+y}")