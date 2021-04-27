#!python3
from tkinter import *
import time

def check_win():
    right_down = [2,5,8]
    middle_down = [1,4,7]
    left_down = [0,3,6]

    diagonal_left = [0,4,8]
    diagonal_right = [2,4,6]

    up_right = [0,1,2]
    middle_right = [3,4,5]
    down_right = [6,7,8]

    x_val = 175
    y_val = 25

    if b_var[0]['text'] == 'X' and b_var[1]['text'] == 'X' and b_var[2]['text'] == 'X':
        for i in up_right:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='X WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[3]['text'] == 'X' and b_var[4]['text'] == 'X' and b_var[5]['text'] == 'X':
        for i in middle_right:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='X WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[6]['text'] == 'X' and b_var[7]['text'] == 'X' and b_var[8]['text'] == 'X':
        for i in down_right:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='X WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[0]['text'] == 'X' and b_var[4]['text'] == 'X' and b_var[8]['text'] == 'X':
        for i in diagonal_left:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='X WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[2]['text'] == 'X' and b_var[4]['text'] == 'X' and b_var[6]['text'] == 'X':
        for i in diagonal_right:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='X WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()    
    elif b_var[0]['text'] == 'X' and b_var[3]['text'] == 'X' and b_var[6]['text'] == 'X':
        for i in left_down:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='X WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[1]['text'] == 'X' and b_var[4]['text'] == 'X' and b_var[7]['text'] == 'X':
        for i in middle_down:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='X WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[2]['text'] == 'X' and b_var[5]['text'] == 'X' and b_var[8]['text'] == 'X':
        for i in right_down:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='X WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    

    if b_var[0]['text'] == 'O' and b_var[1]['text'] == 'O' and b_var[2]['text'] == 'O':
        for i in up_right:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='O WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[3]['text'] == 'O' and b_var[4]['text'] == 'O' and b_var[5]['text'] == 'O':
        for i in middle_right:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='O WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[6]['text'] == 'O' and b_var[7]['text'] == 'O' and b_var[8]['text'] == 'O':
        for i in down_right:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='O WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[0]['text'] == 'O' and b_var[4]['text'] == 'O' and b_var[8]['text'] == 'O':
        for i in diagonal_left:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='O WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[2]['text'] == 'O' and b_var[4]['text'] == 'O' and b_var[6]['text'] == 'O':
        for i in diagonal_right:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='O WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[0]['text'] == 'O' and b_var[3]['text'] == 'O' and b_var[6]['text'] == 'O':
        for i in left_down:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='O WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[1]['text'] == 'O' and b_var[4]['text'] == 'O' and b_var[7]['text'] == 'O':
        for i in middle_down:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='O WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()
    elif b_var[2]['text'] == 'O' and b_var[5]['text'] == 'O' and b_var[8]['text'] == 'O':
        for i in right_down:
            b_var[i].configure(bg='cyan')
            breset = Button(root, text='O WON!', command=reset_board)
            breset.place(height=50, width=100, x=x_val, y=y_val)
            disable_buttons()


def reset_board():
    for i in range(9):
        b_var[i].configure(state=NORMAL, text='', bg='purple')
    

def disable_buttons():
    for i in range(9):
        b_var[i].configure(state=DISABLED)


def alternate_turn():
	if turn_x['bg'] == 'green':
		#print("It's X turn")
		turn_x.configure(bg='red')
		turn_o.configure(bg='green')
        
	else:
		#print("It's O turn")
		turn_x.configure(bg='green')
		turn_o.configure(bg='red')
        

def current_turn():
    if turn_x['bg'] == 'green':
        return 'X'
    else:
        return 'O'


def turn_color():
    if turn_x['bg'] == 'green':
        return 'yellow'
    else:
        return 'blue'


def set_value(i):
    b_var[i].configure(text=current_turn(), bg=turn_color(), state=DISABLED)
    alternate_turn()
    check_win()


# Tkinter window setup
root = Tk()
root.wm_title("Tic Tac Toe")
root.configure(bg='black')
root.geometry('450x500')
root.resizable(0,0)

# Field position
x_v = 50
y_v = 100
b1 = Button(root, bg='purple', text='', command=lambda:set_value(0))
b1.place(bordermode=OUTSIDE, height=100, width=100, x=x_v ,y=y_v)
b2 = Button(root, bg='purple', text='', command=lambda:set_value(1))
b2.place(height=100, width=100, x=x_v + 125, y=y_v)
b3 = Button(root, bg='purple', text='', command=lambda:set_value(2))
b3.place(height=100, width=100, x=x_v + 125*2, y=y_v)
b4 = Button(root, bg='purple', text='', command=lambda:set_value(3))
b4.place(height=100, width=100, x=x_v, y=y_v + 125)
b5 = Button(root, bg='purple', text='', command=lambda:set_value(4))
b5.place(height=100, width=100, x=x_v + 125, y=y_v + 125)
b6 = Button(root, bg='purple', text='', command=lambda:set_value(5))
b6.place(height=100, width=100, x=x_v + 125*2, y=y_v+125)
b7 = Button(root, bg='purple', text='', command=lambda:set_value(6))
b7.place(height=100, width=100, x=x_v, y=y_v + 125*2)
b8 = Button(root, bg='purple', text='', command=lambda:set_value(7))
b8.place(height=100, width=100, x=x_v + 125, y=y_v + 125*2)
b9 = Button(root, bg='purple', text='', command=lambda:set_value(8))
b9.place(height=100, width=100, x=x_v + 125*2, y=y_v + 125*2)

# Turn labels
x_val = 175
y_val = 25
turn_x = Label(text='X', bg='green')
turn_x.place(height=50, width=100, x=50, y=25)
turn_o = Label(text='O', bg='red')
turn_o.place(height=50, width=100, x=300, y=25)
breset = Button(root, text='RESET', command=reset_board)
breset.place(height=50, width=100, x=x_val, y=y_val)

# Button names
b_var = [b1, b2, b3, b4, b5, b6, b7, b8, b9]


root.mainloop()
