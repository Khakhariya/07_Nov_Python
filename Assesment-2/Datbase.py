import pymysql

def getdata (list):

    # Database connected :-
    try:
        db_connection = pymysql.connect(host='localhost',user='root',password='',database='hotel_management')
        print ('database connected')
    except Exception as e :
        print (e)

    # Create Table in Database :- 
    cur = db_connection.cursor()
    create_table = 'Create table customer_info (id integer primary key auto_increment, name text,address text,number Integer,day integer,room text,payment text,Room_number integer)'

    try:
        cur.execute(create_table)
        print('Table Created !')
    except Exception as e :
        print (e)

    # show data of table :-
    
    if list[4] == 'Deluxe':
        # Deluxe room :-
        list1 = [1,2,3,4,5,6,7,8,9]
        list2 = []
        list3 = []

        showdata = 'select * from customer_info'

        try:
            cur.execute(showdata)
            data = cur.fetchall()

            for i in data:
                list2.append(i[7])
            
        except Exception as e :
            print (e)

        for i in list1 :
                if i not in list2 :
                    list3.append(i)
        print (list3)
        Room_Number = list3[0]

    elif list[4] == "General" :
         # General room :-
        list1 = [11,12,13,14,15,16,17,18,19]
        list2 = []
        list3 = []

        showdata = 'select * from customer_info'

        try:
            cur.execute(showdata)
            data = cur.fetchall()

            for i in data:
                list2.append(i[7])
            
        except Exception as e :
            print (e)

        for i in list1 :
                if i not in list2 :
                    list3.append(i)

        Room_Number = list3[0]

    elif list[4] == "Full_Deluxe" :
         # General room :-
        list1 = [21,22,23,24,25,26,27,28,29,30]
        list2 = []
        list3 = []

        showdata = 'select * from customer_info'

        try:
            cur.execute(showdata)
            data = cur.fetchall()

            for i in data:
                list2.append(i[7])
            
        except Exception as e :
            print (e)

        for i in list1 :
                if i not in list2 :
                    list3.append(i)
        Room_Number = list3[0]
    
    elif list[4] == "Joint" :
         # General room :-
        list1 = [31,32,33,34,35]
        list2 = []
        list3 = []

        showdata = 'select * from customer_info'

        try:
            cur.execute(showdata)
            data = cur.fetchall()

            for i in data:
                list2.append(i[7])
            
        except Exception as e :
            print (e)

        for i in list1 :
                if i not in list2 :
                    list3.append(i)
        Room_Number = list3[0]

    # Insert data in table :-

    insert_data = f"insert into customer_info (name,address,number,day,room,payment,Room_number) values ('{list[0]}','{list[1]}',{list[2]},{list[3]},'{list[4]}','{list[5]}','{Room_Number}')"

    try:
        cur.execute(insert_data)
        db_connection.commit()
        print('Data submitted successfully')
    except Exception as e :
        print (e)

def show_data ():

    # Database connected :-
    try:
        db_connection = pymysql.connect(host='localhost',user='root',password='',database='hotel_management',)
        print ('database connected')
    except Exception as e :
        print (e)


    # Create Table in Database :- 
    # cur = db_connection.cursor()
    cur = db_connection.cursor()
    create_table = 'Create table customer_info (id integer primary key auto_increment, name text,address text,number Integer,day integer,room text,payment text,Room_number integer)'

    try:
        cur.execute(create_table)
        print('Table Created !')
    except Exception as e :
        print (e)

    # get all data from database :-

    showdata = 'select * from customer_info'

    try:
        cur.execute(showdata)
        data = cur.fetchall()

    except Exception as e :
        print (e)

    return data

def Check_out (number):

    # Database connected :-
    try:
        db_connection = pymysql.connect(host='localhost',user='root',password='',database='hotel_management',)
        print ('database connected')
    except Exception as e :
        print (e)


    # Create Table in Database :- 
    cur = db_connection.cursor()
    create_table = 'Create table customer_info (id integer primary key auto_increment, name text,address text,number Integer,day integer,room text,payment text,Room_number integer)'

    try:
        cur.execute(create_table)
        print('Table Created !')
    except Exception as e :
        print (e)
    
    # delete checkout customer ;-

    checkout = f"delete from customer_info where Room_number = '{number}'"

    try :
        cur.execute(checkout)
        db_connection.commit()
        print('Checkout Done')
    except Exception as e :
        print (e)
    
def Get_information (number):

    # Database connected :-
    try:
        db_connection = pymysql.connect(host='localhost',user='root',password='',database='hotel_management',)
        print ('database connected')
    except Exception as e :
        print (e)


    # Create Table in Database :- 
    cur = db_connection.cursor()
    create_table = 'Create table customer_info (id integer primary key auto_increment, name text,address text,number Integer,day integer,room text,payment text,Room_number integer)'

    try:
        cur.execute(create_table)
        print('Table Created !')
    except Exception as e :
        print (e)
    
    # Get information of customer :-

    Info_customer = f'select * from customer_info where Room_number = "{number}"'

    try:
        cur.execute(Info_customer)
        data = cur.fetchall()

    except Exception as e :
        print (e)
    
    
    return data