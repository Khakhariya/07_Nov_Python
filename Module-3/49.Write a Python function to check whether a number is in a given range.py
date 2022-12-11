def check_number (number):
    if number >= 0 and number <= 100 :
        print ("It is in a given range of numbers")
    else : 
        print ("It is not in a given range of numbers")

try :
    num = int (input ("Enter the number to check number is in range or not :- "))
except :
    print ("Error!")

check_number (num)