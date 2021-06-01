import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *


def openFile():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txtEdit.delete(1.0, tk.END)
    with open(filepath, "r") as inputFile:
        text = inputFile.read()
        txtEdit.insert(tk.END, text)
    window.title(f"MY PERSONAL EDITOR - {filepath}")


def saveFile():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as outputFile:
        text = txtEdit.get(1.0, tk.END)
        outputFile.write(text)
    window.title(f"MY PERSONAL EDITOR - {filepath}")


window = tk.Tk()
window.title("MY PERSONAL EDITOR")
window.rowconfigure(0, minsize=800, weight=1, )
window.columnconfigure(1, minsize=800, weight=1)


txtEdit = tk.Text(window, font=("Times New Roman", 18),
                  selectbackground="light cyan", selectforeground="black")


frmButtons = tk.Frame(window, relief=tk.RAISED, bd=2)
btnOpen = tk.Button(frmButtons, text="Open", command=openFile)
btnSave = tk.Button(frmButtons, text="Save As", command=saveFile)

btnOpen.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
btnSave.grid(row=1, column=0, sticky="ew", padx=10)

frmButtons.grid(row=0, column=0, sticky="ns")
txtEdit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
