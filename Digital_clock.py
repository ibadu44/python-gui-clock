from tkinter import * 
from time import strftime

root = Tk()
root.geometry('350x150+0+0')
root.config(background='darkblue')
root.overrideredirect(1)

def start():
    text = strftime('%H:%M:%S')
    label.config(text=text)
    label.after(200, start)

label = Label(root, font=('ds-digital', 50, 'bold'), bg='black', fg='green', bd=50)
label.grid(row=0, column=0)

start()
print('done')
root.mainloop()