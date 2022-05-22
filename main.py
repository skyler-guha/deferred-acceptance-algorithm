import random
from tkinter import *
from tkinter import ttk
import time

window = Tk()
window.title("Deferred Acceptanc Algorithm")
window.resizable(width=False, height=False)

#=================Group 1=======================================
group1_label = Label(window,text="Group_1",pady = 10,padx = 10)
group1_label.grid(row = 0,column = 0)

label_A = Label(window,text="A")
label_A.grid(row = 1 ,column = 0)

label_B = Label(window,text="B")
label_B.grid(row = 2 ,column = 0)

label_C = Label(window,text="C")
label_C.grid(row = 3 ,column = 0)

label_1_1 = Label(window,text="1")
label_1_1.grid(row = 0 ,column = 1)

label_2_1 = Label(window,text="2")
label_2_1.grid(row = 0 ,column = 2)

label_3_1 = Label(window,text="3")
label_3_1.grid(row = 0 ,column = 3)


A1 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
A1.grid(row = 1,column = 1)

A2 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
A2.grid(row = 1,column = 2)

A3 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
A3.grid(row = 1,column = 3)

B1 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
B1.grid(row = 2,column = 1)

B2 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
B2.grid(row = 2,column = 2)

B3 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
B3.grid(row = 2,column = 3)

C1 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
C1.grid(row = 3,column = 1)

C2 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
C2.grid(row = 3,column = 2)

C3 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
C3.grid(row = 3,column = 3)


R1_1 = Label(window,borderwidth=1,width =8,height=2,padx = 15,text = "")
R1_1.grid(row = 1 ,column = 4)

R2_1 = Label(window,borderwidth=1,width =8,height=2,padx = 15,text = "")
R2_1.grid(row = 2 ,column = 4)

R3_1 = Label(window,borderwidth=1,width =8,height=2,padx = 15,text = "")
R3_1.grid(row = 3 ,column = 4)


#=================Group 2=======================================
group2_label = Label(window,text="Group_2",pady = 10,padx = 10)
group2_label.grid(row = 4,column = 0)

label_X = Label(window,text="X")
label_X.grid(row = 5 ,column = 0)

label_Y = Label(window,text="Y")
label_Y.grid(row = 6 ,column = 0)

label_Z = Label(window,text="Z")
label_Z.grid(row = 7 ,column = 0)

label_1_2 = Label(window,text="1")
label_1_2.grid(row = 4 ,column = 1)

label_2_2 = Label(window,text="2")
label_2_2.grid(row = 4 ,column = 2)

label_3_2 = Label(window,text="3")
label_3_2.grid(row = 4 ,column = 3)



X1 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
X1.grid(row = 5,column = 1)

X2 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
X2.grid(row = 5,column = 2)

X3 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
X3.grid(row = 5,column = 3)

Y1 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
Y1.grid(row = 6,column = 1)

Y2 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
Y2.grid(row = 6,column = 2)

Y3 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
Y3.grid(row = 6,column = 3)

Z1 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
Z1.grid(row = 7,column = 1)

Z2 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
Z2.grid(row = 7,column = 2)

Z3 = Entry(window, borderwidth=1, relief="solid",width =2,font=('Time New Roman', 20,"bold"),justify='center')
Z3.grid(row = 7,column = 3)


R1_2 = Label(window,borderwidth=1,width =8,height=2,padx = 15,text = "")
R1_2.grid(row = 5 ,column = 4)

R2_2 = Label(window,borderwidth=1,width =8,height=2,padx = 15,text = "")
R2_2.grid(row = 6 ,column = 4)

R3_2 = Label(window,borderwidth=1,width =8,height=2,padx = 15,text = "")
R3_2.grid(row = 7 ,column = 4)


#======================function wiggets===========================

Ran = Button(window,text="Insert random values for all",command = lambda:group_random ())
Ran.grid(row = 1 ,column = 5)

cls = Button(window,text="Clear all values for all",command = lambda:group_clear ())
cls.grid(row = 2 ,column = 5)

Ran_b_1 = Button(window,text="Insert random values for Group 1",command = lambda:group_1_random ())
Ran_b_1.grid(row = 1 ,column = 6)

Ran_b_2 = Button(window,text="Insert random values for Group 2",command = lambda:group_2_random ())
Ran_b_2.grid(row = 2 ,column = 6)

cls_b_1 = Button(window,text="Clear all values for Group 1",command = lambda:group_1_clear ())
cls_b_1.grid(row = 3 ,column = 6)

cls_b_2 = Button(window,text="Clear all values for Group 2",command = lambda:group_2_clear ())
cls_b_2.grid(row = 4 ,column = 6)

options = IntVar()

option_label = Label(window,text="Choose which group should propose to the other:      ")
option_label.grid(row = 5 ,column = 5)

r1 = Radiobutton(window,text="Group 1 → Group 2",variable = options ,value = 1)
r1.grid(row = 6 ,column = 5)

r2 = Radiobutton(window,text="Group 2 → Group 1",variable = options ,value = 2)
r2.grid(row = 7 ,column = 5)

Run_Button_auto = Button(window,text ="Run program",pady = 10,command = lambda:Run_sequence())
Run_Button_auto.grid(row = 8 ,column = 5)

auto_tick = Entry(window)
auto_tick.grid(row = 8 ,column = 6)
auto_tick.insert(0,"0.4")

tick_label = Label(window,text="^seconds per opperation^" ,padx = 40)
tick_label.grid(row = 9 ,column = 6)

#==============Functions===================
def timer():
    window.update()
    time.sleep(float(auto_tick.get()))
    window.update()


def bg_group1(color,row,column):

    if (row == 1):
        if (column == 3):
            A1.configure(bg=color)
        if (column == 2):
            A2.configure(bg=color)
        if (column == 1):
            A3.configure(bg=color)

    if (row == 2):
        if (column == 3):
            B1.configure(bg=color)
        if (column == 2):
            B2.configure(bg=color)
        if (column == 1):
            B3.configure(bg=color)

    if (row == 3):
        if (column == 3):
            C1.configure(bg=color)
        if (column == 2):
            C2.configure(bg=color)
        if (column == 1):
            C3.configure(bg=color)

def bg_group2(color,row,column):

    if (row == 1):
        if (column == 3):
            X1.configure(bg=color)
        if (column == 2):
            X2.configure(bg=color)
        if (column == 1):
            X3.configure(bg=color)

    if (row == 2):
        if (column == 3):
            Y1.configure(bg=color)
        if (column == 2):
            Y2.configure(bg=color)
        if (column == 1):
            Y3.configure(bg=color)

    if (row == 3):
        if (column == 3):
            Z1.configure(bg=color)
        if (column == 2):
            Z2.configure(bg=color)
        if (column == 1):
            Z3.configure(bg=color)


def group_1_random ():

    bg_group1("white",1,1)
    bg_group1("white",1,2)
    bg_group1("white",1,3)
    bg_group1("white",2,1)
    bg_group1("white",2,2)
    bg_group1("white",2,3)
    bg_group1("white",3,1)
    bg_group1("white",3,2)
    bg_group1("white",3,3)

    A1.delete(0,END)
    A2.delete(0,END)
    A3.delete(0,END)
    B1.delete(0,END)
    B2.delete(0,END)
    B3.delete(0,END)
    C1.delete(0,END)
    C2.delete(0,END)
    C3.delete(0,END)

    x = [1,2,3]
    y = [1,2,3]
    z = [1,2,3]

    A1_val = random.choice(x)
    x.remove(A1_val)

    A2_val = random.choice(x)
    x.remove(A2_val)

    A3_val = x[0]

    B1_val = random.choice(y)
    y.remove(B1_val)

    B2_val = random.choice(y)
    y.remove(B2_val)

    B3_val = y[0]

    C1_val = random.choice(z)
    z.remove(C1_val)

    C2_val = random.choice(z)
    z.remove(C2_val)

    C3_val = z[0]


    A1.insert(0,"X" if (A1_val == 1) else "Y" if (A1_val == 2) else "Z")
    A2.insert(0,"X" if (A2_val == 1) else "Y" if (A2_val == 2) else "Z")
    A3.insert(0,"X" if (A3_val == 1) else "Y" if (A3_val == 2) else "Z")
    B1.insert(0,"X" if (B1_val == 1) else "Y" if (B1_val == 2) else "Z")
    B2.insert(0,"X" if (B2_val == 1) else "Y" if (B2_val == 2) else "Z")
    B3.insert(0,"X" if (B3_val == 1) else "Y" if (B3_val == 2) else "Z")
    C1.insert(0,"X" if (C1_val == 1) else "Y" if (C1_val == 2) else "Z")
    C2.insert(0,"X" if (C2_val == 1) else "Y" if (C2_val == 2) else "Z")
    C3.insert(0,"X" if (C3_val == 1) else "Y" if (C3_val == 2) else "Z")


def group_2_random ():
    bg_group2("white",1,1)
    bg_group2("white",1,2)
    bg_group2("white",1,3)
    bg_group2("white",2,1)
    bg_group2("white",2,2)
    bg_group2("white",2,3)
    bg_group2("white",3,1)
    bg_group2("white",3,2)
    bg_group2("white",3,3)

    X1.delete(0,END)
    X2.delete(0,END)
    X3.delete(0,END)
    Y1.delete(0,END)
    Y2.delete(0,END)
    Y3.delete(0,END)
    Z1.delete(0,END)
    Z2.delete(0,END)
    Z3.delete(0,END)

    x = [1,2,3]
    y = [1,2,3]
    z = [1,2,3]

    A1_val = random.choice(x)
    x.remove(A1_val)

    A2_val = random.choice(x)
    x.remove(A2_val)

    A3_val = x[0]

    B1_val = random.choice(y)
    y.remove(B1_val)

    B2_val = random.choice(y)
    y.remove(B2_val)

    B3_val = y[0]

    C1_val = random.choice(z)
    z.remove(C1_val)

    C2_val = random.choice(z)
    z.remove(C2_val)

    C3_val = z[0]


    X1.insert(0,"A" if (A1_val == 1) else "B" if (A1_val == 2) else "C")
    X2.insert(0,"A" if (A2_val == 1) else "B" if (A2_val == 2) else "C")
    X3.insert(0,"A" if (A3_val == 1) else "B" if (A3_val == 2) else "C")
    Y1.insert(0,"A" if (B1_val == 1) else "B" if (B1_val == 2) else "C")
    Y2.insert(0,"A" if (B2_val == 1) else "B" if (B2_val == 2) else "C")
    Y3.insert(0,"A" if (B3_val == 1) else "B" if (B3_val == 2) else "C")
    Z1.insert(0,"A" if (C1_val == 1) else "B" if (C1_val == 2) else "C")
    Z2.insert(0,"A" if (C2_val == 1) else "B" if (C2_val == 2) else "C")
    Z3.insert(0,"A" if (C3_val == 1) else "B" if (C3_val == 2) else "C")


def group_random ():
    group_1_random()
    group_2_random()

def group_1_clear ():

    A1.delete(0,END)
    A2.delete(0,END)
    A3.delete(0,END)
    B1.delete(0,END)
    B2.delete(0,END)
    B3.delete(0,END)
    C1.delete(0,END)
    C2.delete(0,END)
    C3.delete(0,END)
    R1_1.configure(text="")
    R2_1.configure(text="")
    R3_1.configure(text="")

    bg_group1("white",1,1)
    bg_group1("white",1,2)
    bg_group1("white",1,3)
    bg_group1("white",2,1)
    bg_group1("white",2,2)
    bg_group1("white",2,3)
    bg_group1("white",3,1)
    bg_group1("white",3,2)
    bg_group1("white",3,3)


def group_2_clear ():

    X1.delete(0,END)
    X2.delete(0,END)
    X3.delete(0,END)
    Y1.delete(0,END)
    Y2.delete(0,END)
    Y3.delete(0,END)
    Z1.delete(0,END)
    Z2.delete(0,END)
    Z3.delete(0,END)
    R1_2.configure(text="")
    R2_2.configure(text="")
    R3_2.configure(text="")

    bg_group2("white",1,1)
    bg_group2("white",1,2)
    bg_group2("white",1,3)
    bg_group2("white",2,1)
    bg_group2("white",2,2)
    bg_group2("white",2,3)
    bg_group2("white",3,1)
    bg_group2("white",3,2)
    bg_group2("white",3,3)

def group_clear ():
    group_1_clear ()
    group_2_clear ()

def group_1_is_full():
    #returns true is group 1 is empty

     ans = False if (A1.get()==""
     or A2.get()==""
     or A3.get()==""
     or B1.get()==""
     or B2.get()==""
     or B3.get()==""
     or C1.get()==""
     or C2.get()==""
     or C3.get()=="") else True
     return(ans)

def group_2_is_full():
    #returns true is group 2 is group_1_is empty

     ans = False if (X1.get()==""
     or X2.get()==""
     or X3.get()==""
     or Y1.get()==""
     or Y2.get()==""
     or Y3.get()==""
     or Z1.get()==""
     or Z2.get()==""
     or Z3.get()=="") else True
     return(ans)


def group_1_is_valid():
    #returns true is group 1 only has X,Y,Z

     ch = ["X","Y","Z"]
     ans = False if (A1.get() not in ch
     or A2.get() not in ch
     or A3.get() not in ch
     or B1.get() not in ch
     or B2.get() not in ch
     or B3.get() not in ch
     or C1.get() not in ch
     or C2.get() not in ch
     or C3.get() not in ch) else True
     return(ans)


def group_2_is_valid():
    #returns true is group 2 only has X,Y,Z

     ch = ["A","B","C"]
     ans = False if (X1.get() not in ch
     or X2.get() not in ch
     or X3.get() not in ch
     or Y1.get() not in ch
     or Y2.get() not in ch
     or Y3.get() not in ch
     or Z1.get() not in ch
     or Z2.get() not in ch
     or Z3.get() not in ch) else True
     return(ans)



def G1_to_2_sequence():
    R1_1.configure(text="")
    R2_1.configure(text="")
    R3_1.configure(text="")
    R1_2.configure(text="")
    R2_2.configure(text="")
    R3_2.configure(text="")

    personA_preference_list = [A1.get(),A2.get(),A3.get()]
    personB_preference_list = [B1.get(),B2.get(),B3.get()]
    personC_preference_list = [C1.get(),C2.get(),C3.get()]
    personX_preference_list = [X1.get(),X2.get(),X3.get()]
    personY_preference_list = [Y1.get(),Y2.get(),Y3.get()]
    personZ_preference_list = [Z1.get(),Z2.get(),Z3.get()]

    def ans_color_g1():
        def INDEX_REV(x):
            r = 0
            if(x==0):
                r = 3
            if(x==1):
                r = 2
            if(x==2):
                r = 1
            return(r)

        if(R1_2.cget("text") != ''):
            if(R1_2.cget("text") == "A"):
                bg_group2("yellow",1,INDEX_REV(personX_preference_list.index("A")))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("A")+1))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("A")+2))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("A")-1))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("A")-2))
            if(R1_2.cget("text") == "B"):
                bg_group2("yellow",1,INDEX_REV(personX_preference_list.index("B")))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("B")+1))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("B")+2))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("B")-1))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("B")-2))
            if(R1_2.cget("text") == "C"):
                bg_group2("yellow",1,INDEX_REV(personX_preference_list.index("C")))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("C")+1))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("C")+2))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("C")-1))
                bg_group2("white",1,INDEX_REV(personX_preference_list.index("C")-2))

        if(R2_2.cget("text") != ''):
            if(R2_2.cget("text") == "A"):
                bg_group2("yellow",2,INDEX_REV(personY_preference_list.index("A")))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("A")+1))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("A")+2))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("A")-1))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("A")-2))
            if(R2_2.cget("text") == "B"):
                bg_group2("yellow",2,INDEX_REV(personY_preference_list.index("B")))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("B")+1))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("B")+2))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("B")-1))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("B")-2))
            if(R2_2.cget("text") == "C"):
                bg_group2("yellow",2,INDEX_REV(personY_preference_list.index("C")))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("C")+1))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("C")+2))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("C")-1))
                bg_group2("white",2,INDEX_REV(personY_preference_list.index("C")-2))

        if(R3_2.cget("text") != ''):
            if(R3_2.cget("text") == "A"):
                bg_group2("yellow",3,INDEX_REV(personZ_preference_list.index("A")))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("A")+1))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("A")+2))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("A")-1))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("A")-2))
            if(R3_2.cget("text") == "B"):
                bg_group2("yellow",3,INDEX_REV(personZ_preference_list.index("B")))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("B")+1))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("B")+2))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("B")-1))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("B")-2))
            if(R3_2.cget("text") == "C"):
                bg_group2("yellow",3,INDEX_REV(personZ_preference_list.index("C")))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("C")+1))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("C")+2))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("C")-1))
                bg_group2("white",3,INDEX_REV(personZ_preference_list.index("C")-2))


    def part_1():
        if (personA_preference_list[0] == "X" and (R1_2.cget("text") == "" or personX_preference_list.index("A") <= personX_preference_list.index(R1_2.cget("text")))):
            R1_2.configure(text="A")
            bg_group1("green",1,len(personA_preference_list))
            ans_color_g1()

        elif (personA_preference_list[0] == "Y" and (R2_2.cget("text") == "" or personY_preference_list.index("A") <= personY_preference_list.index(R2_2.cget("text")))):
            R2_2.configure(text="A")
            bg_group1("green",1,len(personA_preference_list))
            ans_color_g1()

        elif (personA_preference_list[0] == "Z" and (R3_2.cget("text") == "" or personZ_preference_list.index("A") <= personZ_preference_list.index(R3_2.cget("text")))):
            R3_2.configure(text="A")
            bg_group1("green",1,len(personA_preference_list))
            ans_color_g1()

        else:
            personA_preference_list.pop(0)
            bg_group1("red",1,len(personA_preference_list)+2)
            timer()
            bg_group1("red",1,len(personA_preference_list)+1)
            timer()
            bg_group1("red",1,len(personA_preference_list))



    def part_2():
        if (personB_preference_list[0] == "X" and (R1_2.cget("text") == "" or personX_preference_list.index("B") <= personX_preference_list.index(R1_2.cget("text")))):
            R1_2.configure(text="B")
            bg_group1("green",2,len(personB_preference_list))
            ans_color_g1()
        elif (personB_preference_list[0] == "Y" and (R2_2.cget("text") == "" or personY_preference_list.index("B") <= personY_preference_list.index(R2_2.cget("text")))):
            R2_2.configure(text="B")
            bg_group1("green",2,len(personB_preference_list))
            ans_color_g1()
        elif (personB_preference_list[0] == "Z" and (R3_2.cget("text") == "" or personZ_preference_list.index("B") <= personZ_preference_list.index(R3_2.cget("text")))):
            R3_2.configure(text="B")
            bg_group1("green",2,len(personB_preference_list))
            ans_color_g1()
        else:
            personB_preference_list.pop(0)
            bg_group1("red",2,len(personB_preference_list)+2)
            timer()
            bg_group1("red",2,len(personB_preference_list)+1)
            timer()
            bg_group1("red",2,len(personB_preference_list))

    def part_3():
        if (personC_preference_list[0] == "X" and (R1_2.cget("text") == "" or personX_preference_list.index("C") <= personX_preference_list.index(R1_2.cget("text")))):
            R1_2.configure(text="C")
            bg_group1("green",3,len(personC_preference_list))
            ans_color_g1()
        elif (personC_preference_list[0] == "Y" and (R2_2.cget("text") == "" or personY_preference_list.index("C") <= personY_preference_list.index(R2_2.cget("text")))):
            R2_2.configure(text="C")
            bg_group1("green",3,len(personC_preference_list))
            ans_color_g1()
        elif (personC_preference_list[0] == "Z" and (R3_2.cget("text") == "" or personZ_preference_list.index("C") <= personZ_preference_list.index(R3_2.cget("text")))):
            R3_2.configure(text="C")
            bg_group1("green",3,len(personC_preference_list))
            ans_color_g1()
        else:
            personC_preference_list.pop(0)
            bg_group1("red",3,len(personC_preference_list)+2)
            timer()
            bg_group1("red",3,len(personC_preference_list)+1)
            timer()
            bg_group1("red",3,len(personC_preference_list))
            timer()

    while True:
        timer()
        part_1()
        timer()
        part_2()
        timer()
        part_3()
        if(R1_2.cget("text") != "" and R2_2.cget("text") != "" and R3_2.cget("text") != ""):
            break #end of function

def G2_to_1_sequence():
    R1_1.configure(text="")
    R2_1.configure(text="")
    R3_1.configure(text="")
    R1_2.configure(text="")
    R2_2.configure(text="")
    R3_2.configure(text="")

    personA_preference_list = [A1.get(),A2.get(),A3.get()]
    personB_preference_list = [B1.get(),B2.get(),B3.get()]
    personC_preference_list = [C1.get(),C2.get(),C3.get()]
    personX_preference_list = [X1.get(),X2.get(),X3.get()]
    personY_preference_list = [Y1.get(),Y2.get(),Y3.get()]
    personZ_preference_list = [Z1.get(),Z2.get(),Z3.get()]

    def ans_color_g2():
        def INDEX_REV(x):
            r = 0
            if(x==0):
                r = 3
            if(x==1):
                r = 2
            if(x==2):
                r = 1
            return(r)

        if(R1_1.cget("text") != ''):
            if(R1_1.cget("text") == "X"):
                bg_group1("yellow",1,INDEX_REV(personA_preference_list.index("X")))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("X")+1))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("X")+2))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("X")-1))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("X")-2))
            if(R1_1.cget("text") == "Y"):
                bg_group1("yellow",1,INDEX_REV(personA_preference_list.index("Y")))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("Y")+1))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("Y")+2))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("Y")-1))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("Y")-2))
            if(R1_1.cget("text") == "Z"):
                bg_group1("yellow",1,INDEX_REV(personA_preference_list.index("Z")))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("Z")+1))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("Z")+2))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("Z")-1))
                bg_group1("white",1,INDEX_REV(personA_preference_list.index("Z")-2))

        if(R2_1.cget("text") != ''):
            if(R2_1.cget("text") == "X"):
                bg_group1("yellow",2,INDEX_REV(personB_preference_list.index("X")))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("X")+1))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("X")+2))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("X")-1))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("X")-2))
            if(R2_1.cget("text") == "Y"):
                bg_group1("yellow",2,INDEX_REV(personB_preference_list.index("Y")))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("Y")+1))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("Y")+2))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("Y")-1))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("Y")-2))
            if(R2_1.cget("text") == "Z"):
                bg_group1("yellow",2,INDEX_REV(personB_preference_list.index("Z")))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("Z")+1))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("Z")+2))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("Z")-1))
                bg_group1("white",2,INDEX_REV(personB_preference_list.index("Z")-2))

        if(R3_1.cget("text") != ''):
            if(R3_1.cget("text") == "X"):
                bg_group1("yellow",3,INDEX_REV(personC_preference_list.index("X")))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("X")+1))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("X")+2))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("X")-1))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("X")-2))
            if(R3_1.cget("text") == "Y"):
                bg_group1("yellow",3,INDEX_REV(personC_preference_list.index("Y")))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("Y")+1))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("Y")+2))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("Y")-1))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("Y")-2))
            if(R3_1.cget("text") == "Z"):
                bg_group1("yellow",3,INDEX_REV(personC_preference_list.index("Z")))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("Z")+1))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("Z")+2))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("Z")-1))
                bg_group1("white",3,INDEX_REV(personC_preference_list.index("Z")-2))


    def part_1():
        if (personX_preference_list[0] == "A" and (R1_1.cget("text") == "" or personA_preference_list.index("X") <= personA_preference_list.index(R1_1.cget("text")))):
            R1_1.configure(text="X")
            bg_group2("green",1,len(personX_preference_list))
            ans_color_g2()

        elif (personX_preference_list[0] == "B" and (R2_1.cget("text") == "" or personB_preference_list.index("X") <= personB_preference_list.index(R2_1.cget("text")))):
            R2_1.configure(text="X")
            bg_group2("green",1,len(personX_preference_list))
            ans_color_g2()

        elif (personX_preference_list[0] == "C" and (R3_1.cget("text") == "" or personC_preference_list.index("X") <= personC_preference_list.index(R3_1.cget("text")))):
            R3_1.configure(text="X")
            bg_group2("green",1,len(personX_preference_list))
            ans_color_g2()

        else:
            personX_preference_list.pop(0)
            bg_group2("red",1,len(personX_preference_list)+2)
            timer()
            bg_group2("red",1,len(personX_preference_list)+1)
            timer()
            bg_group2("red",1,len(personX_preference_list))



    def part_2():
        if (personY_preference_list[0] == "A" and (R1_1.cget("text") == "" or personA_preference_list.index("Y") <= personA_preference_list.index(R1_1.cget("text")))):
            R1_1.configure(text="Y")
            bg_group2("green",2,len(personY_preference_list))
            ans_color_g2()
        elif (personY_preference_list[0] == "B" and (R2_1.cget("text") == "" or personB_preference_list.index("Y") <= personB_preference_list.index(R2_1.cget("text")))):
            R2_1.configure(text="Y")
            bg_group2("green",2,len(personY_preference_list))
            ans_color_g2()
        elif (personY_preference_list[0] == "C" and (R3_1.cget("text") == "" or personC_preference_list.index("Y") <= personC_preference_list.index(R3_1.cget("text")))):
            R3_1.configure(text="Y")
            bg_group2("green",2,len(personY_preference_list))
            ans_color_g2()
        else:
            personY_preference_list.pop(0)
            bg_group2("red",2,len(personY_preference_list)+2)
            timer()
            bg_group2("red",2,len(personY_preference_list)+1)
            timer()
            bg_group2("red",2,len(personY_preference_list))

    def part_3():
        if (personZ_preference_list[0] == "A" and (R1_1.cget("text") == "" or personA_preference_list.index("Z") <= personA_preference_list.index(R1_1.cget("text")))):
            R1_1.configure(text="Z")
            bg_group2("green",3,len(personZ_preference_list))
            ans_color_g2()
        elif (personZ_preference_list[0] == "B" and (R2_1.cget("text") == "" or personB_preference_list.index("Z") <= personB_preference_list.index(R2_1.cget("text")))):
            R2_1.configure(text="Z")
            bg_group2("green",3,len(personZ_preference_list))
            ans_color_g2()
        elif (personZ_preference_list[0] == "C" and (R3_1.cget("text") == "" or personC_preference_list.index("Z") <= personC_preference_list.index(R3_1.cget("text")))):
            R3_1.configure(text="Z")
            bg_group2("green",3,len(personZ_preference_list))
            ans_color_g2()
        else:
            personZ_preference_list.pop(0)
            bg_group2("red",3,len(personZ_preference_list)+2)
            timer()
            bg_group2("red",3,len(personZ_preference_list)+1)
            timer()
            bg_group2("red",3,len(personZ_preference_list))
            timer()

    while True:
        timer()
        part_1()
        timer()
        part_2()
        timer()
        part_3()
        if(R1_1.cget("text") != "" and R2_1.cget("text") != "" and R3_1.cget("text") != ""):
            break #end of function


def popup_box (msg):
    popup = Tk()
    popup.wm_title("Error!!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy )
    B1.pack()

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True

def clear_all_color():
    bg_group1("white",1,1)
    bg_group1("white",1,2)
    bg_group1("white",1,3)
    bg_group1("white",2,1)
    bg_group1("white",2,2)
    bg_group1("white",2,3)
    bg_group1("white",3,1)
    bg_group1("white",3,2)
    bg_group1("white",3,3)
    bg_group2("white",1,1)
    bg_group2("white",1,2)
    bg_group2("white",1,3)
    bg_group2("white",2,1)
    bg_group2("white",2,2)
    bg_group2("white",2,3)
    bg_group2("white",3,1)
    bg_group2("white",3,2)
    bg_group2("white",3,3)



def Run_sequence():

    if (options.get()==0):
        popup_box ("please select a option for which set proposes to which")
    elif (group_1_is_full() == False or group_2_is_full() == False):
        popup_box ("Values missing!! Please Enter the XYZ and or ABC values")
    elif (group_1_is_valid() == False or group_2_is_valid() == False):
        popup_box ("Incorect Values!! Please Enter Valid XYZ and or ABC values")
    elif (is_integer(auto_tick.get())== False):
        popup_box ("Incorect time Value!! Please Enter a valid integer value")
    elif(options.get()==1):
        try:
            clear_all_color()
            Run_Button_auto.configure(state ="disabled",text="running...")
            G1_to_2_sequence()
            Run_Button_auto.configure(state ="normal",text="run again")
        except Exception:
            popup_box ("Something went wrong. Close the program and try again.")
    elif(options.get()==2):
        try:
            clear_all_color()
            Run_Button_auto.configure(state ="disabled",text="running...")
            G2_to_1_sequence()
            Run_Button_auto.configure(state ="normal",text="run again")
        except Exception:
            popup_box ("Something went wrong. Close the program and try again.")

window.mainloop()
