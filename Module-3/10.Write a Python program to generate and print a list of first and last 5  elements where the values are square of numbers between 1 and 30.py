list = []

sn = int (input ("Enter the starting number of list : "))
en = int (input ("Enter the ending number of list : "))

for i in range (sn,en+1):
    power = i ** 2
    list.append(power)

print (f"First Five Numbers of square is : {list[:5]} \n Last five Numbers of squaer is : {list [-5:]}")