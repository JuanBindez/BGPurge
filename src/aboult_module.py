# this is part of the BGPurge project.
#
# Release: v1.0.0
#
# Copyright ©  2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


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
                font=custom_font_name).place(x=174, y=20)
   
   custom_font_version = ('Arial', 14)
   label = Label(window,
                text="v1.0.0",
                font=custom_font_version).place(x=185, y=45)

   label = Label(window, 
                text="Remove image background.", ).place(x=120, y=88)

   label = Label(window,
                text="This software comes with absolutely no warranty.", ).place(x=45, y=154)

   label = Label(window, 
                text="For more details, visit the GNU General Public License, version 2", ).place(x=9, y=175)
                
   label = Label(window,
                text="Copyright © 2023  Juan Bindez",).place(x=120, y=260)