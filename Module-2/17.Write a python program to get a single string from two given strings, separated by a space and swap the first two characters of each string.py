str1 = "jay"
str2 = "khakhariya"

print ("string1 : ",str1)
print ("string2 : ",str2)

x = str1[:2]
y = str2[:2]

print ("final string is :",str1.replace(x,y),end="")
print (str2.replace(y,x))