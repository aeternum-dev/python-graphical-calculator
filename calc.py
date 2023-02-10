import tkinter

def main():
    root = tkinter.Tk()
    root.title("Simple Calculator")

    large_font = ('Arial', 25)
    small_font = ('Arial', 15)

    def basic4(n1,op,n2):# plus mod and fdiv
        if op == "+":
            a = str(int(n1) + int(n2))
            return a
        elif op == "-":
            b = str(int(n1) - int(n2))
            return b
        elif op == "x":
            return str(int(n1)*int(n2))
        elif op == "÷" and n2 != "0":
            return str(float(n1)/float(n2))
        elif op == "÷" and n2 == "0":
            return "cannot divide by 0"
        elif op == "m":
            return str(int(n1) % int(n2))
        elif op == "f":
            return str(int(n1) // int(n2))

    def button_click(char):   #elöszőr kettő taggal rockie
        if char == "clr":
            e.delete(0, "end")

        elif char == "=":
            data = e.get()
            for i, x in enumerate(data):
                if x.isdigit() == False:
                    l_index = i
                    op = x
            n1 = "".join([x for i, x in enumerate(data) if i < l_index])
            n2 = "".join([x for i, x in enumerate(data) if i > l_index])
            solution = (basic4(n1,op,n2))
            e.delete(0, "end")
            e.insert(10, str(solution))

        else:
            e.insert(10, char)


    frame = tkinter.Frame(root)
    frame.pack()

    e = tkinter.Entry(frame, width=12, readonlybackground="white", borderwidth=3, font=large_font)
    e.grid(row=0, column=0, columnspan=4, padx=24, pady=10)
    button_1 = tkinter.Button(frame, text="1",font=large_font, command=lambda: button_click(1))
    button_2 = tkinter.Button(frame, text="2",font=large_font, command=lambda: button_click(2))
    button_3 = tkinter.Button(frame, text="3",font=large_font, command=lambda: button_click(3))
    button_4 = tkinter.Button(frame, text="4",font=large_font, command=lambda: button_click(4))
    button_5 = tkinter.Button(frame, text="5",font=large_font, command=lambda: button_click(5))
    button_6 = tkinter.Button(frame, text="6",font=large_font, command=lambda: button_click(6))
    button_7 = tkinter.Button(frame, text="7",font=large_font,  command=lambda: button_click(7))
    button_8 = tkinter.Button(frame, text="8",font=large_font,  command=lambda: button_click(8))
    button_9 = tkinter.Button(frame, text="9",font=large_font,  command=lambda: button_click(9))
    button_0 = tkinter.Button(frame, text="0",font=large_font, command=lambda: button_click(0))

    button_plus = tkinter.Button(frame, text="+", font=large_font, command=lambda: button_click("+"))
    button_minus = tkinter.Button(frame, text="-", font=large_font, command=lambda: button_click("-"))
    button_mult = tkinter.Button(frame, text="x", font=large_font, command=lambda: button_click("x"))
    button_div = tkinter.Button(frame, text="÷", font=large_font, command=lambda: button_click("÷"))
    button_mod = tkinter.Button(frame, text="m", font=large_font, command=lambda: button_click("m")) #in basic4 for the time being
    button_fdiv = tkinter.Button(frame, text="f", font=large_font, command=lambda: button_click("f")) #in basic4 for the time being
    button_equal = tkinter.Button(frame, text="=", font=large_font, command=lambda: button_click("="))
    button_clear = tkinter.Button(frame, text="clr", font=large_font, command=lambda: button_click("clr"))


    button_7.grid(row=1, column=0, sticky="nesw")
    button_8.grid(row=1, column=1, sticky="nesw")
    button_9.grid(row=1, column=2, sticky="nesw")

    button_4.grid(row =2 , column =0, sticky="nesw")
    button_5.grid(row =2 , column =1, sticky="nesw")
    button_6.grid(row =2 , column =2, sticky="nesw")

    button_1.grid(row =3 , column =0, sticky="nesw")
    button_2.grid(row =3 , column =1, sticky="nesw")
    button_3.grid(row =3 , column =2, sticky="nesw")

    button_0.grid(row=4, column=0, sticky="nesw")
    button_mod.grid(row=4, column=1, sticky="nesw")
    button_fdiv.grid(row=4, column=2, sticky="nesw")
    button_plus.grid(row=1, column=3, sticky="nesw")
    button_minus.grid(row=2, column=3, sticky="nesw")
    button_mult.grid(row=3, column=3, sticky="nesw")
    button_div.grid(row=4, column=3, sticky="nesw")
    button_clear.grid(row=5, column=0, columnspan=2, sticky="nesw")
    button_equal.grid(row=5, column=2, columnspan=2, sticky="nesw")


    root.mainloop()
main()