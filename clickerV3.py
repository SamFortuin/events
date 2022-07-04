import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title('Clicker V3')
root.configure(bg="#808080")

def colorChange(newColor): 
    root.configure(bg=newColor)

def counterChange(changeBy):
    global number, latch
    number += changeBy
    print(number)
    counter.configure(text=number)
    if changeBy > 0:
        latch = True
    elif changeBy < 0:
        latch = False
    if number == 0:
        colorChange("#808080")
    elif number > 0:
        colorChange("#008400")
    else:
        colorChange("#ff0000")

def counterMath(a):
    global number,latch
    if latch:
        number *= 3
        counter.configure(text=number)
    elif not latch:
        number /= 3
        counter.configure(text=number)
number = 0
latch = None

btnUp = tk.Button(root)
btnUp.config(text="up",width=30,command=lambda: counterChange(1))
btnUp.place(relx=0.5,rely=0.25,anchor='center')

counter = tk.Label(root)
counter.configure(width=30,text=number)
counter.bind("<Enter>",lambda a:colorChange('#ffff00'))
counter.bind("<Leave>",lambda a:counterChange(0))
counter.bind("<Double-Button-1>",lambda a: counterMath('a'))
counter.place(relx=0.5,rely=0.5,anchor='center')

btnDown = tk.Button(root)
btnDown.bind()
btnDown.config(text="down",width=30,command=lambda: counterChange(-1))
btnDown.place(relx=0.5,rely=0.75,anchor='center')

# test binds
# root.bind("<Up>", lambda a: counterChange(1))
# root.bind("<Down>", lambda a: counterChange(-1))

root.mainloop()