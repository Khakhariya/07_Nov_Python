number1 = float (input ("Enter the first number is :"))
number2 = float (input ("Enter the second number is :"))

ans = True

if number1 < number2 :
   number1,number2 =number2,number1
sum = number1 + number2
dif = number1 - number2

if number1 == number2 or sum == 5 or dif == 5:
   print (ans) 