
import tkinter as tk

def hello():
    value= entry.get()
    out['text']= f"Hello, {value}"

window = tk.Tk()

label = tk.Label(text='Enter your name:', height=2, width=25)
entry = tk.Entry(width=25)
button= tk.Button(text= 'Go', command= hello)
out= tk.Label(height=2, width=25)

label.pack()
entry.pack()
button.pack()
out.pack()
window.mainloop()