def factorial (number) :
    res = 1
    for i in range (number):
        res = res * (i+1)
    print (f"Factorial of {number} is : {res}")
num = int (input ("Enter the number to find factorial of numbers : "))
factorial (num)