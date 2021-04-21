from base64 import *
from codelib.rot import *
try:
	from tkinter import *
except:
	from Tkinter import *


root=Tk()
root.title('turbo coder ctf')
frame=LabelFrame(root,text="values",padx=71,pady=70,bg="gray")
frame2=LabelFrame(root,text="theams", padx=143,  pady=40,bg="gray")
frame3=LabelFrame(root,text="expresion", padx=108,  pady=20,bg="gray")
frame. grid(row= 1, column= 0)
frame3.grid(row= 2, column= 0)
frame2.grid(row= 3, column= 0)


ebgc = "green"

def ecode():
	a=e1.get().encode()
	result=b64encode(a)
	v.set(result.decode())

def dcode():
	try:
		a=e1.get().encode()
		result=b64decode(a)
		v.set(result.decode())
	except:
		pass

def b32e():
	a=e1.get().encode()
	result=b32encode(a)
	v.set(result.decode())

def b32d():
	try:
		a=e1.get().encode()
		result=b32decode(a)
		v.set(result.decode())
	except:
		pass

def b16e():
	a=e1.get().encode()
	result=b16encode(a)
	v.set(result.decode())

def b16d():
	try:
		a=e1.get().encode()
		result=b16decode(a)
		v.set(result.decode())
	except:
		pass

def rot13_():
	a=e1.get()
	result= rot13(a)
	v.set(result)

def rot13add():
	a=e1.get()
	result= rot13IterForword(a, 1)
	v.set(result)

def rot13sub():
	a=e1.get()
	result= rot13IterBackword(a, 1)
	v.set(result)

def rot47_():
	a=e1.get()
	result= rot47(a)
	v.set(result)

def rot47add():
	a=e1.get()
	result= rot47IterForword(a, 1)
	v.set(result)

def rot47sub():
	a=e1.get()
	result= rot47IterBackword(a, 1)
	v.set(result)

def clear():
	e1.delete(0,END)


def color(color):
	bgc = "darkgoldenrod"
	fgc = "black"
	ebgc = "blue"
	
	if (color == 'gray_green'):
		bgc="gray"
		fgc="white"
		ebgc="green"
	elif(color.strip() == 'dark__blue'):
		bgc="black"
		fgc="white"
		ebgc="blue"

	frame.configure(bg=bgc, fg="white")
	frame2.configure(bg=bgc, fg="white")
	frame3.configure(bg=bgc, fg="white")
	e1.configure(bg=ebgc)

def helpp():
	l=Label(frame2,text="thats the base64 decode & encode window")
	l.grid(row=1,column=0)

def cp_to_cb():
	root.clipboard_clear()
	root.clipboard_append(str(v.get()))


v = StringVar()
e1=Entry(frame,width=40,bg="blue",fg="white", textvariable=v)
e1.grid(row=1,column=1)



but1=Button(frame3, width=7, text="b64enc",bg="black",fg="white",command=ecode)
but2=Button(frame3, width=7, text="b64dec",bg="black",fg="white",command=dcode)
but3=Button(frame3, width=7, text="b32enc",bg="black",fg="white",command=b32e)
but4=Button(frame3, width=7, text="b32dec",bg="black",fg="white",command=b32d)
but5=Button(frame3, width=7, text="b16enc",bg="black",fg="white",command=b16e)
but6=Button(frame3, width=7, text="b16dec",bg="black",fg="white",command=b16d)
but7=Button(frame3, width=7, text="clear",bg="green",fg="white",command=clear)
but8=Button(frame3, width=7, text="copy",bg="blue",fg="white",command=cp_to_cb)
but9=Button(frame3, width=7, text=" exit ",bg="red",fg="white",command=exit)
but10=Button(frame3, width=7, text="rot13",bg="black",fg="white",command=rot13_)
but11=Button(frame3, width=7, text="rot13add",bg="black",fg="white",command=rot13add)
but12=Button(frame3, width=7, text="rot13sub",bg="black",fg="white",command=rot13sub)
but13=Button(frame3, width=7, text="rot47",bg="black",fg="white",command=rot47_)
but14=Button(frame3, width=7, text="rot47add",bg="black",fg="white",command=rot47add)
but15=Button(frame3, width=7, text="rot47sub",bg="black",fg="white",command=rot47sub)


but1.grid(row=0,column=0)
but2.grid(row=0,column=1)
but9.grid(row=0,column=2)
but3.grid(row=1,column=0)
but4.grid(row=1,column=1)
but8.grid(row=1,column=2)
but5.grid(row=2,column=0)
but6.grid(row=2,column=1)
but7.grid(row=2,column=2)
but10.grid(row=3,column=0)
but11.grid(row=3,column=1)
but12.grid(row=3,column=2)
but13.grid(row=4,column=0)
but14.grid(row=4,column=1)
but15.grid(row=4,column=2)



# color changing

color_list = [ 'mangoblue', 'gray_green','dark__blue' ]

help_btn = Button(frame2,text="help", bg="black",fg="white",command=helpp)
clicked = StringVar()
clicked.set(color_list[0])

color_menu = OptionMenu(frame2 , clicked, *color_list)
color_btn = Button(frame2,text="apply",  bg="black", fg="white",  command=lambda:color(clicked.get()))

color_btn.grid(row = 0, column=1)
color_menu.grid(row = 0, column=0)
help_btn.grid(row=0,column=1)

#frame.configure(bg="red")

root.mainloop()
