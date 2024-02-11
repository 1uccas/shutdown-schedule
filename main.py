import tkinter as tkr
import customtkinter as ct

windows = tkr.Tk() 
windows.geometry("400x400")
windows.title("Shutdown Schedule")
windows.configure(bg="black")


entry = ct.CTkEntry(master=windows, placeholder_text="Enter your time")
entry.place(relx=0.5, rely=0.5, anchor=tkr.CENTER)
state = entry.cget("state")

button = ct.CTkButton(master=windows, corner_radius=10, text="Click")
button.place(relx=0.5, rely=0.6, anchor=tkr.CENTER)

windows.mainloop()