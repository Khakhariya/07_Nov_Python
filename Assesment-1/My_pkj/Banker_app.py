import datetime as dt

def Banker_app ():
    print ('''
    
Welcome to Banker's App 
                        Operations Menu
                        1) Add Customer
                        2) View Customer
                        3) Search Customer
                        4) View All Customer
                        5) Total Amounts in Bank         
    ''')
# 1) Add customer in bank app :-
def Add_customer () :
    
    file = open('banker.txt','a')
    # Account number :- 
    A_NO = True
    while A_NO == True :
        try :
            Acc_no = int (input("Enter account no : "))
        except :
            print ("\n------------Please Enter Only Integer-----------")    
        else :
            A_NO = False
    
    # Customer Name :- 
    cus_nm = input ("Enter the customer name : ")
    
    # Open Balance :- 
    OP_Bal = True
    while OP_Bal == True :
        try :
            open_balance = float (input ("Enter opening balance : "))
        except :
            print ("\n------------Please Enter Floating number or integer number only -----------")    
        else :
            OP_Bal = False
    
    current_date = dt.datetime.now()
    x = current_date
    y = str (x)
    B = ['Acc_no','customer name ' , 'Open Balance ','Opening Date']
    C = [Acc_no ,cus_nm , open_balance,y]
    
    dict1 = dict(zip(B,C))
    file.write(f"{dict1}\n")
    
    file1 = open('Balance.txt','a')
    file1.write(f"{open_balance}")
    file1.write("\n")
    file1.close()

    file.close()

# 2) View Customer in bank app :-
def View_customer () :

    file = open('banker.txt','r')

    # Account number :- 
    C_NO = True
    while C_NO == True :
        try :
            customer_no = input("Enter the customer number :- ")
        except :
            print ("\n------------Please Enter Only Integer-----------")    
        else :
            C_NO = False
    # Customer name :- 
    customer_name = input ("Enter customer name :- ")
    
    x = file.readlines()

    for i in x :
        if customer_no in i and customer_name in i:
            print (i)

    file.close()

# 3) Search Customer in bank app :-
def Search_customer ():

    file = open ('banker.txt','r')

    # Customer name :- 
    customer_name = input ("Enter customre name :- ")
    
    for i in file :
        if customer_name in i :
            print (f"{customer_name} is our bank cutomer\nand his/her information is :{i}")
   
    file.close()

# 4) View All Customer in bank app :-
def View_All_Customer ():

    file = open('banker.txt','r')

    for i in file :
        print (i)
    
    file.close()

# 5) Check All balance in bank :-
def All_balance ():

    file = open('Balance.txt','r')
    Total_Balance = float()
    for i in file :
        x = i
        y = float(x)
        Total_Balance = Total_Balance + y
    print ("Total Bank Balance in Bank is : ",Total_Balance)
    file.close()