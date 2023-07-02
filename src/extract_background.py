# this is part of the BGPurge project.
#
# Release: v1.0-rc3
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



from rembg import remove
import PIL.Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox



def extract_bg():
    def open_file():

        file_path = filedialog.askopenfilename()
        return file_path

    image_name = open_file()

    if image_name:
        img = PIL.Image.open(image_name)

        image_out = remove(img)

        image_out.save('image_out.png')
        messagebox.showinfo("BGPurge", 
                                    "Successfully cleaned background image salved!")