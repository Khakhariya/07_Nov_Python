import tkinter 
from tkinter import *
from tkinter import ttk
import Datbase


def check_inn ():

    check = Toplevel ()

    check.geometry('1200x600')

    list1 = []
    # All frame :- 

    frame_1 = Frame(check,borderwidth='2',background='White',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    frame_1.place(relx=0.02,rely=0.02,relheight=0.10,relwidth=0.96)

    frame_2 = Frame(check,borderwidth='2',background='White',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    frame_2.place(relx=0.02,rely=0.13,relheight=0.60,relwidth=0.96)

    frame_3 = Frame(check,borderwidth='2',background='White',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    frame_3.place(relx=0.02,rely=0.74,relheight=0.25,relwidth=0.96)


    # Message of frame_1:-

    M1 = Message(frame_1,text='YOU CLICKED ON       :        CHECK  IN',font="Cooper 20 bold",background='WHITE',width=791)
    M1.place(relx=0.01, rely=0.20, relheight=0.50, relwidth=0.86)

    # frame_2 :-
    # Label of Information :-

    L1 = Label(frame_2,text='ENTER YOUR NAME',font="Cooper 15 bold",background='white')
    L1.place(relx=0.03, rely=0.06, height=40,width=300)

    L2 = Label(frame_2,text='ENTER YOUR ADDRESS',font="Cooper 15 bold",background='white')
    L2.place(relx=0.03, rely=0.16, height=40,width=335)

    L3 = Label(frame_2,text='ENTER YOUR NUMBER',font="Cooper 15 bold",background='white')
    L3.place(relx=0.03, rely=0.26, height=40,width=325)

    L4 = Label(frame_2,text='NUMBER OF DAYS',font="Cooper 15 bold",background='white')
    L4.place(relx=0.03, rely=0.36, height=40,width=285)

    # Label (:)  :- 

    L5 = Label(frame_2,text=':',font="Cooper 15 bold",background='white')
    L5.place(relx=0.45, rely=0.06)
    L6 = Label(frame_2,text=':',font="Cooper 15 bold",background='white')
    L6.place(relx=0.45, rely=0.16)
    L7 = Label(frame_2,text=':',font="Cooper 15 bold",background='white')
    L7.place(relx=0.45, rely=0.26)
    L8 = Label(frame_2,text=':',font="Cooper 15 bold",background='white')
    L8.place(relx=0.45, rely=0.36)

    # Entry information space :-

    name = Entry(frame_2,font='Arial 12 bold',background='white',relief=GROOVE,border=2)
    name.place(relx=0.5,rely=0.06,height=30,width=440)

    address = Entry(frame_2,font='Arial 12 bold',background='white',relief=GROOVE,border=2)
    address.place(relx=0.5,rely=0.16,height=30,width=440)

    number = Entry(frame_2,font='Arial 12 bold',background='white',relief=GROOVE,border=2)
    number.place(relx=0.5,rely=0.26,height=30,width=440)

    Days = Entry(frame_2,font='Arial 12 bold',background='white',relief=GROOVE,border=2)
    Days.place(relx=0.5,rely=0.36,height=30,width=440)


    # frame_3 ok funciton :-
    def Name ():
        x = name.get()
        if len(x) != 0 :
            Label(frame_3,text='Name has been inputed.',background='white').place(relx=0.01,rely=0.01)
        else :
            Label(frame_3,text='Invalid name.',background='white').place(relx=0.01,rely=0.01)

    def Address ():
        x = address.get()
        if len(x) != 0 :
            Label(frame_3,text='Address has been inputed.                   ',background='white').place(relx=0.01,rely=0.15)
        else :
            Label(frame_3,text='Invalid Address, Please enter valid address.',background='white').place(relx=0.01,rely=0.15)
    def Number ():
        x = number.get()
        if len(x) != 0 :
            Label(frame_3,text='Mobile number has been inputed.                  ',background='white').place(relx=0.01,rely=0.30)
        else :
            Label(frame_3,text='Invalid Number, Please enter valid number.',background='white').place(relx=0.01,rely=0.30)
    def Day ():
        x = Days.get()
        if len(x) != 0 :
            Label(frame_3,text='Day has been Inputed.',background='white').place(relx=0.01,rely=0.45)
        else :
            Label(frame_3,text='Please Enter day.',background='white').place(relx=0.01,rely=0.45)


    # Ok button :-
    bname = Button(frame_2,font='Arial 12 bold',text='ok',command=Name,background='white',relief=GROOVE,border=2)
    bname.place(relx=0.9,rely=0.06,height=30,width=40)

    baddress = Button(frame_2,font='Arial 12 bold',text='ok',command=Address,background='white',relief=GROOVE,border=2)
    baddress.place(relx=0.9,rely=0.16,height=30,width=40)

    bnumber = Button(frame_2,font='Arial 12 bold',text='ok',command=Number,background='white',relief=GROOVE,border=2)
    bnumber.place(relx=0.9,rely=0.26,height=30,width=40)

    bdays = Button(frame_2,font='Arial 12 bold',text='ok',command=Day,background='white',relief=GROOVE,border=2)
    bdays.place(relx=0.9,rely=0.36,height=30,width=40)


    # Choose Your room :-
    L9 = Label(frame_2,text='CHOOSE YOUR ROOM',font="Cooper 15 bold",background='white')
    L9.place(relx=0.35, rely=0.45,)


    # checkButtom in choose your room :-

    Deluxe = IntVar()
    General = IntVar()
    Full_deluxe= IntVar()
    Joint = IntVar()

    deluxe = Checkbutton (frame_2,font='cooper 15 bold',text='DELUXE',variable=Deluxe,background='white')
    deluxe.place(relx=0.20, rely=0.55)

    general = Checkbutton (frame_2,font='cooper 15 bold',text='GENERAL',variable=General,background='white')
    general.place(relx=0.55, rely=0.55)

    full_deluxe = Checkbutton (frame_2,font='cooper 15 bold',text='FULL DELUXE',variable=Full_deluxe,background='white')
    full_deluxe.place(relx=0.20, rely=0.65)

    joint = Checkbutton (frame_2,font='cooper 15 bold',text='JOINT',variable=Joint,background='white')
    joint.place(relx=0.55, rely=0.65)

    # Choose Your Payment method :-

    L10 = Label(frame_2,text='CHOOSE PAYMENT METHOD',font="Cooper 15 bold",background='white')
    L10.place(relx=0.30, rely=0.80,)    
    
    # CheckButtom in choose Payment method :-

    Cash = IntVar()
    Credit_debit_card = IntVar()

    cash = Checkbutton (frame_2,font='cooper 15 bold',text='CASH',variable=Cash,background='white')
    cash.place(relx=0.20, rely=0.90)

    card = Checkbutton (frame_2,font='cooper 15 bold',text='BY CREDIT / DEBIT CARD',variable=Credit_debit_card,background='white')
    card.place(relx=0.55, rely=0.90)
   
    # Send data function :- 
    def senddata () :

        # Payment condition :-

        if Cash.get() :
            payment = 'cash'
        
        elif Credit_debit_card.get() :
            payment = 'Credit/Debit Card'

        # Rooms condition :- 
        if Deluxe.get() :
            Rooms = 'Deluxe'
        elif General.get():
            Rooms = 'General'
        elif Full_deluxe.get() :
            Rooms = 'Full_Deluxe'
        elif Joint.get() :
            Rooms = 'Joint'

        # Make list :- 

        list1.append(name.get())
        list1.append(address.get())
        list1.append(number.get())
        list1.append(Days.get())
        list1.append(Rooms)
        list1.append(payment)
        
        Datbase.getdata(list1)

    # Submit button using ttk

    sumbit = Button(frame_2,text="SUBMIT",command=senddata,font='Arial 25')
    sumbit.place(relx=0.80,rely=0.65,height=75,width=150)
    
    check.mainloop()

def show_guest_list ():

    show = Toplevel ()

    show.geometry('800x500')

    # Frame all :-

    frame_1 = Frame(show,borderwidth='2',background='White',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    frame_1.place(relx=0.02,rely=0.02,relheight=0.96,relwidth=0.96)

    # frame_1 in 2 more frame :-
    frame_2 = Frame(frame_1,borderwidth='2',background='grey',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    frame_2.place(relx=0.02,rely=0.08,relheight=0.85,relwidth=0.45)

    frame_3 = Frame(frame_1,borderwidth='2',background='grey',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    frame_3.place(relx=0.5,rely=0.08,relheight=0.85,relwidth=0.45)

    fframe_2 = Frame(frame_2,borderwidth='2',background='White',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    fframe_2.place(relx=0.05,rely=0.15,relheight=0.80,relwidth=0.90)

    fframe_3 = Frame(frame_3,borderwidth='2',background='White',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    fframe_3.place(relx=0.05,rely=0.15,relheight=0.80,relwidth=0.90)


    # Labels :-
    # Label  of frame_1 :-

    L1 = Label(show,text='LIST OF ALL GUEST',font='Arial 15 bold',background='grey',fg='white',relief=GROOVE)
    L1.place(relx=0.03,rely=0.01)

    # Label  of frame_2 :-

    L2 = Label(frame_2,text='NAMES',font='Arial 15 bold',background='grey',fg='white')
    L2.place(relx=0.4,rely=0.03)

    # Label  of frame_3 :-

    L3 = Label(frame_3,text='ROOM NO.',font='Arial 15 bold',background='grey',fg='white')
    L3.place(relx=0.3,rely=0.03)

    # show data in window :- 

    data = Datbase.show_data()
    add = 0.01
    for i in data :
        Label(fframe_2,text=f'{i[1]}',font='Arial 15 bold',background='white').place(relx=0.01,rely=add)
        Label(fframe_3,text=f'{i[7]}',font='Arial 15 bold',background='white').place(relx=0.01,rely=add)
    
        add = add + 0.10

    show.mainloop()

def check_out ():
    out = Tk ()

    out.geometry('700x500')

    # frame all :-

    frame_1 = Frame(out,borderwidth='2',background='White',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    frame_1.place(relx=0.03,rely=0.03,relheight=0.94,relwidth=0.94)

    frame_2 = Frame(frame_1,borderwidth='2',background='White',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    frame_2.place(relx=0.05,rely=0.50,relheight=0.45,relwidth=0.90)

    # Label :- 

    L1 = Label(frame_1,text="ENTER THE ROOM NO. : ",font='cooper 15 bold',background='white')
    L1.place(relx=0.2, rely=0.15)

    # Entry Room Number :-

    Room_number = Entry(frame_1,font="cooper 12 bold",border=2)
    Room_number.place(relx=0.6,rely=0.15,height=40,width=40)

    
    # button of checkout :-

    def checkout ():
        x = Room_number.get()
        number = Room_number.get()
        data = Datbase.Check_out(number)
        print (data)
        if len(x) != 0 :
            Label(frame_2,text=f'Thanks  for visit our hotel.',background='white').place(relx=0.01,rely=0.01)
        else :
            Label(frame_2,text='Invalid Room numbers .',background='white').place(relx=0.01,rely=0.01)
        
    
    bcheckout = Button(frame_1,text='CHECK OUT',font='Arial 15 bold italic',command=checkout)
    bcheckout.place(relx=0.3,rely=0.30,height=50,width=150)

    out.mainloop()

def get_info ():
    out = Tk ()

    out.geometry('700x500')

    # frame all :-

    frame_1 = Frame(out,borderwidth='2',background='grey',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    frame_1.place(relx=0.03,rely=0.03,relheight=0.94,relwidth=0.94)

    frame_2 = Frame(frame_1,borderwidth='2',background='White',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
    frame_2.place(relx=0.05,rely=0.50,relheight=0.45,relwidth=0.90)

    # Label : 

    L1 = Label(frame_1,text="GET INFO HERE ..!! ",font='cooper 20 bold',background='grey')
    L1.place(relx=0.3, rely=0.05)

    L2 = Label(frame_1,text="ENTER THE ROOM NO.    : ",font='cooper 15 bold',background='grey')
    L2.place(relx=0.15, rely=0.15)

    # Entry Room Number :-

    Room_number = Entry(frame_1,font="cooper 12 bold",border=2)
    Room_number.place(relx=0.6,rely=0.15,height=30,width=60)

    # button of checkout :-

    def submit ():
        
        x = Room_number.get()
        number =Room_number.get()
        data = Datbase.Get_information(number)
        add = 0.01
        if len(x) != 0 :
            for i in data :
                Label(frame_2,text=f'Name :- "{i[1]}"',background='white').place(relx=0.01,rely=add) 
                add = add + 0.10      
                Label(frame_2,text=f'Room Number :-"{i[7]}"',background='white').place(relx=0.01,rely=add)
                

        else :
            Label(frame_2,text='Invalid Room numbers .',background='white').place(relx=0.01,rely=0.01)  
        
    bcheckout = Button(frame_1,text='SUBMIT',font='Arial 15 bold ',command=submit,background='grey')
    bcheckout.place(relx=0.3,rely=0.30,height=50,width=150)

    out.mainloop()