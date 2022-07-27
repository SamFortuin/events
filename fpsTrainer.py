from random import randint,choice
from string import capwords
import tkinter as tk

root = tk.Tk()
root.configure(bg="#000555")
root.title("FPS Trainer")
root.geometry("600x400")

timer = 0
score = 0

def placeLabel():
    global lbl,keyPresses
    keyPresses = ['w','a','s','d','<space>','<Button-1>','<Double-Button-1>','<Triple-Button-1>']
    lbl = tk.Label()
    lbl.configure(bg='red',height=3,textvariable=pressString)
    randX = randint(1,91) / 100
    randY = randint(1,87) / 100
    lbl.place(relx=randX,rely=randY)
    currentKey = choice(keyPresses)
    cleanedKey = capwords(currentKey[1:-1]).replace('-',' ') if "<" in currentKey else currentKey.upper()
    lbl.configure(width=6) if len(currentKey) <= 1 or currentKey == '<space>' else None
    pressString.set(cleanedKey)
    root.bind(f'{currentKey}',lambda a: newLabel(currentKey))

def newLabel(key):
    global lbl
    root.unbind(key)
    lbl.destroy()
    placeLabel()


counter = tk.StringVar(root,value=timer)
def clock():
    global timer, keyPresses, counter
    timer+=1
    counter.set(timer)
    print(timer)
    if timer == 20:
        for x in keyPresses:
            root.unbind(x)
        lbl.destroy()
    else:
        root.after(1000,clock)

counterLbl = tk.Label()
counterLbl.configure(bg="white",textvariable=counter)
counterLbl.place(relx=0,rely=0)

placeHolderString = 'a'
pressString = tk.StringVar(root,value=placeHolderString)
placeLabel()
root.after(1000,clock)

root.mainloop()