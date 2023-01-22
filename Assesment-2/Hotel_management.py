from tkinter import *
from tkinter import ttk

# Welcome window :-
from Module import *
welcome_window = Tk()

welcome_window.title('Hotel Management')
welcome_window.geometry('1200x700')

# Welcome page frame1 :- 
frame_1 = Frame(welcome_window,borderwidth='2',background='White',width=995,highlightcolor='black',highlightbackground='black',relief=GROOVE)
frame_1.place(relx=0.02,rely=0.02,relheight=0.96,relwidth=0.96)

# Welcome message :-
M1 = Message(frame_1,text='WELCOME',font="Cooper 50",background='WHITE',width=791)
M1.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)

# welcome page Button :-
B1 = Button(frame_1,text='1. CHECK INN',font='Arial-Black 15',command=check_inn)
B1.place(relx=0.08, rely=0.20, height=95, width=566)

B2 = Button(frame_1,text='2. SHOW GUEST LIST',font='Arial-Black 15',command=show_guest_list)
B2.place(relx=0.08, rely=0.35, height=95, width=566)

B3 = Button(frame_1,text='3. CHECK OUT',font='Arial-Black 15',command=check_out)
B3.place(relx=0.08, rely=0.50, height=95, width=566)

B4 = Button(frame_1,text='4. GET INFO OF ANY GUEST',font='Arial-Black 15',command=get_info)
B4.place(relx=0.08, rely=0.65, height=95, width=566)

B5 = Button(frame_1,text='5. EXIT',font='Arial-Black 15',command='exit')
B5.place(relx=0.08, rely=.80, height=95, width=566)

# Welcome page message extra :- 
L1 = Label(frame_1,text='HOTEL MANAGEMENT',font="Cooper 30 bold",background='white')
L1.place(relx=0.58, rely=0.20, relheight=0.15, relwidth=0.40)

L2 = Label(frame_1,text='PYTHON TKINTER',font="Cooper 33 bold",background='white')
L2.place(relx=0.58, rely=0.40, relheight=0.15, relwidth=0.40)

L3 = Label(frame_1,text='GUI',font="Cooper 80 bold",background='white')
L3.place(relx=0.58, rely=0.60, relheight=0.15, relwidth=0.40)

welcome_window.mainloop() 