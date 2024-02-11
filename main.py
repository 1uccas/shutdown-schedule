import tkinter as tkr
import customtkinter as ct

windows = tkr.Tk() 
windows.geometry("400x400")
windows.title("Shutdown Schedule")
windows.configure(bg="black")

def capValue():
    e_text=entry.get()
    print(e_text)

entry = ct.CTkEntry(master=windows, placeholder_text="Enter your time")
entry.place(relx=0.5, rely=0.5, anchor=tkr.CENTER)

button = ct.CTkButton(master=windows, corner_radius=10, text="Click", command=capValue)
button.place(relx=0.5, rely=0.6, anchor=tkr.CENTER)


windows.mainloop()