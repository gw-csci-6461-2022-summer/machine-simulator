import tkinter as tk
import sys
from dis import Instruction
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Separator 

#from cpu import CPU

sys.path.insert(0, './memory')
#from memory import Memory 

window = Tk()
window.configure(background='#97ecf7')
window.title("Machine Simulator")

# setting layout of main window
window.grid_columnconfigure(2,weight=1)
window.grid_rowconfigure(3,weight=1)

# bit array to be represented with the checkboxes
def bitToCheckbox(boxArray, bitArray):
  for i in range(len(boxArray)):
    if bitArray[i] == '1':
      boxArray[i].set(1)
    else:
      boxArray[i].set(0)

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
gpr0_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green", padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=0,column=17)
# gpr0_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green", command=lambda: bitToCheckbox(gpr0, "1111100000101010010001010"), padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=0,column=17)

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

def mar_pc_Load(arr):
  bits = ""
  for i in range(4, 16):
    if str(buttons[i].cget("bg")) == "blue":
      colorChange(i)
      bits += '1'
    else:
      bits += '0'
  print(bits)
  bitToCheckbox(arr, bits)
  
def mbrLoad():
  bits = ""
  for i in range(0, 16):
    if str(buttons[i].cget("bg")) == "blue":
      colorChange(i)
      bits += '1'
    else:
      bits += '0'
  print(bits)
  bitToCheckbox(mbr, bits)

# label for for PC, MAR, MBR, IR, MFR, Privileged
pc_btn = tk.Label(otherFrame, text = "PC", fg = "blue",width=6,relief=tk.RAISED,justify='right')
pc_btn.grid(row=1,column=22)
pc = []
for i in range (23,35):
  pc.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=pc[i-23], bg="#97ecf7").grid(row=1,column=i)
pc_LD= tk.Button(otherFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: mar_pc_Load(pc)).grid(row=1,column=35)

mar_btn = tk.Label(otherFrame, text = "MAR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
mar_btn.grid(row=2,column=22)
mar = []
for i in range (23,35):
  mar.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mar[i-23], bg="#97ecf7").grid(row=2,column=i)
mar_LD = tk.Button(otherFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: mar_pc_Load(mar)).grid(row=2,column=35)

mbr_btn = tk.Label(otherFrame, text = "MBR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
mbr_btn.grid(row=3,column=18)
mbr = []
for i in range (19,35):
  mbr.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mbr[i-19], bg="#97ecf7").grid(row=3,column=i)
mbr_LD = tk.Button(otherFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: mbrLoad()).grid(row=3,column=35)

ir_btn = tk.Label(otherFrame, text = "IR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
ir_btn.grid(row=4,column=18)
ir = []
for i in range (19,35):
  ir.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=ir[i-19], bg="#97ecf7").grid(row=4,column=i)

mfr_btn = tk.Label(otherFrame, text = "MFR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
mfr_btn.grid(row=5,column=30)
mfr = []
for i in range (31,35):
  mfr.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mfr[i-31], bg="#97ecf7").grid(row=5,column=i)

privileged_btn = tk.Label(otherFrame, text = "Privileged", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
privileged_btn.grid(row=6,column=33)
priv_1 = tk.Checkbutton(otherFrame, text='', bg="#97ecf7").grid(row=6,column=34)

# creating frame for Store, St+, Load, and Init buttons 
buttonFrame = tk.Frame(window, bg="#97ecf7")
buttonFrame.grid(row=4,column=4)
buttonFrame.grid_columnconfigure(4, weight=7, minsize=100)

store_btn = tk.Button(buttonFrame, text = "Store", fg = "green",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7").grid(row=20,column=0)
store_plus_btn = tk.Button(buttonFrame, text = "Store+", fg = "green",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7").grid(row=20,column=1)
load_btn = tk.Button(buttonFrame, text = "Load", fg = "green",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7").grid(row=20,column=2)
#init_btn = tk.Button(buttonFrame, text = "Init", fg = "red",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7", command=UploadFile).grid(row=20,column=3)

# creating Instruction Buttons
InstructionFrame = tk.Frame(window, bg="#97ecf7")
InstructionFrame.grid(row=5,column=0)
def colorChange(button):
  if str(buttons[button].cget("bg")) == "blue":
    buttons[button].config(bg="#97ecf7")
  else:
    buttons[button].config(bg="blue")
buttons = []
btn_no = -1
for i in range (0,16):
  btn_no += 1
  buttons.append(tk.Button(InstructionFrame, text=(-1)*(btn_no-15), bg="#97ecf7", command= lambda x=btn_no: colorChange(x)))
  buttons[btn_no].grid(row=5,column=i, padx=5, pady=30)
  
Separator(InstructionFrame, orient=VERTICAL).place(relx=0.42, rely=0, relwidth=0.001, relheight=1)
Separator(InstructionFrame, orient=VERTICAL).place(relx=0.538, rely=0, relwidth=0.001, relheight=1)
Separator(InstructionFrame, orient=VERTICAL).place(relx=0.653, rely=0, relwidth=0.001, relheight=1)
Separator(InstructionFrame, orient=VERTICAL).place(relx=0.71, rely=0, relwidth=0.001, relheight=1)

Label(InstructionFrame, text = "Operation", justify="right").place(relx = 0.21, rely = 0.1, anchor = 'center')
Label(InstructionFrame, text = "GPR", justify="right").place(relx = 0.48, rely = 0.1, anchor = 'center')
Label(InstructionFrame, text = "IXR", justify="right").place(relx = 0.6, rely = 0.1, anchor = 'center')
Label(InstructionFrame, text = "I", justify="right").place(relx = 0.68, rely = 0.1, anchor = 'center')
Label(InstructionFrame, text = "Address", justify="right").place(relx = 0.85, rely = 0.1, anchor = 'center')

# SS button, Run button, Halt checkbutton and Run checkbutton created
runFrame = tk.Frame(window, bg="#97ecf7")
runFrame.grid(row=4,column=1)
SS_btn = tk.Button(runFrame, text = "SS", fg = "black",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7").grid(row=0,column=0)
Run_btn = tk.Button(runFrame, text = "Run", fg = "black",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7").grid(row=0,column=1)
Halt_ck = tk.Checkbutton(runFrame, text='Halt', bg="#97ecf7").grid(row=0,column=2)
Run_ck = tk.Checkbutton(runFrame, text='Run', bg="#97ecf7").grid(row=1,column=2)

window.mainloop()

