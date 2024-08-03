# CZEMU NIE MA TUTAJ JAKIŚ POTPOWIEDZI JAK W JAVIE 

import tkinter as tk
from tkinter import messagebox

def chuj():
    messagebox.showinfo("Gratulacje!", "Gratulacje użytkowniku! udało ci się wygrać nic! BRAWO!!!")
    
    root.withdraw()
    
    new_root = tk.Toplevel(root)
    new_root.title("Coś")
    new_root.geometry("300x200")

    help_button = tk.Button(new_root, text="Mam dość", command=new_root.destroy)
    help_button.pack(pady=20)

root = tk.Tk()
root.title("cwel")
root.geometry("300x200")

main_button = tk.Button(root, text="Kliknij po free IPHUJA -2000 IQ NOWA GENERACJA", command=chuj)
main_button.pack(pady=20)

root.mainloop()
