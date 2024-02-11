import tkinter as tkr
import customtkinter as ct

windows = tkr.Tk() 
windows.geometry("400x400")
windows.title("Shutdown Schedule")
windows.configure(bg="black")

button = ct.CTkButton(master=windows, corner_radius=10, text="Click")
button.place(relx=0.5, rely=0.5, anchor=tkr.CENTER)


windows.mainloop()