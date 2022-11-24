number = int (input ("enter the number :- "))

default_1 = 0
default_2 = 1

print ("fibonacci sequence : ")
print (default_1,end=", ")
print (default_2,end=", ")

for i in range (number+1):
    sum =  default_1 + default_2
    default_1 = default_1
    default_2 = sum
    if sum <= number:
        print (sum,end=", ")