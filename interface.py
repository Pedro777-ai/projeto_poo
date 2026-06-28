# Parte visual 

import tkinter as tk
from tkinter import ttk

class Interface:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Biblioteca Escolar")
        self.janela.geometry("800x600")

        self.janela.mainloop()