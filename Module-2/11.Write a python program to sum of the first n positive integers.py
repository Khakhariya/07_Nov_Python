number = int (input ("enter the number : "))
a = 0

if number > 0 :
    for i in range (number+1):
        if i <= number :
            sum = a + i
            a = sum
print (f"sum of positive number is : {sum}")