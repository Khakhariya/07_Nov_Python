A = True
while (A == True) :
    try : 
        number = int (input("Enter the number only : "))
        A = False
    except :
        print ('------------Please Enter only number----------')
    finally :
        print ("This is finally block which is run every time.")