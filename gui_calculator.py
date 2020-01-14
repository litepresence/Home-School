"""
A simple GUI calculator
"""
import tkinter as tk
import numexpr

# Create window and set title
ROOT = tk.Tk()
ROOT.title("Calculator")


def calculate():
    """
    calculate tkinter entry
    """
    # get the entry
    cal_this = ENTER.get()
    # if entry is valid
    try:
        # evaluate entered equation
        number = numexpr.evaluate(cal_this)
        # clear the entry box
        ENTER.delete(0, 100)
        # write the answer to the entry box
        ENTER.insert(0, str(number))
    # else:
    except KeyError:
        # clear the entry box
        ENTER.delete(0, 100)
        # write `error` to the entry box
        ENTER.insert(0, "ERROR")

# create entry box and pack
ENTER = tk.Entry(ROOT, bg="green", relief=tk.RIDGE, borderwidth=20, width=48)
ENTER.pack()

# create calculate button and pack
B = tk.Button(
    ROOT,
    text="Calculate",
    command=calculate,
    width=50,
    bg="green",
    activebackground="red",
)
B.pack()

# tkinter main loop
tk.mainloop()
