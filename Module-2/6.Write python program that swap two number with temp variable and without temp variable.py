number1 = int (input ("enter the number1 :- " ))
number2 = int (input ("enter the number2 :- " ))

print ("number1 = {} \t number2 = {}".format(number1,number2))

if number1 > number2 :
    number1 -= number2
    number2 += number1
    number1 = number2 - number1
else:
    number2 -= number1
    number1 += number2
    number2 = number1 - number2

print ("number1 = {} \t number2 = {}".format(number1,number2))