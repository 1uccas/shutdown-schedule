import tkinter as tkr
import customtkinter as ct
import os
from PIL import Image

class Shutdown:
    def __init__(self):
        self.On_windows()
        
    def startTimer_15(self):
        #start stopwatch in C
        self.path_15minutes = 'timer\\15\\timer.exe'
        self.startTimer = os.startfile(self.path_15minutes, 'open')
        
    def startTimer_30(self):
        #start stopwatch in C
        self.path_30minutes = 'timer\\30\\timer.exe'
        self.startTimer = os.startfile(self.path_30minutes, 'open')
        
    def optionRadio(self):
        selected_value = self.variableRadio.get()
        self.entry.delete(0, tkr.END)  
        self.entry.insert(0, selected_value)
        
    def cleanOptions(self):
        self.variableRadio.set("")
        self.entry.delete(0, "end")

    def On_windows(self):
        self.windows = tkr.Tk() 
        self.windows.geometry("500x500")
        self.windows.title("Shutdown Schedule")
        self.windows.configure(bg="black")
        
        #image
        self.time = ct.CTkImage(dark_image=Image.open("img/time.png"), size=(50,50))
        self.clock = ct.CTkImage(dark_image=Image.open("img/clock.png"), size=(50,50))
        self.clock_2 = ct.CTkImage(dark_image=Image.open("img/clock_2.png"), size=(50,50))
        self.watch = ct.CTkImage(dark_image=Image.open("img/watch.png"), size=(50,50))
        self.calendar = ct.CTkImage(dark_image=Image.open("img/calendar.png"), size=(50,50))
        
        #Fonts
        self.Title = ct.CTkFont(family="Consolas", size=35)
        self.BoxText = ct.CTkFont(family="Consolas", size=12)
        
        #TabView
        self.tabview = ct.CTkTabview(master=self.windows, width=400, height=400)
        self.tabview.place(relx=0.5, rely=0.5, anchor=tkr.CENTER)
        self.tabview.add("On")
        self.tabview.add("Off")
        self.tabview.tab("On").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Off").grid_columnconfigure(0, weight=1)
        
        #LabelImages
        labeltime = ct.CTkLabel(master=self.tabview.tab("On"), text="", image=self.time)
        labeltime.place(relx=0.9, rely=0.1, anchor="center")
        
        labelClock = ct.CTkLabel(master=self.tabview.tab("On"), text="", image=self.clock)
        labelClock.place(relx=0.7, rely=0.1, anchor="center")
        
        labelClock_2 = ct.CTkLabel(master=self.tabview.tab("On"), text="", image=self.clock_2)
        labelClock_2.place(relx=0.5, rely=0.1, anchor="center")
        
        labelWatch = ct.CTkLabel(master=self.tabview.tab("On"), text="", image=self.watch)
        labelWatch.place(relx=0.3, rely=0.1, anchor="center")
        
        labelCalendar = ct.CTkLabel(master=self.tabview.tab("On"), text="", image=self.calendar)
        labelCalendar.place(relx=0.1, rely=0.1, anchor="center")
        
        #Principal Label
        label = ct.CTkLabel(master=self.tabview.tab("On"), text="Switch off time:")
        label.place(relx=0.5, rely=0.3, anchor="center")
        label.configure(font=self.Title)
        
        #Radio
        self.variableRadio = ct.StringVar()
        
        radio_15 = ct.CTkRadioButton(master=self.tabview.tab("On"), text="15 minutes", variable=self.variableRadio,value=15, command=self.optionRadio)
        radio_15.place(relx=0.2, rely=0.4, anchor="center")
        radio_15.configure(font=self.BoxText)
        
        radio_30 = ct.CTkRadioButton(master=self.tabview.tab("On"), text="30 minutes", variable=self.variableRadio,value=30, command=self.optionRadio)
        radio_30.place(relx=0.5, rely=0.4, anchor="center")
        radio_30.configure(font=self.BoxText)
        
        radio_60 = ct.CTkRadioButton(master=self.tabview.tab("On"), text="60 minutes", variable=self.variableRadio,value=60, command=self.optionRadio)
        radio_60.place(relx=0.8, rely=0.4, anchor="center")
        radio_60.configure(font=self.BoxText)
        
        #Entry
        self.entry = ct.CTkEntry(master=self.tabview.tab("On"), placeholder_text="ex: 25min")
        self.entry.place(relx=0.5, rely=0.5, anchor=tkr.CENTER)
        self.entry.configure(font=self.BoxText)
        
        
        #TextBox
        self.boxText = ct.CTkTextbox(self.tabview.tab("On"), width=400, height=100, corner_radius=15,
                                     border_width=1, border_color="black", text_color="lightgreen")
        
        self.boxText.place(relx=0.5, rely=0.8, anchor=tkr.CENTER)
        self.boxText.configure(font=self.BoxText)
        
        #Button
        buttonEnter = ct.CTkButton(master=self.tabview.tab("On"), corner_radius=10, text="Enter", command=self.capValue)
        buttonEnter.place(relx=0.3, rely=0.6, anchor=tkr.CENTER)
        buttonEnter.configure(font=self.BoxText)
        
        buttonClean = ct.CTkButton(master=self.tabview.tab("On"), fg_color="darkred", corner_radius=10, text="Clean", command=self.cleanOptions)
        buttonClean.place(relx=0.7, rely=0.6, anchor=tkr.CENTER)
        buttonClean.configure(font=self.BoxText)
        
        self.off_windows()
        
        self.windows.mainloop()
    
    def off_windows(self):
        #Buttons off_windows
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
        self.boxText.delete("0.0", tkr.END)
        self.boxText.insert("end", f"Finish Shutdown\n")

    def capValue(self):
        try:
            e_text=int(self.entry.get())
            valueConvert = int(e_text * 60)
            os.system(f"shutdown -s -t {valueConvert}")
            
            if(e_text == 15):
                self.startTimer_15()
            elif(e_text == 30):
                self.startTimer_30()
            elif(e_text == 60):
                self.startTimer_60()
           
            self.boxText.delete("0.0", tkr.END)
            self.boxText.insert("0.0", f"Your windows will shutdown in ~ {e_text}:00 min\n")
            
        except ValueError as Error:
            self.boxText.delete("0.0", tkr.END)
            self.boxText.insert("end", f"Error ~ {Error}\n")
    
if __name__ == "__main__":
    shutdown = Shutdown()