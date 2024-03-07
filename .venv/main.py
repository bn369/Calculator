import tkinter
from tkinter import *

app = Tk()
app.title("Calculator")
app.geometry("570x600+100+200")
app.resizable(False, False)
app.configure(bg="#17161b")

equation = ""
prev_value = ""
symbols = [".", "/", "%", "*", "+", "-"]
starting_symbol = [".", "/", "%", "*", "+"]

def show(value):
    global equation, symbols, prev_value
    if len(equation) > 18:
        equation = "error! number too big"
    if value in starting_symbol and equation == "":
        equation = ""
    elif value in starting_symbol and equation =="-":
        equation = "-"
    elif value in symbols and prev_value in symbols:
        equation = equation[:-1]
        equation += value
        prev_value = value
        label_result.config(text=equation)
        print(value)
    else:
        equation += value
        label_result.config(text=equation)
    prev_value = value
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
            equation = str(result)
            if len(equation) > 18:
                equation = "error! too big number"
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

label_result = Label(app, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

Button(app, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10, y=100)
Button(app, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=150, y=100)
Button(app, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=290, y=100)
Button(app, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=430, y=100)

Button(app, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=200)
Button(app, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=200)
Button(app, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=200)
Button(app, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=430, y=200)

Button(app, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=300)
Button(app, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=300)
Button(app, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=300)
Button(app, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=430, y=300)

Button(app, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=400)
Button(app, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=400)
Button(app, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=400)
Button(app, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=500)

Button(app, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=500)
Button(app, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate()).place(x=430, y=400)

app.mainloop()