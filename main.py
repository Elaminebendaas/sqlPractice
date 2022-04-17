import tkinter
import time
from tkinter import font
import customtkinter as ctk

main = ctk.CTk()
main.geometry('725x375')


companyName = ctk.CTkLabel(master=main, text="Hello World!",width=150,height=50, font='')

companyName.place(relx=0.1, rely= 0.07, anchor=tkinter.CENTER)




main.mainloop()

