dic = {"TV" : 21 , "A.C." : 12 , "Watch" : 15 , "Mobile No." : 13}

print (f"Original dictionary : {dic}")
 
def check_key (n) :
    if n in dic :
        print ("It is already exists in a dictionary.")
    else :
        print ("It is not exists in a dictionary.")

n = input ("Enter the electronics items name :- ")

check_key (n)