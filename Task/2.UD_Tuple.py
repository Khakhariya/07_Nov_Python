Loop = int (input ("Enter the number to insert element of Tuple :- "))
L = []

for i in range (Loop) :
    List = input ("Enter the Tuple element :- ")
    L.append(List)

T = tuple(L)

print ("Tuple is : ",T)