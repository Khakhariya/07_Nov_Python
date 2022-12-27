import os 
#os.chdir ('task')
import sqlite3

print ('''
    Database :-
    1) Create Database 
    2) Create Table
    3) insert into table
    4) update into table
    5) delete in table data
    6) Show record in Table 
    ''')
index = int (input ("Enter number to perform various condition of database :-"))

if index == 1 :

    # Create Database :-
    Database_name = input("Enter Database name : ")

    try :
        ab = sqlite3.connect(f'{Database_name}.db')
        print ("Database create or connected successfully.")    
    except Exception as a :
        print (a)

if index == 2 :

    # Create Database :-
    Database_name = input("Enter Database name : ")

    try :
        ab = sqlite3.connect(f'{Database_name}.db')
        print ("Database create or connected successfully.")    
    except Exception as a :
        print (a)

    # Create Table :-
    Table_name = input("Enter table name : ")
    Table_create = f"create table {Table_name} (id integer primary key autoincrement , name text ,Address vartext(21))"
    try :
        ab.execute(Table_create)
        print ("Table Created Successfully")
    except Exception as a :
        print (a)

if index == 3:

    # Create Database :-
    Database_name = input("Enter Database name : ")

    try :
        ab = sqlite3.connect(f'{Database_name}.db')
        print ("Database create or connected successfully.")    
    except Exception as a :
        print (a)
    
    Table_name = input("Enter table name : ")
    
    # Insert into Table :- 
    con = False 
    while con == False:
        try :
            n = int(input ("Enter number of data insert into table :"))
        except Exception as a:
            print (a)
        else :
            con = True
    
    
    for i in range (n):
        name = input ("Enter the name : ")
        Address = input ("Enter the Address :")
        Data_insert = f"insert into {Table_name}(name,Address)values('{name}','{Address}')"

        try:
            ab.execute(Data_insert)   
            ab.commit()
            print ("Record inserted Succesfully.")
        except Exception as a:
            print (a)

if index == 4 :

   # Create Database :-
    Database_name = input("Enter Database name : ")

    try :
        ab = sqlite3.connect(f'{Database_name}.db')
        print ("Database create or connected successfully.")    
    except Exception as a :
        print (a) 

    # Update into table :- 
    Table_name = input("Enter table name : ")
    
    q = input ("What to change in table :- ")
    q1 = input ("Enter value want to change :- ")
    A = input ("Where to change :- ")
    A1 = input ("Enter the data want to change : - ")
    
    upadate_data = f"update {Table_name} set {q} = '{q1}' where {A} = '{A1}'"

    try:
        ab.execute(upadate_data)   
        ab.commit()
        print ("Record updated Succesfully.")
    except Exception as a:
        print (a)

if index == 5 :

   # Open Database :-
    Database_name = input("Enter Database name : ")

    try :
        ab = sqlite3.connect(f'{Database_name}.db')
        print ("Database create or connected successfully.")    
    except Exception as a :
        print (a) 
 
    Table_name = input("Enter table name : ")

    # Delete Record into table :-
    print ('''
        Press 
        1) To delete all items from table 
        2) To delete specific items from table 
        ''')
    Want = int (input("Enter number to delete :- "))
    
    if Want == 1 :
        delete_record = f"delete from {Table_name}"
        try:
            ab.execute(delete_record)   
            ab.commit()
            print ("Record deleted Succesfully.")
        except Exception as a:
            print (a)

    if Want == 2 :
        index_table = input ("Enter what to remove  :- ")
        Data = input ("Enter data which want to remove from table :- ")
        delete_record = f"delete from {Table_name} where {index_table} = '{Data}'"
        
        try:
            ab.execute(delete_record)   
            ab.commit()
            print ("Record deleted Succesfully.")
        except Exception as a:
            print (a)

if index == 6 :

    # Open Database :-
    Database_name = input("Enter Database name : ")

    try :
        ab = sqlite3.connect(f'{Database_name}.db')
        print ("Database create or connected successfully.")    
    except Exception as a :
        print (a)

    Table_name = input("Enter table name : ")

    show_data = f"select * from {Table_name}"
    
    cur = ab.cursor()
    try:
        cur.execute(show_data)   
        data = cur.fetchall()
        for i in data :
            print (i)
    except Exception as a:
        print (a)