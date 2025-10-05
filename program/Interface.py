from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import algorithm_file

# Global variables for files names.
variables = {
    "elecs_path": "",
    "model_path": ""
}

'''Display a file selector with some selecting criteria.'''
def seleccionar_csv(label_fitxer, clau):
    global file_name  # Declaring the variables as global.
    # Opening a dialogue to select files
    fitxer = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if fitxer:  # Updating label and variable, if user does not cancel.
        variables[clau] = fitxer  # Saving file name at global variable.
        ruta = variables[clau]
        name = ""
        aux = ""
        for i in range(len(ruta)):
            if ruta[i] == "/":
                aux = ""   
            else:
                aux += ruta[i]
        name = aux
        label_fitxer.config(text=name)

'''Process data from files selected by user.'''
def processar(label_text, clau_elecs, clau_model):
    nelements_str = entrada.get()
    nelements = int(nelements_str)
    if ( variables[clau_elecs] != "") and (variables[clau_model] != ""):
        ruta = variables[clau_model]
        name = ""
        aux = ""
        for i in range(len(ruta)):
            if ruta[i] == "/":
                aux = ""   
            else:
                aux += ruta[i]
        name = aux
        label_text.config(text="You can get your ETRS-89, UTM-31 N coordinate model file at original directory, its name will be 'new_'." + name + "'")
        algorithm_file.processar(variables[clau_elecs], variables[clau_model], nelements)
    else:
        label_text.config(text="You need to select all files.")

# Creating main window.
root = Tk()
root.title("Relative -> ETRS-89, UTM-31 N coordinates converter for geophisical models.")  # Window title
frm = ttk.Frame(root, padding=10)
frm.grid()

# Adding a centred Title.
ttk.Label(frm, text="Relative -> ETRS-89, UTM-31 N coordinates converter for geophisical models.", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=(0, 20))


# Electodes button.

# Adding a left booded label.
ttk.Label(frm, text="Insert the CSV document with model elements data: \n     Remember! This document must have:\n          First column (A): electrodes names: e1, e2, ..., e36, ..., en they must be in increasing or decreasing ordered.\n          Second column (B): X coordinate in ETRS-89, UTM-31 N of the electrode in the same row (column A). \n          Third column (C):  Y coordinate in ETRS-89, UTM-31 N of the electrode in the same row (column A). \n     IMPORTANT! There must be NO electrodes in the first row, it is interpreated as a header.", anchor=W).grid(column=0, row=1, sticky=W, columnspan=2, padx=(10, 10), pady=(30, 0))

# Label to show the selected file.
label_fitxer_elecs = ttk.Label(frm, text="You must select a file")
label_fitxer_elecs.grid(column=1, row=2, padx=(0, 20))

# Button to select CSV file.
ttk.Button(frm, text='Select .csv file', command=lambda: seleccionar_csv(label_fitxer_elecs, "elecs_path")).grid(column=0, row=2, sticky=EW, pady=(10, 10), padx=10)


# Models Button.

# Adding a left blooded label.
ttk.Label(frm, text="Insert the CSV document with model elemnts data: \n     Remember! This document must have:\n          First column (A): The distance between e1 elctrode and the model element of the row.\n          Second column (B): model elements elevation.\n          Third column (C): Resistivity of model's element.\n     IMPORTANT! There must be NO model's elements in the first row, it is interpreated as a header.", anchor=W).grid(column=0, row=3, sticky=W, columnspan=2, padx=(10, 0), pady=(30, 0))

# Label to show the selected document.
label_fitxer_model = ttk.Label(frm, text="You must select a file")
label_fitxer_model.grid(column=1, row=4, padx=(0, 20))

# Button so select a CSV file.
ttk.Button(frm, text='Select .csv file', command=lambda: seleccionar_csv(label_fitxer_model, "model_path")).grid(column=0, row=4, sticky=EW, pady=(10, 10), padx=10)

# How many elements?
ttk.Label(frm, text="How many elements does the model have?", anchor=W).grid(column=0, row=5, sticky=W, columnspan=2, padx=(10, 0), pady=(30, 0))
entrada = Entry(frm)
entrada.grid(column=0, row=6, columnspan=2, sticky=EW, pady=5, padx=10)  # Afegir espai vertical



# Submit button
label_text = ttk.Label(frm, text = "")
label_text.grid(column=0, row=8, columnspan=2, padx=(10, 0), pady=(10, 0))

ttk.Button(frm, text='Submit', command=lambda: processar(label_text, "elecs_path", "model_path")).grid(column=0, row=7, columnspan=2, sticky=EW, pady=(40, 0), padx=10)


# Quit button

# Quit button's frame
frame_sortir = ttk.Frame(root)
frame_sortir.grid(column=0, row=1, sticky=SE, padx=10, pady=10)

# Quit button at right down corner.
ttk.Button(frame_sortir, text="Quit", command=root.destroy).pack(side=BOTTOM)


# Starting main loop
root.mainloop()