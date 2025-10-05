from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

'''This is a funcion that shows an error when something is wrong on the data provided. Show's some tips on what to do, and tells what to do next.'''
def show_error():
    root = Tk()
    root.title("Error")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Profile elements are out of the electrode range.", anchor=W).grid(column=0, row=0, sticky=EW, columnspan=2, padx=10, pady=(30, 0))
    ttk.Label(frm, text="Check if last electrode is correctly tagged as\ne'N + 1' where N means nº of model elements.", anchor=W).grid(column=0, row=1, sticky=EW, columnspan=2, padx=10, pady=(30, 0))
    ttk.Label(frm, text="Please restart the program and try again.", anchor=W).grid(column=0, row=2, sticky=EW, columnspan=2, padx=10, pady=30)
    root.mainloop()
