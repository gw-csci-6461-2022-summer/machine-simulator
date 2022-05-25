import tkinter as tk

window = tk.Tk()
window.configure(background='aliceblue',padx=300, pady=300)
window.title("Machine Simulator")

# creating frames and aliging them with pack()
top_frame = tk.Frame(window).pack(side = "left")
bottom_frame = tk.Frame(window).pack(side = "bottom")
Left_frame = tk.Frame(window).pack(side = "left")
right_frame = tk.Frame(window).pack(side = "right")

# labels for 4 general purpose registers 
btn1 = tk.Label(top_frame, text = "gpr_0", fg = "green",padx=5,pady=10,relief=tk.RAISED).pack() 
btn2 = tk.Label(top_frame, text = "gpr_1", fg = "green",padx=5,pady=10,relief=tk.RAISED).pack()
btn3 = tk.Label(top_frame, text = "gpr_2", fg = "green",padx=5,pady=10,relief=tk.RAISED).pack()
btn4 = tk.Label(top_frame, text = "gpr_3", fg = "green",padx=5,pady=10,relief=tk.RAISED).pack()

# labels for  3 Index Registers 1-3
btn5 = tk.Label(top_frame,Left_frame, text = "ix_1", fg = "blue",padx=5,pady=10,relief=tk.RAISED).pack() 
btn6 = tk.Label(top_frame, text = "ix_2", fg = "blue",padx=5,pady=10,relief=tk.RAISED).pack()
btn7 = tk.Label(top_frame, text = "ix_2", fg = "blue",padx=5,pady=10,relief=tk.RAISED).pack()

# labels for for PC, MAR, MBR, IR, MFR, Privileged
btn8 = tk.Label(right_frame, text = "PC", fg = "blue",padx=5,pady=10).pack(side="top")
btn9 = tk.Label(right_frame, text = "MAR", fg = "blue",padx=5,pady=10).pack(side="right")
btn10 = tk.Label(right_frame, text = "MBR", fg = "blue",padx=5,pady=10).pack(side="right")
btn11= tk.Label(right_frame, text = "IR", fg = "blue",padx=5,pady=10).pack(side="right")
btn12= tk.Label(right_frame, text = "MFR", fg = "blue",padx=5,pady=10).pack(side="right")

# store, load, initialize 

def store():
    myLabel = tk.Label(window, text = "Store")
    myLabel.pack()

def load():
    myLabel = tk.Label(window, text = "Load")
    myLabel.pack()

def init():
    myLabel = tk.Label(window, text = "Init")
    myLabel.pack()

storeButton = tk.Button(bottom_frame, text="store",command=store,fg='red', padx=5,pady=10)
storeButton.pack()
laodButton = tk.Button(bottom_frame, text="Load",command=load,fg='red',padx=5,pady=10)
laodButton.pack()
initButton = tk.Button(bottom_frame, text="Init",command=init,fg='red',width=5,height=10)
initButton.pack()

initButton.pack()
window.mainloop()

