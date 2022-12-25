def Customer_app ():
   print ('''
   Welcome to Customer's App
                    Operation Menu
                    1) Withdraw Amount
                    2) Deposite Amount
                    3) View Balance
   ''') 


def Withdraw_amount ():

   File1 = open ('banker.txt','r')

   name = input ("Enter Your name :- ")
   a = 0
   for i in File1 :
      a += 1
      if name in i :
         j = a - 1
   
   File1.close()  

   File = open ('Balance.txt','r')
   
   x = File.readlines()

   File .close()
   
   W_AM = True
   while W_AM == True :
        try :
            withdrawl_amount = float(input ("Enter the Withdrawl Amount :- "))
        except :
            print ("\n------------Please Enter Floating number or integer number only -----------")    
        else :
            W_AM = False
   
   y = float(x[j])

   if withdrawl_amount < y :
      y = y - withdrawl_amount
      print (y)
   else :
      print ("You are not able to withdraw money exceed your Bank balance :- ")
   
   x[j] = str(y)

   File = open ('Balance.txt','w')

   for i in x:
      File.write(i)
      if x[j] == i :
         File.write("\n")
   File.close()


def Deposit_amount ():
   File1 = open ('banker.txt','r')

   name = input ("Enter Your name :- ")
   a = 0
   for i in File1 :
      a += 1
      if name in i :
         j = a - 1
   
   File1.close()  

   File = open ('Balance.txt','r')
   
   x = File.readlines()

   File .close()
   
   D_AM = True
   while D_AM == True :
        try :
            Deposit_amount = float(input ("Enter the Deposit Amount :- "))
        except :
            print ("\n------------Please Enter Floating number or integer number only -----------")    
        else :
            D_AM = False
   
   y = float(x[j])

   if Deposit_amount < y :
      y = y + Deposit_amount
      print (y)
   else :
      print ("You are not able to withdraw money exceed your Bank balance :- ")
   
   x[j] = str(y)

   File = open ('Balance.txt','w')

   for i in x:
      File.write(i)
      if x[j] == i :
         File.write("\n")
   File.close()

def View_Balance ():
   file= open ('banker.txt','r')

   name = input ("Enter Your Name :- ")
   V_Bal = True
   while V_Bal == True :
        try :
            Ac_number = int(input("Enter Your Ac_no :- "))
        except :
            print ("\n------------Please Enter Only Integer-----------")    
        else :
                V_Bal = False
                Ac_no = str(Ac_number)

   a = 0
   for i in file :
      a += 1
      if name in i :
         j = a - 1
   file.close()
   
   file1 = open ("Balance.txt",'r')

   print (f"Mr./Ms. {name} Your Balance is :{file1.readlines()[j]}")

   file1.close()