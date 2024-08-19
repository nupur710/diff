import tkinter as tk
from tkinter import ttk


root= tk.Tk()
root.geometry("600x400")

m= tk.StringVar()
n= tk.StringVar()
src_string= ttk.Label(root, text="Source String: ")
src_string.pack(side="left", padx=(0, 10))
src_entry= ttk.Entry(root, width= 15, textvariable=m)
src_entry.pack(side="left")
src_entry.focus()

dest_string= ttk.Label(root, text="Destination String: ")
dest_string.pack(side="left")
dest_entry= ttk.Entry(root, width=15, textvariable=n)
dest_entry.pack(side="left")

run_btn= ttk.Button(root, text="Run")
run_btn.pack(side="left")
root.mainloop() 
