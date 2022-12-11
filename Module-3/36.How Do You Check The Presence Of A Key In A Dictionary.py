#we can check the presence of a key in a dictionary using 

#if statement and membership operator
    
dic = {"TV" : 21 , "A.C." : 12 , "Watch" : 15 , "Mobile No." : 13}
print (f"Original dictionary :- {dic}")
def check_key (x) :
    if x in dic :
        print (f"{x} is present in dic .")    
    else : 
        print (f"{x} is not present in dic .")

for i in range (3) :
    key = input("Enter to check that items in dictionary or not :- ")
    check_key (key)