# this is part of the BGPurge project.
#
# Release: v1.0-rc1
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


from tkinter import Tk, Button, filedialog
from tkinter import messagebox

from src.aboult_module import *
from src.extract_background import extract_bg


window = Tk()
window.title("BGPurge")
window.geometry("530x375")


button_first = Button(window,
                text="Select Image",
                command=extract_bg,
                font=('Arial'),
                width=57,).place(x=0, y=300)


window.mainloop()
