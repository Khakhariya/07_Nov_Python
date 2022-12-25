import re

s = False

# Enter password Using regular expression :-
while s == False :
    password = input("Enter the password :- ")
    Length = len (password)
    if Length >= 8 :
        if re.findall('[a-z]',password) and re.findall('^[A-Z]',password) and re.findall('[0-9]',password) and re.findall ('\W',password):
            A = True
            s = True
        else :
            print('''please Enter Strong password :- 
            How to enter Password :- 
            Minimum 8 characters.
            The alphabet must be between [a-z]
            At least one alphabet should be of Upper Case [A-Z] 
            At least 1 number or digit between [0-9].
            At least 1 character from [ _ or @ or $ ].''')
    else :
        print ("Please Enter minimun 8 character of password.")

# Reenter password to confirm password :- 
while A == True:
    Confirm_password = input ("Enter password to confirm :- ")
    if password == Confirm_password :
        print ("Your password is confirmed and saved")
        A = False
    else :
        print ("Enter Same password.")