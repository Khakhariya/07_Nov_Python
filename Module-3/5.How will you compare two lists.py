list1 = []
n = int (input ("Enter the number to run loop : "))
for i in range (n) :
     num = int (input ("Enter the number : "))
     list1.append(num)
print (list1)

list2 = []
n = int (input ("Enter the number to run loop : "))
for i in range (n) :
     num = int (input ("Enter the number : "))
     list1.append(num)
print (list1)

list1.sort()
list2.sort()

if list1 == list2 :
    print ("These are equal list.")
else :
    print ("These are not equal list.")