from tkinter import *
import tkinter as tk
from tkinter import filedialog 
from cpu import CPU
import sys
sys.path.insert(0, './memory')
from memory import Memory 

# make instance of CPU
cpu = CPU()

def UploadFile(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    
    CPU.load_program(cpu, filename)

window = tk.Tk()
window.configure(background='#97ecf7')
window.title("Machine Simulator")

# setting layout of main window
window.grid_columnconfigure(2,weight=1)
window.grid_rowconfigure(3,weight=1)

# create register frame and place it
registersGPRFrame = tk.Frame(window, bg="#97ecf7")
registersGPRFrame.grid(column=0,row=0) 
registersGPRFrame.grid_columnconfigure(1, weight=1, minsize=50)
registersGPRFrame.grid_columnconfigure(4, weight=1, minsize=50)

# create labels for 4 general purpose registers (GPR 0 - GPR 3)
gpr0_btn = tk.Label(registersGPRFrame, text = "GPR 0", fg = "green",padx=5,pady=5,relief=tk.RAISED)
gpr0_btn.grid(row=0,column=0)
gpr0 = []
for i in range (1,17):
  gpr0.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr0[i-1], bg="#97ecf7").grid(row=0,column=i)
gpr0_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=0,column=17)

gpr1_btn = tk.Label(registersGPRFrame, text = "GPR 1", fg = "green",padx=5,pady=5,relief=tk.RAISED)
gpr1_btn.grid(row=1,column=0)
gpr1 = []
for i in range (1,17):
  gpr1.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr1[i-1], bg="#97ecf7").grid(row=1,column=i)
gpr1_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=1,column=17)

gpr2_btn = tk.Label(registersGPRFrame, text = "GPR 2", fg = "green",padx=5,pady=5,relief=tk.RAISED)
gpr2_btn.grid(row=2,column=0)
gpr2 = []
for i in range (1,17):
  gpr2.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr2[i-1], bg="#97ecf7").grid(row=2,column=i)
gpr2_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=2,column=17)

gpr3_btn = tk.Label(registersGPRFrame, text = "GPR 3", fg = "green",padx=5,pady=5,relief=tk.RAISED)
gpr3_btn.grid(row=3,column=0)
gpr3 = []
for i in range (1,17):
  gpr3.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr3[i-1], bg="#97ecf7").grid(row=3,column=i)
gpr3_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=3,column=17)

# create register frame and place it
indexFrame = tk.Frame(window, bg="#97ecf7")
indexFrame.grid(row=2,column=0)
indexFrame.grid_columnconfigure(1, weight=1, minsize=50)
indexFrame.grid_columnconfigure(4, weight=1, minsize=50)

#labels for 3 Index Registers IXR 1 - IXR 3
ixr1_btn = tk.Label(indexFrame , text = "IXR 1", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
ixr1_btn.grid(row=5,column=0)
ixr1 = []
for i in range (1,17):
  ixr1.append(IntVar())
  tk.Checkbutton(indexFrame, text='', variable=ixr1[i-1], bg="#97ecf7").grid(row=5,column=i)
ixr1_LD = tk.Button(indexFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=5,column=17)

ixr2_btn = tk.Label(indexFrame , text = "IXR 2", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
ixr2_btn.grid(row=6,column=0)
ixr2 = []
for i in range (1,17):
  ixr2.append(IntVar())
  tk.Checkbutton(indexFrame, text='', variable=ixr2[i-1], bg="#97ecf7").grid(row=6,column=i)
ixr2_LD = tk.Button(indexFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=6,column=17)

ixr3_btn = tk.Label(indexFrame , text = "IXR 3", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
ixr3_btn.grid(row=7,column=0)
ixr3 = []
for i in range (1,17):
  ixr3.append(IntVar())
  tk.Checkbutton(indexFrame, text='', variable=ixr3[i-1], bg="#97ecf7").grid(row=7,column=i)
ixr3_LD = tk.Button(indexFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=7,column=17)

# creating frame for PC, MAR, MBR, IR, MFR, Privileged 
otherFrame = tk.Frame(window, bg="#97ecf7")
otherFrame.grid(row=0,column=2)
otherFrame.grid_columnconfigure(4, weight=1, minsize=50)

# label for for PC, MAR, MBR, IR, MFR, Privileged
pc_btn = tk.Label(otherFrame, text = "PC", fg = "blue",width=6,relief=tk.RAISED,justify='right')
pc_btn.grid(row=1,column=22)
pc = [12]
for i in range (23,35):
  pc.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=pc[i-22], bg="#97ecf7").grid(row=1,column=i)
pc_LD= tk.Button(otherFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=1,column=35)

mar_btn = tk.Label(otherFrame, text = "MAR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
mar_btn.grid(row=2,column=22)
mar = [12]
for i in range (23,35):
  mar.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mar[i-22], bg="#97ecf7").grid(row=2,column=i)
mar_LD = tk.Button(otherFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=2,column=35)

mbr_btn = tk.Label(otherFrame, text = "MBR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
mbr_btn.grid(row=3,column=18)
mbr = [16]
for i in range (19,35):
  mbr.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mbr[i-18], bg="#97ecf7").grid(row=3,column=i)
mbr_LD = tk.Button(otherFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=3,column=35)

ir_btn = tk.Label(otherFrame, text = "IR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
ir_btn.grid(row=4,column=18)
ir = [16]
for i in range (19,35):
  ir.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=ir[i-18], bg="#97ecf7").grid(row=4,column=i)

mfr_btn = tk.Label(otherFrame, text = "MFR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
mfr_btn.grid(row=5,column=30)
mfr = [4]
for i in range (31,35):
  mfr.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mfr[i-30], bg="#97ecf7").grid(row=5,column=i)

privileged_btn = tk.Label(otherFrame, text = "Privileged", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
privileged_btn.grid(row=6,column=33)
priv_1 = tk.Checkbutton(otherFrame, text='', bg="#97ecf7").grid(row=6,column=34)

# creating frame for Store, St+, Load, and Init buttons 
buttonFrame = tk.Frame(window, bg="#97ecf7")
buttonFrame.grid(row=0,column=4)
buttonFrame.grid_columnconfigure(4, weight=7, minsize=100)

store_btn = tk.Button(buttonFrame, text = "Store", fg = "green",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7").grid(row=20,column=0)
store_plus_btn = tk.Button(buttonFrame, text = "Store+", fg = "green",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7").grid(row=20,column=1)
load_btn = tk.Button(buttonFrame, text = "Load", fg = "green",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7").grid(row=20,column=2)
init_btn = tk.Button(buttonFrame, text = "Init", fg = "red",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7", command=UploadFile).grid(row=20,column=3)

# TODO: add checkboxes for instruction 
# TODO: add button for "Run" which calls function CPU.run_program()
# TODO: add button for "Step" which calls function CPU.step_through()
# TODO: function for "LD" buttons

window.mainloop()

