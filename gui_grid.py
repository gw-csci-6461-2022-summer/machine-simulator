from tkinter import *
import tkinter as tk

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
gpr0 = [16]
for i in range (1,17):
  gpr0.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr0[i-1]).grid(row=0,column=i)
gpr0_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=5,pady=5,relief=tk.RAISED).grid(row=0,column=17)

btn2 = tk.Label(registersGPRFrame, text = "GPR 1", fg = "green",padx=5,pady=5,relief=tk.RAISED)
btn2.grid(row=1,column=0)
gpr1 = [16]
for i in range (1,17):
  gpr1.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr1[i-1]).grid(row=1,column=i)
gpr1_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=5,pady=5,relief=tk.RAISED).grid(row=1,column=17)

btn3 = tk.Label(registersGPRFrame, text = "GPR 2", fg = "green",padx=5,pady=5,relief=tk.RAISED)
btn3.grid(row=2,column=0)
gpr2 = [16]
for i in range (1,17):
  gpr2.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr2[i-1]).grid(row=2,column=i)
gpr2_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=5,pady=5,relief=tk.RAISED).grid(row=2,column=17)

btn4 = tk.Label(registersGPRFrame, text = "GPR 3", fg = "green",padx=5,pady=5,relief=tk.RAISED)
btn4.grid(row=3,column=0)
gpr3 = [16]
for i in range (1,17):
  gpr3.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr3[i-1]).grid(row=3,column=i)
gpr3_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=5,pady=5,relief=tk.RAISED).grid(row=3,column=17)


# creating the register frame and place it
indexFrame = tk.Frame(window)
indexFrame.grid(row=2,column=0)
indexFrame.grid_columnconfigure(1, weight=1, minsize=50)
indexFrame.grid_columnconfigure(4, weight=1, minsize=50)

#labels for  3 Index Registers 1-3
btn5 = tk.Label(indexFrame , text = "IXR 1", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn5.grid(row=5,column=0)
ixr1 = [16]
for i in range (1,17):
  ixr1.append(IntVar())
  tk.Checkbutton(indexFrame, text='', variable=ixr1[i-1]).grid(row=5,column=i)
ixr1_LD = tk.Button(indexFrame, text = "LD", fg = "green",padx=5,pady=5,relief=tk.RAISED).grid(row=5,column=17)

btn6 = tk.Label(indexFrame , text = "IXR 2", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn6.grid(row=6,column=0)
ixr2 = [16]
for i in range (1,17):
  ixr2.append(IntVar())
  tk.Checkbutton(indexFrame, text='', variable=ixr2[i-1]).grid(row=6,column=i)
ixr2_LD = tk.Button(indexFrame, text = "LD", fg = "green",padx=5,pady=5,relief=tk.RAISED).grid(row=6,column=17)

btn7 = tk.Label(indexFrame , text = "IXR 3", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn7.grid(row=7,column=0)
ixr3 = [16]
for i in range (1,17):
  ixr3.append(IntVar())
  tk.Checkbutton(indexFrame, text='', variable=ixr3[i-1]).grid(row=7,column=i)
ixr3_LD = tk.Button(indexFrame, text = "LD", fg = "green",padx=5,pady=5,relief=tk.RAISED).grid(row=7,column=17)

# creating frame for PC, MAR, MBR, IR, MFR, Privileged 
otherFrame = tk.Frame(window)
otherFrame.grid(row=0,column=2)
otherFrame.grid_columnconfigure(4, weight=1, minsize=50)

# labelfor for PC, MAR, MBR, IR, MFR, Privileged
btn8 = tk.Label(otherFrame, text = "PC", fg = "blue",width=6,relief=tk.RAISED,justify='right')
btn8.grid(row=1,column=22)
pc = [12]
for i in range (23,35):
  pc.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=pc[i-22]).grid(row=1,column=i)
pc_LD= tk.Button(otherFrame, text = "LD", fg = "green",padx=5,pady=5,relief=tk.RAISED).grid(row=1,column=35)

btn9 = tk.Label(otherFrame, text = "MAR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn9.grid(row=2,column=22)
mar = [12]
for i in range (23,35):
  mar.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mar[i-22]).grid(row=2,column=i)
mar_LD = tk.Button(otherFrame, text = "LD", fg = "green",padx=5,pady=5,relief=tk.RAISED).grid(row=2,column=35)

btn10 = tk.Label(otherFrame, text = "MBR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn10.grid(row=3,column=18)
mbr = [16]
for i in range (19,35):
  mbr.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mbr[i-18]).grid(row=3,column=i)
mbr_LD = tk.Button(otherFrame, text = "LD", fg = "green",padx=5,pady=5,relief=tk.RAISED).grid(row=3,column=35)

btn11= tk.Label(otherFrame, text = "IR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn11.grid(row=4,column=18)
ir = [16]
for i in range (19,35):
  ir.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=ir[i-18]).grid(row=4,column=i)

btn12= tk.Label(otherFrame, text = "MFR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn12.grid(row=5,column=30)
mfr = [4]
for i in range (31,35):
  mfr.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mfr[i-30]).grid(row=5,column=i)

btn13= tk.Label(otherFrame, text = "Privileged", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
btn13.grid(row=6,column=33)
priv_1 = tk.Checkbutton(otherFrame, text='').grid(row=6,column=34)

window.mainloop()


