from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master=master
        master.title("Calculator")   
        master.config(background="#babbbc")

        self.Display=Text(master, state="disabled", width=60, height=5, background="#6e7072", foreground="white", highlightbackground="black", highlightthickness=0)
        self.Display.grid(row=0, column=0, columnspan=5, padx=8, pady=8)
        self.Display.configure(state="normal")

        self.equation=""

        self.num1=Button(master, text="1",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("1"), activeforeground="red")# highlightbackground="red")
        self.num1.grid(row=1, column=0)
        self.num2=Button(master, text="2",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("2"), activeforeground="red")
        self.num2.grid(row=1, column=1)
        self.num3=Button(master, text="3",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("3"), activeforeground="red")
        self.num3.grid(row=1, column=2)
        self.num4=Button(master, text="4",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("4"), activeforeground="red")
        self.num4.grid(row=2, column=0)
        self.num5=Button(master, text="5",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("5"), activeforeground="red")
        self.num5.grid(row=2, column=1)
        self.num6=Button(master, text="6",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("6"), activeforeground="red")
        self.num6.grid(row=2, column=2)
        self.num7=Button(master, text="7",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("7"), activeforeground="red")
        self.num7.grid(row=3, column=0)
        self.num8=Button(master, text="8",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("8"), activeforeground="red")
        self.num8.grid(row=3, column=1)
        self.num9=Button(master, text="9",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("9"), activeforeground="red")
        self.num9.grid(row=3, column=2)
        self.num0=Button(master, text="C",padx=45, pady=15, font=("Arial",17), width=2,command = lambda: DisplayText("C"), activeforeground="red")
        self.num0.grid(row=4, column=0)
        self.num0=Button(master, text="0",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("0"), activeforeground="red")
        self.num0.grid(row=4, column=1)
        self.Equal=Button(master, text="=",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("="), activeforeground="red")
        self.Equal.grid(row=4, column=2)
        self.Add=Button(master, text="+",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("+"), activeforeground="red")
        self.Add.grid(row=1, column=4)
        self.Sub=Button(master, text="-",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("-"), activeforeground="red")
        self.Sub.grid(row=2, column=4)
        self.Mult=Button(master, text="*",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("*"), activeforeground="red")
        self.Mult.grid(row=3, column=4)
        self.Div=Button(master, text="/",padx=45, pady=15, font=("Arial",17), width=2, command = lambda: DisplayText("/"), activeforeground="red")
        self.Div.grid(row=4, column=4)

        def DisplayText(text, newline=False):
            if(text=="C"):
                ClearDisplay()
            elif(text=="="):
                self.Display.configure(state="normal")
                result=eval(self.equation)
                ClearDisplay()
                self.Display.insert(END,result)
                self.equation+=str(result)
                self.Display.configure(state="disabled")
                
            else:
                self.Display.configure(state="normal")
                self.Display.insert(END,text)
                self.equation+=str(text)
                self.Display.configure(state="disabled")

        def ClearDisplay():
            self.equation=""
            self.Display.configure(state="normal")
            self.Display.delete('1.0',END)

                
        
        
        


root=Tk()
root.resizable(0,0)
calc=Calculator(root)
root.mainloop()
