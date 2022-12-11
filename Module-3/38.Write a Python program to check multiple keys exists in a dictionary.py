'''dic = {"TV" : 21 , "A.C." : 12 , "Watch" : 15 , "Mobile No." : 13}
x = False
if ('TV' and 'A.C.') in dic :
    x = True
print (x)'''

from my_lib import user_list 

dic = {"TV" : 21 , "A.C." : 12 , "Watch" : 15 , "Mobile No." : 13}
print (dic)

try :
    list = user_list ()
except :
    print ("Please enter valid integer value.")

x = False
temp = 0
print (list)

for i in range (len(list)):
    if list[i] in dic :
        temp = temp + 1

if len(list) == temp :
    x = True
print (x)