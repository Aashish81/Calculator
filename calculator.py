from tkinter import *
root= Tk()
root.title("Simple Calculator")
entry= Entry(root,width=50,borderwidth=5)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
def button_click(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))
def button_add():
    first_num=entry.get()
    global f_name
    global math
    math =  "addition"
    f_name= int(first_num)
    entry.delete(0,END)
def button_subtract():
    first_num=entry.get()
    global f_name
    global math
    math ="subtraction"
    f_name= int(first_num)
    entry.delete(0,END)
def button_multiply():
    first_num=entry.get()
    global f_name
    global math
    math = "multiplication"
    f_name= int(first_num)
    entry.delete(0,END)
def button_divide():
    first_num=entry.get()
    global f_name
    global math
    math =  "division"
    f_name= int(first_num)
    entry.delete(0,END)
def button_clear():
     entry.delete(0,END)
def button_equal():
    second_number= entry.get()
    entry.delete(0,END)
    if math == "addition":
        entry.insert(0,f_name+ int(second_number))
    elif math=="subtraction":
        entry.insert(0,f_name - int(second_number))
    elif math == "multiplication":
        entry.insert(0, f_name *int(second_number))
    elif math == "division":
        entry.insert(0, f_name /int(second_number))
  #Creating the buttons
button_1= Button(root,text="1",padx=40,pady=40,bg="yellow",fg="black",command=lambda:button_click(1))#using lambda function cause its the only way to assign value to the function!
button_2= Button(root,text="2",padx=40,pady=40,bg="yellow",fg="black",command=lambda:button_click(2))
button_3= Button(root,text="3",padx=40,pady=40,bg="yellow",fg="black",command=lambda:button_click(3))
button_4= Button(root,text="4",padx=40,pady=40,bg="yellow",fg="black",command=lambda:button_click(4))
button_5= Button(root,text="5",padx=40,pady=40,bg="yellow",fg="black",command=lambda:button_click(5))
button_6= Button(root,text="6",padx=40,pady=40,bg="yellow",fg="black",command=lambda:button_click(6))
button_7= Button(root,text="7",padx=40,pady=40,bg="yellow",fg="black",command=lambda:button_click(7))
button_8= Button(root,text="8",padx=40,pady=40,bg="yellow",fg="black",command=lambda:button_click(8))
button_9= Button(root,text="9",padx=40,pady=40,bg="yellow",fg="black",command=lambda:button_click(9))
button_0= Button(root,text="0",padx=40,pady=40,bg="yellow",fg="black",command=lambda:button_click(0))
button_add= Button(root,text="+",padx=48,pady=40,bg="orange",fg="black",command=button_add)
button_subtract= Button(root,text="-",padx=48,bg="orange",fg="black",pady=40,command=button_subtract)
button_multiply= Button(root,text="*",padx=40,pady=40,bg="orange",fg="black",command=button_multiply)
button_divide= Button(root,text="%",padx=40,pady=40,bg="orange",fg="black",command=button_divide)
button_clear= Button(root,text="Clear",padx=40,pady=40,bg="crimson",fg="black",command=button_clear)
button_equal= Button(root,text="=",padx=48,pady=40,bg="black",fg="white",command=button_equal)
    #Displaying buttons
button_equal.grid(row=4,column=3)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=2,column=3)
button_subtract.grid(row=3,column=3)
button_multiply.grid(row=4,column=1)
button_divide.grid(row=4,column=2)
button_clear.grid(row=1,column=3)
root.mainloop()