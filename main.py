import tkinter as tkr
import customtkinter as ct
import os

windows = tkr.Tk() 
windows.geometry("400x400")
windows.title("Shutdown Schedule")
windows.configure(bg="black")

def capValue():
    try:
        e_text=int(entry.get())
        os.system(f"shutdown -s -t {e_text}")
        print(e_text)
    except ValueError as Error:
        print(f"Encontramos um problema em seu codigo -> {Error}")
    
label = ct.CTkLabel(master=windows, text="Shutdown in...")
label.place(relx=0.5, rely=0.3, anchor="center")
new_font = ct.CTkFont(family="Arial", size=35)
label.configure(font=new_font)

entry = ct.CTkEntry(master=windows, placeholder_text="ex: 25min")
entry.place(relx=0.5, rely=0.5, anchor=tkr.CENTER)

button = ct.CTkButton(master=windows, corner_radius=10, text="Enter", command=capValue)
button.place(relx=0.5, rely=0.6, anchor=tkr.CENTER)


windows.mainloop()