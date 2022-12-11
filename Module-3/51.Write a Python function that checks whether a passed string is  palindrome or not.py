def palindrome (string ):
    print (f"Original string is : {string}")
    length = len (string)
    str2 = ""

    for i in range (length,0,-1) :
        str2 = str2 + string[i-1]

    if string == str2 :
        print ("It is a palindrome string which is entered.")
    else :
        print ("It is not a palindrome string which is entered.")

str1 = input ("Enter the string to check string is palindrome or not :- ")
palindrome (str1)