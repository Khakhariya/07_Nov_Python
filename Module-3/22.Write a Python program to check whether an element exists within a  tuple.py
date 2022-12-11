tup = ('Rajkot','Gondal','Morbi','Ahmedabad')

x = False
City = input ("Enter the city name : ")

for i in tup :
    if City == i :
        x = True

if x == True :
    print ("It is in tuple.")
elif x == False :
    print ("It is not in tuple.")