List = []

Number = int(input("Enter the number :- "))

for i in range (Number) :
    number = int (input ("Enter the number to make a list :- "))
    List.append (number)

print (f"Original list : {List}")
List.sort ()
print(List[1])