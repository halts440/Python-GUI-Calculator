# Tkinter Project No. 1
# Date: 7/20/2019

# importing libraries
import tkinter as tk
import tkinter.font as Font


# creating main screen or main window
window = tk.Tk()
window.title('Calculator')
window.geometry("334x360")
window.iconbitmap(r'chalkboard_icon-icons.com_54408.ico')


# creating label where all results will be show
main_label = tk.Label(window, text='', height=2, bg='#ffcc80', width=43)
main_label.place(x=13, y=10)


# Adding new numbers and operators to label
def add_to_text(temp_button, temp_label):
    temp = temp_label.cget('text') + temp_button.cget('text')
    temp_label.config(text=temp)

# Getting resulting from expression
def convert_val(temp_label):
    temp_label.config(text=str( eval(temp_label.cget('text') ) ) )


# Fisrt set of buttons including
# button for numbers 1,2,3 and addition
btn2 = tk.Button(window, text='2', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn2, main_label) )
btn1 = tk.Button(window, text='1', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn1, main_label) )
btn3 = tk.Button(window, text='3', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn3, main_label))
btn_add = tk.Button(window, text='+', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn_add, main_label))


# Second set of buttons including
# button for numbers 4,5,6 and subtraction
btn4 = tk.Button(window, text='4', width=9, height=2,  bg='#ffcc80',  command=lambda:add_to_text(btn4, main_label))
btn5 = tk.Button(window, text='5', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn5, main_label))
btn6 = tk.Button(window, text='6', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn6, main_label))
btn_sub = tk.Button(window, text='-', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn_sub, main_label))


# Third set of buttons including
# buttons for numbers 7,8,9 and multiplication
btn7 = tk.Button(window, text='7', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn7, main_label))
btn8 = tk.Button(window, text='8', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn8, main_label))
btn9 = tk.Button(window, text='9', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn9, main_label))
btn_multiply = tk.Button(window, text='*', width=9, bg='#ffcc80',  height=2, command=lambda:add_to_text(btn_multiply, main_label))


# Fourth set of buttons including
# buttons for number 0, point , division and result(i.e =)
btn0 = tk.Button(window, text='0', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn0, main_label))
btn_p = tk.Button(window, text='.', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn_p, main_label))
btn_res = tk.Button(window, text='=', width=9, height=2, bg='#ffcc80',  command=lambda:convert_val(main_label))
btn_div = tk.Button(window, text='/', width=9, height=2, bg='#ffcc80',  command=lambda:add_to_text(btn_div, main_label))


# clear button to remove contents of main label
clr_btn = tk.Button(window, text='Clear', width=9, height=2, bg='#ffcc80',  command= lambda: main_label.config(text='') )


# placement of first set of buttons
btn1.place(x=12, y=60)
btn2.place(x=90, y=60)
btn3.place(x=168, y=60)
btn_add.place(x=247, y=60)


# placement of second set of buttons
btn4.place(x=12,y=120)
btn5.place(x=90, y=120)
btn6.place(x=168, y=120)
btn_sub.place(x=247, y=120)


# placement of third set of buttons
btn7.place(x=12, y=180)
btn8.place(x=90, y=180)
btn9.place(x=168, y=180)
btn_multiply.place(x=247, y=180)


# placement of fourth set of buttons
btn0.place(x=12, y=240)
btn_p.place(x=90, y=240)
btn_res.place(x=168, y=240)
btn_div.place(x=247, y=240)


# placement of clear button
clr_btn.place(x=12, y=300)


window.mainloop()