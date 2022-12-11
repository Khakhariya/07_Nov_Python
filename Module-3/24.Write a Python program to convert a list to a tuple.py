list1 = []

n = int(input ("How many city you want to enter : "))

for i in range (n):
    city = input ("Enter the city name : ")
    list1.append (city)

print (f"Original list : {list1}")
print (f"list to tuple : {tuple(list1)}")