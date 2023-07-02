import base64
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def help_info():
   """displays information about the program.

   clicking on the button will open a window with information.
   """
    
   window = Tk()
   window.title("BGPurge")
   window.geometry("435x300")
   window.resizable(False, False)
   window.attributes('-alpha',9.1)

   custom_font_name = ('Arial', 15)
   label = Label(window,
                text="BGPurge",
                font=custom_font_name).place(x=185, y=20)
   
   custom_font_version = ('Arial', 14)
   label = Label(window,
                text="v1.0-rc1",
                font=custom_font_version).place(x=195, y=42)

   label = Label(window, 
                text="BGPurge: remove image background.", ).place(x=55, y=88)

   label = Label(window,
                text="This software comes with absolutely no warranty.", ).place(x=45, y=154)

   label = Label(window, 
                text="For more details, visit the GNU General Public License, version 2", ).place(x=9, y=170)
                
   label = Label(window,
                text="Copyright © 2023  Juan Bindez",).place(x=80, y=260)