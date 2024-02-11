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
        valueConvert = int(e_text * 60)
        os.system(f"shutdown -s -t {valueConvert}")
        print(e_text)
        new_windows = ct.CTkToplevel()
        new_windows.geometry("400x400")
        new_windows.title("New Windows")
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