from tkinter import*
from tkinter import messagebox
def istruzioni():
 messagebox.showinfo('istruzioni','cliccare il bottone in basso per generare automaticamente l Haiku?')
root=Tk()
root.geometry('600x600')
root.title("GENERATORE DI HAIKU AUTOMATICO")
root.configure(background="orange")
lbl=Label(root,text="Benvenuto nel generatore automatico di Haiku!", fg='black', font=("times new roman", 20), background="yellow")
lbl.pack()
b=Button(root, text="Cliccami per le istruzioni d'uso", fg= 'black', command=istruzioni, font=("georgia", 15), background="yellow")
b.pack()
root.mainloop()
