import numbers
from math import*
from tkinter import*
from unittest.util import strclass

def btnClick(number):
    current=e.get() #nolasa esošo skaitli
    e.delete(0,END) #nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) #ievieto displejā
    return 0

def btnCommand(command):
    global number
    global num1
    global mathOp 
    mathOp=command #+ - * /
    num1=int(e.get())
    e.delete(0,END)
    return 0

def btnEquals():
    num2=0
    num2=float(e.get())
    result=0
    if num2!=0:
        if mathOp=="+":
            result=num1+num2
        elif mathOp=="-":
            result=num1-num2
        elif mathOp=="x":
            result=num1*num2
        elif mathOp=="/":
            result=num1/num2
        elif mathOp=="%":
            result=(0.01*num1)*num2
        elif mathOp=="_/":
            result=num2**(1/num1)
        else:
            result=0
    elif num2==0:
        if mathOp=="%":
            result=num1*0.01
        elif mathOp=="_/":
            result=num1**0.5
        else:
            result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0 

def Clear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

print("python strādā")
mansLogs=Tk()
mansLogs.title("Kalkulators")
e=Entry(mansLogs,width=15, bd=20, font=("Daytona",20))
btn0=Button(mansLogs, text="0", padx="40",bd=10 , pady="20", command=lambda:btnClick(0))
btn1=Button(mansLogs, text="1", padx="40",bd=10 , pady="20", command=lambda:btnClick(1))
btn2=Button(mansLogs, text="2", padx="40",bd=10 , pady="20", command=lambda:btnClick(2))
btn3=Button(mansLogs, text="3", padx="40",bd=10 , pady="20", command=lambda:btnClick(3))
btn4=Button(mansLogs, text="4", padx="40",bd=10 , pady="20", command=lambda:btnClick(4))
btn5=Button(mansLogs, text="5", padx="40",bd=10 , pady="20", command=lambda:btnClick(5))
btn6=Button(mansLogs, text="6", padx="40",bd=10 , pady="20", command=lambda:btnClick(6))
btn7=Button(mansLogs, text="7", padx="40",bd=10 , pady="20", command=lambda:btnClick(7))
btn8=Button(mansLogs, text="8", padx="40",bd=10 , pady="20", command=lambda:btnClick(8))
btn9=Button(mansLogs, text="9", padx="40",bd=10 , pady="20", command=lambda:btnClick(9))

btnnodzes=Button(mansLogs, text="C", padx="40",bd=10 , pady="20", command=Clear)
btnvienadiba=Button(mansLogs, text="=", padx="40",bd=10 , pady="20", command=btnEquals)

btnminus=Button(mansLogs, text="-", padx="40",bd=10 , pady="20", command=lambda:btnCommand("-"))
btnpluss=Button(mansLogs, text="+", padx="40", bd=10 ,pady="20", command=lambda:btnCommand("+"))
btnreiz=Button(mansLogs, text="x", padx="40", bd=10 ,pady="20", command=lambda:btnCommand("*"))
btndev=Button(mansLogs, text="/", padx="40", bd=10 ,pady="20", command=lambda:btnCommand("/"))
btnprocent=Button(mansLogs, text="%", padx="40", bd=10 ,pady="20", command=lambda:btnCommand("%"))
btnsqrt=Button(mansLogs, text="_/", padx="40", bd=10 ,pady="20", command=lambda:btnCommand("_/"))


btn1.grid(row=1,column=1)
btn2.grid(row=1,column=2)
btn3.grid(row=1,column=3)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)
btn6.grid(row=2,column=3)
btn7.grid(row=3,column=1)
btn8.grid(row=3,column=2)
btn9.grid(row=3,column=3)

btnnodzes.grid(row=4,column=1)
btn0.grid(row=4,column=2)
btnvienadiba.grid(row=4,column=3)

btnpluss.grid(row=1,column=4)
btnminus.grid(row=2,column=4)
btnreiz.grid(row=3,column=4)
btndev.grid(row=4,column=4)

btnprocent.grid(row=1,column=6)
btnsqrt.grid(row=2,column=6)

e.grid(row=0, column=1, columnspan=4)

mansLogs.mainloop()

