# from dis import Instruction
from instruction import Instruction
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Separator 
from cpu import CPU
import sys
sys.path.insert(0, './memory')
from memory import Memory 
import helper_functions

# make instance of CPU
cpu = CPU()
def UploadFile(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    
    # load the txt input program into memory
    CPU.load_program(cpu, filename)
    
# on "Store" button click, store value of MBR into Memory[MAR]
def gui_store():
    word = helper_functions.binary_to_decimal(cpu.mar.get_value())
    cpu.memory.store_memory_value(word, cpu.mbr.get_value())
    helper_functions.print_memory_contents(cpu.memory)
    
# on "Load" button click, load value at Memory[MAR] into MBR
def gui_load():
    word = helper_functions.binary_to_decimal(cpu.mar.get_value())
    print(word)
    value = cpu.memory.get_memory_value(word)
    print(value)
    cpu.mbr.set_value(value)
    helper_functions.print_memory_contents(cpu.memory)
    if value == 0:
        bitToCheckbox(mbr, '0000000000000000')
    else:
        str1 = str(cpu.mbr.get_value()).zfill(16)
        bitToCheckbox(mbr, str1)
  
# on "LD" button click, load GPR0 with input value
def ld_gpr0(value):
    bits = ""
    for i in range(0, 16):
      if str(buttons[i].cget("bg")) == "blue":
        colorChange(i)
        bits += '1'
      else:
        bits += '0'
        
    cpu.gpr0.set_value(bits)
    bitToCheckbox(gpr0, bits)
    print("Loaded GPR0: {}".format(cpu.gpr0.get_value()))

# on "LD" button click, load GPR1 with input value
def ld_gpr1(value):
    bits = ""
    for i in range(0, 16):
      if str(buttons[i].cget("bg")) == "blue":
        colorChange(i)
        bits += '1'
      else:
        bits += '0'
        
    cpu.gpr1.set_value(bits)
    bitToCheckbox(gpr1, bits)
    print("Loaded GPR1: {}".format(cpu.gpr1.get_value()))

# on "LD" button click, load GPR2 with input value
def ld_gpr2(value):
    bits = ""
    for i in range(0, 16):
      if str(buttons[i].cget("bg")) == "blue":
        colorChange(i)
        bits += '1'
      else:
        bits += '0'
        
    cpu.gpr2.set_value(bits)
    bitToCheckbox(gpr2, bits)
    print("Loaded GPR2: {}".format(cpu.gpr2.get_value()))

# on "LD" button click, load GPR3 with input value
def ld_gpr3(value):
    bits = ""
    for i in range(0, 16):
      if str(buttons[i].cget("bg")) == "blue":
        colorChange(i)
        bits += '1'
      else:
        bits += '0'
        
    cpu.gpr3.set_value(bits)
    bitToCheckbox(gpr3, bits)
    print("Loaded GPR3: {}".format(cpu.gpr3.get_value()))

# on "LD" button click, load IXR1 with input value
def ld_ixr1(value):
    bits = ""
    for i in range(0, 16):
      if str(buttons[i].cget("bg")) == "blue":
        colorChange(i)
        bits += '1'
      else:
        bits += '0'
        
    cpu.ixr1.set_value(bits)
    bitToCheckbox(ixr1, bits)
    print("Loaded ixr1: {}".format(cpu.ixr1.get_value()))

# on "LD" button click, load IXR2 with input value
def ld_ixr2(value):
    bits = ""
    for i in range(0, 16):
      if str(buttons[i].cget("bg")) == "blue":
        colorChange(i)
        bits += '1'
      else:
        bits += '0'
        
    cpu.ixr2.set_value(bits)
    bitToCheckbox(ixr2, bits)
    print("Loaded ixr2: {}".format(cpu.ixr2.get_value()))

# on "LD" button click, load IXR3 with input value 
def ld_ixr3(value):
    bits = ""
    for i in range(0, 16):
      if str(buttons[i].cget("bg")) == "blue":
        colorChange(i)
        bits += '1'
      else:
        bits += '0'
        
    cpu.ixr3.set_value(bits)
    bitToCheckbox(ixr3, bits)
    print("Loaded ixr3: {}".format(cpu.ixr3.get_value()))

# on "LD" button click, load MAR with input value 
def ld_mar():
  bits = ""
  for i in range(4, 16):
    if str(buttons[i].cget("bg")) == "blue":
      colorChange(i)
      bits += '1'
    else:
      bits += '0'
  print(bits)
  cpu.mar.set_value(bits)
  print("Loaded mar: {}".format(cpu.mar.get_value()))
  bitToCheckbox(mar, bits)

# on "LD" button click, load PC with input value 
def ld_pc():
  bits = ""
  for i in range(4, 16):
    if str(buttons[i].cget("bg")) == "blue":
      colorChange(i)
      bits += '1'
    else:
      bits += '0'
  print(bits)
  val = helper_functions.binary_to_decimal(int(bits))
  cpu.pc.set_value(val)
  print("Loaded pc: {}".format(cpu.pc.get_value()))
  bitToCheckbox(pc, bits)
  
# on "LD" button click, load MBR with input value 
def ld_mbr():
  bits = ""
  for i in range(0, 16):
    if str(buttons[i].cget("bg")) == "blue":
      colorChange(i)
      bits += '1'
    else:
      bits += '0'
  
  cpu.mbr.set_value(bits)
  print("Loaded mbr: {}".format(cpu.mbr.get_value()))
  bitToCheckbox(mbr, bits)
  
# changes the color of the instruction switches
def colorChange(button):
  if str(buttons[button].cget("bg")) == "blue":
    buttons[button].config(bg="#97ecf7")
  else:
    buttons[button].config(bg="blue")
    
# bit array to be represented with the checkboxes
def bitToCheckbox(boxArray, bitArray):
  for i in range(len(boxArray)):
    if bitArray[i] == '1':
      boxArray[i].set(1)
    else:
      boxArray[i].set(0)

window = Tk()
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
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr0[i-1], bg="#97ecf7", onvalue=1, offvalue=0).grid(row=0,column=i)
gpr0_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green", padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: ld_gpr0(gpr0)).grid(row=0,column=17)
# gpr0_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green", command=lambda: bitToCheckbox(gpr0, "1111100000101010010001010"), padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7").grid(row=0,column=17)

gpr1_btn = tk.Label(registersGPRFrame, text = "GPR 1", fg = "green",padx=5,pady=5,relief=tk.RAISED)
gpr1_btn.grid(row=1,column=0)
gpr1 = []
for i in range (1,17):
  gpr1.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr1[i-1], bg="#97ecf7").grid(row=1,column=i)
gpr1_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: ld_gpr1(gpr1)).grid(row=1,column=17)

gpr2_btn = tk.Label(registersGPRFrame, text = "GPR 2", fg = "green",padx=5,pady=5,relief=tk.RAISED)
gpr2_btn.grid(row=2,column=0)
gpr2 = []
for i in range (1,17):
  gpr2.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr2[i-1], bg="#97ecf7").grid(row=2,column=i)
gpr2_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: ld_gpr2(gpr2)).grid(row=2,column=17)

gpr3_btn = tk.Label(registersGPRFrame, text = "GPR 3", fg = "green",padx=5,pady=5,relief=tk.RAISED)
gpr3_btn.grid(row=3,column=0)
gpr3 = []
for i in range (1,17):
  gpr3.append(IntVar())
  tk.Checkbutton(registersGPRFrame, text='', variable=gpr3[i-1], bg="#97ecf7").grid(row=3,column=i)
gpr3_LD = tk.Button(registersGPRFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: ld_gpr3(gpr3)).grid(row=3,column=17)

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
ixr1_LD = tk.Button(indexFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: ld_ixr1(ixr1)).grid(row=5,column=17)

ixr2_btn = tk.Label(indexFrame , text = "IXR 2", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
ixr2_btn.grid(row=6,column=0)
ixr2 = []
for i in range (1,17):
  ixr2.append(IntVar())
  tk.Checkbutton(indexFrame, text='', variable=ixr2[i-1], bg="#97ecf7").grid(row=6,column=i)
ixr2_LD = tk.Button(indexFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: ld_ixr2(ixr2)).grid(row=6,column=17)

ixr3_btn = tk.Label(indexFrame , text = "IXR 3", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
ixr3_btn.grid(row=7,column=0)
ixr3 = []
for i in range (1,17):
  ixr3.append(IntVar())
  tk.Checkbutton(indexFrame, text='', variable=ixr3[i-1], bg="#97ecf7").grid(row=7,column=i)
ixr3_LD = tk.Button(indexFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: ld_ixr3(ixr3)).grid(row=7,column=17)

# creating frame for PC, MAR, MBR, IR, MFR, CC, Privileged 
otherFrame = tk.Frame(window, bg="#97ecf7")
otherFrame.grid(row=0,column=2)
otherFrame.grid_columnconfigure(4, weight=1, minsize=50)

# label for for PC, MAR, MBR, IR, MFR, Privileged
pc_btn = tk.Label(otherFrame, text = "PC", fg = "blue",width=6,relief=tk.RAISED,justify='right')
pc_btn.grid(row=1,column=22)
pc = []
for i in range (23,35):
  pc.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=pc[i-23], bg="#97ecf7").grid(row=1,column=i)
pc_LD= tk.Button(otherFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: ld_pc()).grid(row=1,column=35)

mar_btn = tk.Label(otherFrame, text = "MAR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
mar_btn.grid(row=2,column=22)
mar = []
for i in range (23,35):
  mar.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mar[i-23], bg="#97ecf7").grid(row=2,column=i)
mar_LD = tk.Button(otherFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: ld_mar()).grid(row=2,column=35)

mbr_btn = tk.Label(otherFrame, text = "MBR", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
mbr_btn.grid(row=3,column=18)
mbr = []
for i in range (19,35):
  mbr.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=mbr[i-19], bg="#97ecf7").grid(row=3,column=i)
mbr_LD = tk.Button(otherFrame, text = "LD", fg = "green",padx=8,pady=5,relief=tk.RAISED, bg="#97ecf7", command=lambda: ld_mbr()).grid(row=3,column=35)

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

cc_btn = tk.Label(otherFrame, text = "CC", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
cc_btn.grid(row=6,column=30)
cc = []
for i in range (31,35):
  cc.append(IntVar())
  tk.Checkbutton(otherFrame, text='', variable=cc[i-31], bg="#97ecf7").grid(row=6,column=i)

privileged_btn = tk.Label(otherFrame, text = "Privileged", fg = "blue",padx=5,pady=5,relief=tk.RAISED)
privileged_btn.grid(row=7,column=33)
priv_1 = tk.Checkbutton(otherFrame, text='', bg="#97ecf7").grid(row=7,column=34)

# creating frame for Store, St+, Load, and Init buttons 
buttonFrame = tk.Frame(window, bg="#97ecf7")
buttonFrame.grid(row=4,column=4)
buttonFrame.grid_columnconfigure(4, weight=7, minsize=100)

store_btn = tk.Button(buttonFrame, text = "Store", fg = "green",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7", command=lambda:gui_store()).grid(row=20,column=0)
# store_plus_btn = tk.Button(buttonFrame, text = "Store+", fg = "green",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7").grid(row=20,column=1)
load_btn = tk.Button(buttonFrame, text = "Load", fg = "green",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7", command=lambda:gui_load()).grid(row=20,column=2)
init_btn = tk.Button(buttonFrame, text = "Init", fg = "red",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7", command=UploadFile).grid(row=20,column=3)

# creating Instruction Buttons
InstructionFrame = tk.Frame(window, bg="#97ecf7")
InstructionFrame.grid(row=5,column=0)
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
SS_btn = tk.Button(runFrame, text = "SS", fg = "black",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7", command=lambda:stepCheck()).grid(row=0,column=0)
Run_btn = tk.Button(runFrame, text = "Run", fg = "black",padx=8,pady=8,relief=tk.RAISED, bg="#97ecf7", command=lambda:runCheck()).grid(row=0,column=1)
Halt_ck = tk.Checkbutton(runFrame, text='Halt', bg="#97ecf7").grid(row=0,column=2)
Run_ck = tk.Checkbutton(runFrame, text='Run', bg="#97ecf7").grid(row=1,column=2)

# On step through update checkboxes
def stepCheck():  
  bitToCheckbox(gpr0,helper_functions.decimal_to_bit_array_unsigned(int(cpu.gpr0.get_value()),cpu.gpr0.get_register_size()))
  bitToCheckbox(gpr1,helper_functions.decimal_to_bit_array_unsigned(int(cpu.gpr1.get_value()),cpu.gpr1.get_register_size()))
  bitToCheckbox(gpr2,helper_functions.decimal_to_bit_array_unsigned(int(cpu.gpr2.get_value()),cpu.gpr2.get_register_size()))
  bitToCheckbox(gpr3,helper_functions.decimal_to_bit_array_unsigned(int(cpu.gpr3.get_value()),cpu.gpr3.get_register_size()))

  bitToCheckbox(ixr1,helper_functions.decimal_to_bit_array_unsigned(int(cpu.ixr1.get_value()),cpu.ixr1.get_register_size()))
  bitToCheckbox(ixr2,helper_functions.decimal_to_bit_array_unsigned(int(cpu.ixr2.get_value()),cpu.ixr2.get_register_size()))
  bitToCheckbox(ixr3,helper_functions.decimal_to_bit_array_unsigned(int(cpu.ixr3.get_value()),cpu.ixr3.get_register_size()))

  bitToCheckbox(pc,helper_functions.decimal_to_bit_array_unsigned(int(cpu.pc.get_value()),cpu.pc.get_register_size()))
  bitToCheckbox(mar,helper_functions.decimal_to_bit_array_unsigned(int(cpu.mar.get_value()),cpu.mar.get_register_size()))
  bitToCheckbox(mbr,helper_functions.decimal_to_bit_array_unsigned(int(cpu.mbr.get_value()),cpu.mbr.get_register_size()))
  bitToCheckbox(ir,helper_functions.decimal_to_bit_array_unsigned(int(cpu.ir.get_value()),cpu.ir.get_register_size()))

  CPU.step_through(cpu)
  
# On run, update and step through entire program
def runCheck():
  cpu.HLT = 0
  for i in range(cpu.pc.get_value(), cpu.memory.get_memory_size()):
      bitToCheckbox(gpr0,helper_functions.decimal_to_bit_array_unsigned(int(cpu.gpr0.get_value()),cpu.gpr0.get_register_size()))
      bitToCheckbox(gpr1,helper_functions.decimal_to_bit_array_unsigned(int(cpu.gpr1.get_value()),cpu.gpr1.get_register_size()))
      bitToCheckbox(gpr2,helper_functions.decimal_to_bit_array_unsigned(int(cpu.gpr2.get_value()),cpu.gpr2.get_register_size()))
      bitToCheckbox(gpr3,helper_functions.decimal_to_bit_array_unsigned(int(cpu.gpr3.get_value()),cpu.gpr3.get_register_size()))

      bitToCheckbox(ixr1,helper_functions.decimal_to_bit_array_unsigned(int(cpu.ixr1.get_value()),cpu.ixr1.get_register_size()))
      bitToCheckbox(ixr2,helper_functions.decimal_to_bit_array_unsigned(int(cpu.ixr2.get_value()),cpu.ixr2.get_register_size()))
      bitToCheckbox(ixr3,helper_functions.decimal_to_bit_array_unsigned(int(cpu.ixr3.get_value()),cpu.ixr3.get_register_size()))

      bitToCheckbox(pc,helper_functions.decimal_to_bit_array_unsigned(int(cpu.pc.get_value()),cpu.pc.get_register_size()))
      bitToCheckbox(mar,helper_functions.decimal_to_bit_array_unsigned(int(cpu.mar.get_value()),cpu.mar.get_register_size()))
      bitToCheckbox(mbr,helper_functions.decimal_to_bit_array_unsigned(int(cpu.mbr.get_value()),cpu.mbr.get_register_size()))
      bitToCheckbox(ir,helper_functions.decimal_to_bit_array_unsigned(int(cpu.ir.get_value()),cpu.ir.get_register_size()))
  
      CPU.step_through(cpu)
      
      if cpu.HLT == 1:
          break

window.mainloop()