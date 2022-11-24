n1 = int (input ("enter the 1st number : "))
n2 = int (input ("enter the 2nd number : "))
n3 = int (input ("enter the 3rd number : "))

if n1 == n2 or n2 == n3 or n1 == n3:
    sum = 0
else :
    sum = n1 + n2 + n3

print ("sum of three number is : ",sum)