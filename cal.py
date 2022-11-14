from tkinter import *
import tkinter
from tkinter import messagebox
val = ''
a = 0
op = ''

def btn_1_isclicked():
	global val
	val = val + '1'
	data.set(val)

def btn_2_isclicked():
	global val
	val = val + '2'
	data.set(val)

def btn_3_isclicked():
	global val
	val = val + '3'
	data.set(val)

def btn_4_isclicked():
	global val
	val = val + '4'
	data.set(val)

def btn_5_isclicked():
	global val
	val = val + '5'
	data.set(val)

def btn_6_isclicked():
	global val
	val = val + '6'
	data.set(val)

def btn_7_isclicked():
	global val
	val = val + '7'
	data.set(val)

def btn_8_isclicked():
	global val
	val = val + '8'
	data.set(val)

def btn_9_isclicked():
	global val
	val = val + '9'
	data.set(val)

def btn_0_isclicked():
	global val
	val = val + '0'
	data.set(val)

def btn_plus_clicked():
	global a
	global op
	global val
	a = int(val)
	op = '+'
	val = val + "+"
	data.set(val)

def btn_minus_clicked():
	global a
	global op
	global val
	a = int(val)
	op = '-'
	val = val + "-"
	data.set(val)

def btn_mul_clicked():
	global a
	global op
	global val
	a = int(val)
	op = '*'
	val = val + "*"
	data.set(val)

def btn_div_clicked():
	global a
	global op
	global val
	a = int(val)
	op = '/'
	val = val + "/"
	data.set(val)

def c_pressed():
	global a
	global val
	global op
	val = ''
	a = 0
	op = ''
	data.set(val)

def result():
	global a
	global val
	global op
	val2 = val
	if op == '+':
		x = int((val2.split('+')[1]))
		c = a + x
		data.set(c)
		val = str(c)
	elif op == '-':
		x = int((val2.split('-')[1]))
		c = a - x
		data.set(c)
		val = str(c)
	elif op == '*':
		x = int((val2.split('*')[1]))
		c = a * x
		data.set(c)
		val = str(c)
	elif op == '/':
		x = int((val2.split('/')[1]))
		if x == 0:
			messagebox.showerror('Error','Divison by 0 not Supported')
			a = ""
			val = ""
			data.set(val)
		else:
			c = int(a/x)
			data.set(c)
			val = str(c)
	else:
		pass
#Create window
root = tkinter.Tk()
root.geometry("250x400+300+300")

#(0,0 for not resize window)
root.resizable(0,0)

#title
root.title("Calculator")

#Label
data = StringVar()
lb = Label(
	root, 
	text='Label', 
	font=('verdana,22,bold'),
	anchor=SE, 
	textvariable = data,
	background = '#ffffff',
	fg = '#000000'

	)
	
lb.pack(expand=True, fill='both') 

#Frame
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = 'both',)

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = 'both',)

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = 'both',)

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = 'both',)

#Button btnrow1
btn1 = Button(btnrow1,text="1",font=("verdana",22),relief=GROOVE, border=0,command=btn_1_isclicked,)
btn1.pack(side=LEFT, expand=True, fill='both', )

btn2 = Button(btnrow1,text="2",font=("verdana",22),relief=GROOVE, border=0,command=btn_2_isclicked,)
btn2.pack(side=LEFT, expand=True, fill='both', )

btn3 = Button(btnrow1,text="3",font=("verdana",22),relief=GROOVE, border=0,command=btn_3_isclicked,)
btn3.pack(side=LEFT, expand=True, fill='both', )

btnplus= Button(btnrow1,text="+",font=("verdana",22),relief=GROOVE, border=0,command=btn_plus_clicked)
btnplus.pack(side=LEFT, expand=True, fill='both', )

#Button btnrow2
btn4 = Button(btnrow2,text="4",font=("verdana",22),relief=GROOVE, border=0,command=btn_4_isclicked,)
btn4.pack(side=LEFT, expand=True, fill='both', )

btn5 = Button(btnrow2,text="5",font=("verdana",22),relief=GROOVE, border=0,command=btn_5_isclicked,)
btn5.pack(side=LEFT, expand=True, fill='both', )

btn6 = Button(btnrow2,text="6",font=("verdana",22),relief=GROOVE, border=0,command=btn_6_isclicked,)
btn6.pack(side=LEFT, expand=True, fill='both', )

btnminus = Button(btnrow2,text="-",font=("verdana",22),relief=GROOVE, border=0,command=btn_minus_clicked)
btnminus.pack(side=LEFT, expand=True, fill='both', )

#Button btnrow3
btn7 = Button(btnrow3,text="7",font=("verdana",22),relief=GROOVE, border=0,command=btn_7_isclicked,)
btn7.pack(side=LEFT, expand=True, fill='both', )

btn8 = Button(btnrow3,text="8",font=("verdana",22),relief=GROOVE, border=0,command=btn_8_isclicked,)
btn8.pack(side=LEFT, expand=True, fill='both', )

btn9 = Button(btnrow3,text="9",font=("verdana",22),relief=GROOVE, border=0,command=btn_9_isclicked,)
btn9.pack(side=LEFT, expand=True, fill='both', )

btnmul = Button(btnrow3,text="*",font=("verdana",22),relief=GROOVE, border=0,command=btn_mul_clicked)
btnmul.pack(side=LEFT, expand=True, fill='both', )

#Button btnrow4
btnc = Button(btnrow4,text="C",font=("verdana",22),relief=GROOVE, border=0,command=c_pressed,)
btnc.pack(side=LEFT, expand=True, fill='both', )

btn0 = Button(btnrow4,text="0",font=("verdana",22),relief=GROOVE, border=0,command=btn_0_isclicked,)
btn0.pack(side=LEFT, expand=True, fill='both', )

btnequal = Button(btnrow4,text="=",font=("verdana",22),relief=GROOVE, border=0,command=result,)
btnequal.pack(side=LEFT, expand=True, fill='both', )

btndiv = Button(btnrow4,text="/",font=("verdana",22),relief=GROOVE, border=0,command=btn_div_clicked)
btndiv.pack(side=LEFT, expand=True, fill='both', )
root.mainloop(  )

