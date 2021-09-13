from tkinter import *
from functools import *

w = 500
h = 400

sign = 123
a = 0
b = 0


def toscreen(root):
    root.title("Calculator V2")
    root.resizable(False, False)
    Global: w = 500
    Global: h = 400
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    root.geometry("{}x{}+{}+{}".format(w, h, int(ws / 2 - w / 2), int(hs / 2)))


def handlerinput(number):
    entrydis.insert(END, number)
    # print("sdfsdf")


def handleract(act):
    print(act)
    global a
    global b
    global sign
    if act == "C":
        entrydis.delete(0, END)
        sign = -1
    elif act == "*":
        a = entrydis.get()
        entrydis.delete(0, END)
        sign = 2
    elif act == "/":
        a = entrydis.get()
        sign = 1
        entrydis.delete(0, END)
    elif act == "+":
        a = entrydis.get()
        entrydis.delete(0, END)
        sign = 3
    elif act == "-":
        a = entrydis.get()
        entrydis.delete(0, END)
        sign = 4
    elif act == "=":
        print(sign)
        if (sign != -1) and (entrydis.get() != ""):
            b = entrydis.get()
            entrydis.delete(0, END)
            print(sign, 'sign')
            a = float(a)
            b = float(b)
            if sign == 2:
                res = a * b
                if int(res) == res:
                    print(int(res))
                else:
                    print(res)
                entrydis.insert(END, a * b)
                #print(a,"=a ",b,"=b")
            elif sign == 1:
                entrydis.insert(END, a / b)
            elif sign == 3:
                entrydis.insert(END, a + b)
            elif sign == 4:
                entrydis.insert(END, a - b)
        else:
            print("Error")
            print(entrydis.get(), "disp", sign, "-znak")


root = Tk()
toscreen(root)
# standard window on screen

# Entry(root, font="Tahoma 30", justify="right").place(height=int(h / 4), width=w, x=0, y=0)
entrydis = Entry(root, font="Tahoma 30", justify="right")
entrydis.place(height=int(h / 4), width=w, x=0, y=0)
# entry on screen

bkey = 0
for y in range(3):
    for x in range(3):
        bkey += 1
        Button(root, text="{0}".format(bkey), font="TimesNewRoman 12",
               command=lambda btntext=bkey: handlerinput(btntext)).place(height=int(h / 4), width=int(w / 5),
                                                                         x=int(x * (w * 0.2)),
                                                                         y=int(h / 4) + int(y * h * 0.25))
        print(bkey)
# numbers on screen

datasymb = {1: "/", 2: "*", 3: "+", 4: "-", 5: "=", 6: "C"}
bkey = 0
for y in range(3):
    for x in range(2):
        bkey += 1
        Button(root, text="{0}".format(datasymb[bkey]), font="TimesNewRoman 12",
               command=lambda act=datasymb[bkey]: handleract(act)).place(height=int(h / 4),
                                                                         width=int(w / 5),
                                                                         x=int(w * 0.6) + int(
                                                                             x * w * 0.2),
                                                                         y=int(h * 0.25) + int(
                                                                             y * h * 0.25))
# math act on screen


root.mainloop()
