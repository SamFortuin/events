from random import randint,choice
from string import capwords
import tkinter as tk

root = tk.Tk()
root.configure(bg="#000555")
root.title("FPS Trainer")
root.geometry("600x400")

# def key2press():
    

def placeLabel():
    keyPresses = ['w','a','s','d','<space>','<Button-1>','<Double-Button-1>','<Triple-Button-1>']
    lbl = tk.Label()
    lbl.configure(bg='red',height=3,textvariable=pressString)
    randX = randint(1,91) / 100
    randY = randint(1,87) / 100
    lbl.place(relx=randX,rely=randY)
    currentKey = choice(keyPresses)
    cleanedKey = capwords(currentKey).replace('<','').replace('>','')
    lbl.configure(width=6) if len(currentKey) <= 1 else None
    pressString.set(cleanedKey)
    root.bind(f'{currentKey}',lambda a: lbl.destroy())

a = 'simp'
pressString = tk.StringVar(root,value=a)
placeLabel()

root.mainloop()