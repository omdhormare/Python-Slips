from  tkinter  import*
import datetime
window=Tk()
window.geometry("500x500")

def cal():
    a=int(e1.get())
    b=int(e2.get())
    c=int(e3.get())

    day=datetime.date.today()

    aa=day.day-a
    bb=day.month-b
    cc=day.year-c

    e11.insert(0,aa);
    e22.insert(0,bb);
    e33.insert(0,cc);
    


l1=Label(window,text="Enter Your Birthdate Day : ")
l1.pack()

e1=Entry(window,width=20)
e1.pack()

l2=Label(window,text="Enter Your Birthdate Month : ")
l2.pack()

e2=Entry(window,width=20)
e2.pack()

l3=Label(window,text="Enter Your Birthdate Year : ")
l3.pack()

e3=Entry(window,width=20)
e3.pack()

b=Button(window,text="Calculate Age ",command=cal)
b.pack()

p=Label(window,text="--------------------------------------------------------------------------------------------------")
p.pack()
l11=Label(window,text="Calculate Day : ")
l11.pack()

e11=Entry(window,width=20)
e11.pack()

l22=Label(window,text="Calculate Month : ")
l22.pack()

e22=Entry(window,width=20)
e22.pack()

l33=Label(window,text="Calculate Year : ")
l33.pack()

e33=Entry(window,width=20)
e33.pack()


window.mainloop()
