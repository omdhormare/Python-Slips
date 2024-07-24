# Write Python GUI program which accepts a number n to displays each digit of number in words.

from tkinter import *
window=Tk()
def digit_word():
    n=e.get()
    e1.delete(0,END)
    for i in n:
        if(i=='1'):
            e1.insert(END,"One")
        elif(i=='2'):
            e1.insert(END,"Two ")
        elif(i=='3'):
            e1.insert(END,"Three ")
        elif(i=='4'):
            e1.insert(END,"Four ")
        elif(i=='5'):
            e1.insert(END,"Five ")
        elif(i=='6'):
            e1.insert(END,"Six ")
        elif(i=='7'):
            e1.insert(END,"Seven ")
        elif(i=='8'):
            e1.insert(END,"Eight ")                        
        elif(i=='9'):
            e1.insert(END,"Nine ") 
        elif(i=='0'):
            e1.insert(END,"Zero ") 
window.geometry("500x500")
l=Label(window,text="Enter Number : ",font=("arial",20))
l.pack()

e=Entry(window,width=20,font=("arial",20))
e.pack()

l1=Label(window,text="Word Number : ",font=("arial",20))
l1.pack()

e1=Entry(window,width=20,font=("arial",20),bg="black",fg="white")
e1.pack()

b=Button(window,text="submit",font=("arial",20),command=digit_word)
b.pack()
window.mainloop()