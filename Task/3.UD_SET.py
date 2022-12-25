Loop = int (input ("Enter the number to insert element of SET :- "))
L = []

for i in range (Loop) :
    List = input ("Enter the SET element :- ")
    L.append(List)

x = set(L)
print ("SET is :- ",x)