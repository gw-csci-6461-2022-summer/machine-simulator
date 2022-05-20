from tkinter import *

root = Tk()
root.configure(background='aliceblue',padx=300, pady=300)

def store():
    myLabel = Label(root, text = "Store")
    myLabel.pack()

def load():
    myLabel = Label(root, text = "Load")
    myLabel.pack()

def init():
    myLabel = Label(root, text = "Init")
    myLabel.pack()

storeButton = Button(root, text="store",command=store,fg='blue')
storeButton.pack()
laodButton = Button(root, text="Load",command=load,fg='blue')
laodButton.pack()
initButton = Button(root, text="Init",command=init,fg='blue')
initButton.pack()

root.mainloop()
