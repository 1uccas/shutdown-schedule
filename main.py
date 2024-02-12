import tkinter as tkr
import customtkinter as ct
import os

class Shutdown:
    def __init__(self):
        self.On_windows()

    def On_windows(self):
        self.windows = tkr.Tk() 
        self.windows.geometry("500x500")
        self.windows.title("Shutdown Schedule")
        self.windows.configure(bg="black")
        
        #Fonts
        self.Title = ct.CTkFont(family="Consolas", size=35)
        self.BoxText = ct.CTkFont(family="Consolas", size=12)
        
        self.tabview = ct.CTkTabview(master=self.windows, width=400, height=400)
        self.tabview.place(relx=0.5, rely=0.5, anchor=tkr.CENTER)
        self.tabview.add("On")
        self.tabview.add("Off")
        self.tabview.tab("On").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Off").grid_columnconfigure(0, weight=1)
        
        label = ct.CTkLabel(master=self.tabview.tab("On"), text="Shutdown in...")
        label.place(relx=0.5, rely=0.3, anchor="center")
        label.configure(font=self.Title)

        self.entry = ct.CTkEntry(master=self.tabview.tab("On"), placeholder_text="ex: 25min")
        self.entry.place(relx=0.5, rely=0.5, anchor=tkr.CENTER)
        self.entry.configure(font=self.BoxText)
        
        self.boxText = ct.CTkTextbox(self.tabview.tab("On"), width=400, height=100, corner_radius=15,
                                     border_width=1, border_color="black", text_color="lightgreen")
        
        self.boxText.place(relx=0.5, rely=0.8, anchor=tkr.CENTER)
        self.boxText.configure(font=self.BoxText)

        button = ct.CTkButton(master=self.tabview.tab("On"), corner_radius=10, text="Enter", command=self.capValue)
        button.place(relx=0.5, rely=0.6, anchor=tkr.CENTER)
        button.configure(font=self.BoxText)
        
        self.off_windows()
        
        self.windows.mainloop()
    
    def off_windows(self):
        buttonExit = ct.CTkButton(master=self.tabview.tab("Off"), corner_radius=10, text="Exit windows", command=self.exitWindows)
        buttonExit.place(relx=0.3, rely=0.5, anchor=tkr.CENTER)
        buttonExit.configure(font=self.BoxText)
        
        buttonTurnOff = ct.CTkButton(master=self.tabview.tab("Off"), corner_radius=10, fg_color="darkred", text="Turn Off Shutdown", command=self.TurnOff)
        buttonTurnOff.place(relx=0.7, rely=0.5, anchor=tkr.CENTER)
        buttonTurnOff.configure(font=self.BoxText)
        
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
            
        except ValueError as Error:
            self.boxText.insert("end", f"Encontramos um problema em seu código -> {Error}\n")
    
if __name__ == "__main__":
    shutdown = Shutdown()