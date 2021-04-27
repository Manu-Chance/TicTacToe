#!python3

from tkinter import *
import time


# Tkinter class
class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master

def check_win():
	if b1['text'] == 'x' and b2['text'] == 'x' and b3['text'] == 'x':
		print('X won!')
		b1.configure(bg='cyan')
		b2.configure(bg='cyan')
		b3.configure(bg='cyan')

def apply_turn():
	for i in range(3):
		var_name[i].configure(text='HOLY SHIT')


def alternate_turn():
	if turn_x['bg'] == 'green':
		print("It's X turn")
		turn_x.configure(bg='red')
		turn_o.configure(bg='green')
	else:
		print("It's O turn")
		turn_x.configure(bg='green')
		turn_o.configure(bg='red')

root = Tk()
app = Window(root)
root.wm_title("Tic Tac Toe")
root.geometry('1000x600')
root.resizable(0,0)
root.configure(bg='black')

x_v = 100
y_v = 100
b1 = Button(root, bg='purple', text='x')
b1.place(bordermode=OUTSIDE, height=100, width=100, x=x_v ,y=y_v)
b2 = Button(root, bg='purple', text='2')
b2.place(height=100, width=100, x=x_v + 125, y=y_v)
b3 = Button(root, bg='purple', text='3')
b3.place(height=100, width=100, x=x_v + 125*2, y=y_v)
b4 = Button(root, bg='purple', text='4')
b4.place(height=100, width=100, x=x_v, y=y_v + 125)
b5 = Button(root, bg='purple', text='5')
b5.place(height=100, width=100, x=x_v + 125, y=y_v + 125)
b6 = Button(root, bg='purple', text='6')
b6.place(height=100, width=100, x=x_v + 125*2, y=y_v+125)
b7 = Button(root, bg='purple', text='7')
b7.place(height=100, width=100, x=x_v, y=y_v + 125*2)
b8 = Button(root, bg='purple', text='8')
b8.place(height=100, width=100, x=x_v + 125, y=y_v + 125*2)
b9 = Button(root, bg='purple', text='9', command=alternate_turn)
b9.place(height=100, width=100, x=x_v + 125*2, y=y_v + 125*2)

var_name = [b1, b2, b3]

turn_x = Label(text='X', bg='green')
turn_x.place(height=50, width=100, x=100, y=25)
turn_o = Label(text='O', bg='red')
turn_o.place(height=50, width=100, x=350, y=25)

apply_turn()
check_win()
alternate_turn()
root.mainloop()
