import tkinter as tkr
import customtkinter as ct
import os

class Shutdown:
    def __init__(self):
        self.windows()

    def windows(self):
        self.windows = tkr.Tk() 
        self.windows.geometry("500x500")
        self.windows.title("Shutdown Schedule")
        self.windows.configure(bg="black")
        
        label = ct.CTkLabel(master=self.windows, text="Shutdown in...")
        label.place(relx=0.5, rely=0.3, anchor="center")
        new_font = ct.CTkFont(family="Arial", size=35)
        label.configure(font=new_font)

        self.entry = ct.CTkEntry(master=self.windows, placeholder_text="ex: 25min")
        self.entry.place(relx=0.5, rely=0.5, anchor=tkr.CENTER)
        
        self.boxText = ct.CTkTextbox(self.windows, width=400, height=100)
        self.boxText.place(relx=0.5, rely=0.8, anchor=tkr.CENTER)

        button = ct.CTkButton(master=self.windows, corner_radius=10, text="Enter", command=self.capValue)
        button.place(relx=0.5, rely=0.6, anchor=tkr.CENTER)
        
        self.tabview = ct.CTkTabview(master=self.windows, width=150, height=50)
        self.tabview.place(relx=0.5, rely=0.1, anchor=tkr.CENTER)
        
        self.windows.mainloop()
        
    def exitWindows(self):
        exit()

    def TurnOff(self):
        os.system(f"shutdown -a")
        self.boxText.insert("end", f"Finish Shutdown\n")

    def capValue(self):
        try:
            e_text=int(self.entry.get())
            valueConvert = int(e_text * 60)
            #os.system(f"shutdown -s -t {valueConvert}")
            self.boxText.insert("0.0", f"Valor adicionado -> {e_text}\n")
            
            '''new_windows = ct.CTkToplevel()
            new_windows.geometry("400x400")
            new_windows.title("New Windows")
            
            buttonExit = ct.CTkButton(master=new_windows, corner_radius=10, text="Exit windows", command=self.exitWindows)
            buttonExit.place(relx=0.3, rely=0.5, anchor=tkr.CENTER)
            
            buttonTurnOff = ct.CTkButton(master=new_windows, corner_radius=10, fg_color="darkred", text="Turn Off Shutdown", command=self.TurnOff)
            buttonTurnOff.place(relx=0.7, rely=0.5, anchor=tkr.CENTER)'''
            
        except ValueError as Error:
            self.boxText.insert("end", f"Encontramos um problema em seu código -> {Error}\n")
    
if __name__ == "__main__":
    shutdown = Shutdown()