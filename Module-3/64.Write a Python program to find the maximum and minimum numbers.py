def min_max_decimal (dec_number):

    print (f"All decimal numbers are : {dec_number}")
    print (f"Minimum numbers in decimal number list is : {min(dec_number)}")
    print (f"Maximum numbers in decimal number list is : {max(dec_number)}")


Decimal_number = input("Enter the decimal number : ").split(" ")
    
min_max_decimal(Decimal_number)