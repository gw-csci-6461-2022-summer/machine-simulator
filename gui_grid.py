import tkinter as tk
import tkinter

window = tk.Tk()
window.configure(background='aliceblue')
window.title("Machine Simulator")

# setting layout of main window
window.grid_columnconfigure(2,weight=1)
window.grid_rowconfigure(3,weight=1)

# creating the register frame and place it
registersGPRFrame = tk.Frame(window)
registersGPRFrame.grid(column=0,row=0) 
registersGPRFrame.grid_columnconfigure(1, weight=1, minsize=50)
registersGPRFrame.grid_columnconfigure(4, weight=1, minsize=50)

# creating labels for 4 general purpose registers 
btn1 = tk.Label(registersGPRFrame, text = "GPR 0", fg = "green",padx=5,pady=5,relief=tk.RAISED)
btn1.grid(row=0,column=0)
for i in range(1,17):
   tk.Button(registersGPRFrame, text= "Bit" +str(i)).grid(row=0,column=i)
btn2 = tk.Label(registersGPRFrame, text = "GPR 1", fg = "green",padx=5,pady=5,relief=tk.RAISED)
btn2.grid(row=1,column=0)
for i in range(1,17):
   tk.Button(registersGPRFrame, text= "Bit" +str(i)).grid(row=1,column=i)
btn3 = tk.Label(registersGPRFrame, text = "GPR 2", fg = "green",padx=5,pady=5,relief=tk.RAISED)
btn3.grid(row=2,column=0)
for i in range(1,17):
   tk.Button(registersGPRFrame, text= "Bit" +str(i)).grid(row=2,column=i)
btn4 = tk.Label(registersGPRFrame, text = "GPR 3", fg = "green",padx=5,pady=5,relief=tk.RAISED)
btn4.grid(row=3,column=0)
for i in range(1,17):
   tk.Button(registersGPRFrame, text= "Bit" +str(i)).grid(row=3,column=i)


# creating the register frame and place it
indexFrame = tk.Frame(window)
indexFrame.grid(row=2,column=0)
indexFrame.grid_columnconfigure(1, weight=1, minsize=50)
indexFrame.grid_columnconfigure(4, weight=1, minsize=50)

#labels for  3 Index Registers 1-3
btn5 = tk.Label(indexFrame , text = "IXR 1", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn5.grid(row=5,column=0)
for i in range(1,17):
   tk.Button(indexFrame, text= "Bit" +str(i)).grid(row=5,column=i)
btn6 = tk.Label(indexFrame , text = "IXR 2", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn6.grid(row=6,column=0)
for i in range(1,17):
   tk.Button(indexFrame, text= "Bit" +str(i)).grid(row=6,column=i)
btn7 = tk.Label(indexFrame , text = "IXR 3", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn7.grid(row=7,column=0)
for i in range(1,17):
   tk.Button(indexFrame, text= "Bit" +str(i)).grid(row=7,column=i)

# creating frame for PC, MAR, MBR, IR, MFR, Privileged 
otherFrame = tk.Frame(window)
otherFrame.grid(row=0,column=2)
otherFrame.grid_columnconfigure(4, weight=1, minsize=50)

# labelfor for PC, MAR, MBR, IR, MFR, Privileged
btn8 = tk.Label(otherFrame, text = "PC", fg = "blue",width=6,relief=tk.RAISED,justify='right')
btn8.grid(row=0,column=25)
btn9 = tk.Label(otherFrame, text = "MAR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn9.grid(row=1,column=25)
btn10 = tk.Label(otherFrame, text = "MBR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn10.grid(row=2,column=25)
btn11= tk.Label(otherFrame, text = "IR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn11.grid(row=3,column=25)
btn12= tk.Label(otherFrame, text = "MFR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn12.grid(row=4,column=25)
btn13= tk.Label(otherFrame, text = "Privileged", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn13.grid(row=5,column=25)

window.mainloop()


