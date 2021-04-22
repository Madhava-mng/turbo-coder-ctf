#!/bin/env python3


from base64 import *
from codelib.rot import *
from tkinter import *
from time import sleep as _sleep
from threading import Thread as _thread


root=Tk()
root.title('turbo coder ctf')
frame=LabelFrame(root,text="values",padx=71,pady=70,bg="gray")
frame2=LabelFrame(root,text="theams", padx=143,  pady=60,bg="gray")
frame3=LabelFrame(root,text="expresion", padx=108,  pady=40,bg="gray")
frame. grid(row= 1, column= 0)
frame3.grid(row= 2, column= 0)
frame2.grid(row= 3, column= 0)


ebgc = "green"
bgc = "gray"

def notify(value, bg):
	global bgc
	msg_label = Label(root, text=value, width=58, borderwidth=3, bg=bg, fg="black")
	msg_label.grid(row=4,column=0)
	_sleep(2)
	msg_label.destroy()
	msg_label = Label(root, width=58, borderwidth=3, bg=bgc)
	msg_label.grid(row=4,column=0)

def ecode():
	a=e1.get().encode()
	result=b64encode(a)
	v.set(result.decode())
	frame.configure(text = "Length: "+str(len(e1.get()))+"  |   base64encode")


_thread(target=notify, args = ['app started', 'green']).start()

def dcode():
	try:
		a=e1.get().encode()
		result=b64decode(a)
		v.set(result.decode())
		frame.configure(text = "Length: "+str(len(e1.get()))+"  |   base64decode")
	except:
		_thread(target=notify, args = ['unable to decode base64', 'red']).start()

def b32e():
	a=e1.get().encode()
	result=b32encode(a)
	v.set(result.decode())
	frame.configure(text = "Length: "+str(len(e1.get()))+"  |   base32encode")

def b32d():
	try:
		a=e1.get().encode()
		result=b32decode(a)
		v.set(result.decode())
		frame.configure(text = "Length: "+str(len(e1.get()))+"  |   base64decode")
	except:
		_thread(target=notify, args = ['unable to decode base32', 'red']).start()

def b16e():
	a=e1.get().encode()
	result=b16encode(a)
	v.set(result.decode())
	frame.configure(text = "Length: "+str(len(e1.get()))+"  |   base16encode")

def b16d():
	try:
		a=e1.get().encode()
		result=b16decode(a)
		v.set(result.decode())
		frame.configure(text = "Length: "+str(len(e1.get()))+"  |   base16decode")
	except:
		_thread(target=notify, args = ['unable to decode base16(hex)', 'red']).start()

def rot13_():
	a=e1.get()
	result= rot13(a)
	v.set(result)
	frame.configure(text = "Length: "+str(len(e1.get()))+"  |   rot13")

def rot13add():
	a=e1.get()
	result= rot13IterForword(a, 1)
	v.set(result)
	frame.configure(text = "Length: "+str(len(e1.get()))+"  |   rot13add")

def rot13sub():
	a=e1.get()
	result= rot13IterBackword(a, 1)
	v.set(result)
	frame.configure(text = "Length: "+str(len(e1.get()))+"  |   rot13sub")


def rot47_():
	a=e1.get()
	result= rot47(a)
	v.set(result)
	frame.configure(text = "Length: "+str(len(e1.get()))+"  |   rot47")

def rot47add():
	a=e1.get()
	result= rot47IterForword(a, 1)
	v.set(result)
	frame.configure(text = "Length: "+str(len(e1.get()))+"  |   rot47add")

def rot47sub():
	a=e1.get()
	result= rot47IterBackword(a, 1)
	v.set(result)
	frame.configure(text = "Length: "+str(len(e1.get()))+"  |   rot47sub")

def clear():
	e1.delete(0,END)
	frame.configure(text = "Length: "+str(len(e1.get())))
	_thread(target=notify, args = ['cleared!', 'green']).start()



def color(color):
	global bgc
	bgc = "darkgoldenrod"
	fgc = "black"
	ebgc = "blue"
	_thread(target=notify, args = ['theme: '+color, 'yellow']).start()
	
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
	_thread(target=notify, args = ['copied!', 'green']).start()


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


root.mainloop()