# this is part of the BGPurge project.
#
# Release: v1.0-rc5
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
                width=57,).place(x=0, y=300)

menu_barra = Menu(window)

menu_arquivo = Menu(menu_barra, tearoff=1)
menu_arquivo.add_command(label="Help", command=help_info, font=('Arial'))
menu_barra.add_cascade(label="Menu", menu=menu_arquivo)
window.config(menu=menu_barra)

if __name__ == "__main__":
    check_new_version("1.0-rc5")
    window.mainloop()
