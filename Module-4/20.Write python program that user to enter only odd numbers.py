try :
    list1 = []
    con = int()
    n = int (input("Enter number to start loop :- "))
    for i in range (n):
        Number = int (input ("Enter the number to make list :- "))
        if Number % 2 != 0 :
            list1.append(Number)
    if len(list1) == n :
        print("These are odd numbers")
        print (list1)
    else :
        Number = Odd
except :
    print ("\nError! :- Please enter odd number only.")

finally :
    print ("\n-------This is Tops Technology-------\n")