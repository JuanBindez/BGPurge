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

from tkinter import Tk, Button, filedialog
from tkinter import messagebox
from tkinter import *

from src.aboult_module import help_info
from src.extract_background import extract_bg
from src.check_update_module import *
from src.images import *


window = Tk()
window.title("BGPurge")
window.geometry("530x375")

bg = PhotoImage(data=base64.b64decode(BANNER))
label = Label(window, image=bg, bd=0)
label.place(x = 0,y = 0)


button_first = Button(window,
                text="Select Image",
                command=extract_bg,
                font=('Arial'),
                width=57,).place(x=0, y=280)

custom_font1 = ('Arial', 40)
label = Label(window,
                text="BGPurge",
                font=custom_font1,).place(x=155, y=100)

custom_font2 = ('Arial', 10)
label = Label(window,
                text="select the image and the program will remove the background",
                font=custom_font2,).place(x=90, y=200)

custom_font3 = ('Arial', 12)
label = Label(window,
                text="v1.0.0",
                font=custom_font3,).place(x=5, y=350)

menu_barra = Menu(window)

menu_arquivo = Menu(menu_barra, tearoff=0)
menu_arquivo.add_command(label="Help", command=help_info, font=('Arial'))
menu_barra.add_cascade(label="Menu", menu=menu_arquivo)
window.config(menu=menu_barra)

if __name__ == "__main__":
    check_new_version("1.0.0")
    window.mainloop()
