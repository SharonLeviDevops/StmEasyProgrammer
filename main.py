import sys
from io import BytesIO
from tkinter.ttk import Combobox
import tkinter.font as tkFont
import re
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import subprocess, os

path = [r"X:\\Software\\Eureka\\Version 2.1.0.2\\Slaves\\twine-winder-g743-master\\Debug\\twine-winder-g743-master.bin",
        r"X:\\Software\\Eureka\\Version 2.1.0.2\\Slaves\\twine-midtank-g743-master\\Debug\\twine-midtank-g743-master.bin",
        r"X:\\Software\\Eureka\\Version 2.1.0.2\\Slaves\\twine-lubricant-g743-master\\Debug\\twine-lubricant-g743-master.bin",
        r"X:\\Software\\Eureka\\Version 2.1.0.2\\Slaves\\twine-head-g473-master\\Debug\\twine-head-g473-master.bin",
        r"X:\\Software\\Eureka\\Version 2.1.0.2\\Slaves\\twine-emulator-g473-master\\Debug\\twine-emulator-g473-master.bin",
        r"X:\\Software\\Eureka\\Version 2.1.0.2\\Slaves\\twine-dryer-g473-master\\Debug\\twine-dryer-g473-master",
        r"X:\\Software\\Eureka\\Version 2.1.0.2\\Slaves\\twine-dispenser-g473-master\\Debug\\twine-dispenser-g473-master.bin"]
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# setting title
ws = tk.Tk()
ws.title('Twine LTD - Stm32 Easy Programmer')
window_width = 600
window_height = 470


bg = PhotoImage(file=resource_path("22.png"))
canvas1 = Canvas(ws, width=500,
                 height=500)
canvas1.pack(fill="both", expand=True)
# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")
# get the screen dimension
screen_width = ws.winfo_screenwidth()
screen_height = ws.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
ws.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

ws.resizable(width=False, height=False)
pic = PhotoImage(file=resource_path("1.png"))
pic2 = PhotoImage(file=resource_path("2.png"))
pic3 = PhotoImage(file=resource_path("3.png"))
pic4 = PhotoImage(file=resource_path("4.png"))
pic5 = PhotoImage(file=resource_path("5.png"))
pic6 = PhotoImage(file=resource_path("6.png"))



def New_Window():
    command = f'cmd.exe /k start {resource_path("test.bat")}'
    subprocess.Popen(command)

def AreYouSure():
    MsgBox = tk.messagebox.askquestion('Burn Firmware', 'Are you sure you want to burn this firmware?',
                                       icon='warning')
    if MsgBox == 'yes':
        return True
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)


def find_and_replace(path_to_replace):
    with open(resource_path("test.bat"), "r") as rfile:
        s = rfile.read()
        rplce = re.sub('filepath', path_to_replace, s)
    with open(resource_path("test.bat"), "w") as wfile:
        wfile.write(rplce)
        New_Window()


def Resetfile():
    with open(resource_path("original_file.bat"), 'rb') as f2, open(resource_path("test.bat"), 'wb') as f1:
        shutil.copyfileobj(f2, f1)


def GButton_480_command():
    AreYouSure()
    if AreYouSure:
        find_and_replace(path[0])
    Resetfile()


def GButton_420_command():
    AreYouSure()
    if AreYouSure:
        find_and_replace(path[1])
    Resetfile()


def GButton_647_command():
    AreYouSure()
    if AreYouSure:
        find_and_replace(path[2])
    Resetfile()


def GButton_988_command():
    AreYouSure()
    if AreYouSure:
        find_and_replace(path[3])
    Resetfile()


def GButton_806_command():
    AreYouSure()
    if AreYouSure:
        find_and_replace(path[4])
    Resetfile()


def GButton_229_command():
    AreYouSure()
    if AreYouSure:
        find_and_replace(path[5])
    Resetfile()


GButton_480 = tk.Button()
GButton_480["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
GButton_480["font"] = ft
GButton_480["fg"] = "#000000"
GButton_480["justify"] = "center"
GButton_480["text"] = "Winder-g743-master"
GButton_480.place(x=70, y=150, width=114, height=102)
GButton_480["image"] = pic6
GButton_480["command"] = lambda: GButton_480_command()

GButton_420 = tk.Button()
GButton_420["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
GButton_420["font"] = ft
GButton_420["fg"] = "#000000"
GButton_420["justify"] = "center"
GButton_420.place(x=240, y=150, width=114, height=102)
GButton_420["image"] = pic3
GButton_420["command"] = lambda: GButton_420_command()

GButton_647 = tk.Button()
GButton_647["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
GButton_647["font"] = ft
GButton_647["fg"] = "#000000"
GButton_647["justify"] = "center"
GButton_647.place(x=410, y=150, width=114, height=102)
GButton_647["image"] = pic5
GButton_647["command"] = lambda: GButton_647_command()

GButton_988 = tk.Button()
GButton_988["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
GButton_988["font"] = ft
GButton_988["fg"] = "#000000"
GButton_988["justify"] = "center"
GButton_988["text"] = ""
GButton_988.place(x=70, y=290, width=114, height=102)
GButton_988["image"] = pic
GButton_988["command"] = lambda: GButton_988_command()

GButton_806 = tk.Button()
GButton_806["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
GButton_806["font"] = ft
GButton_806["fg"] = "#000000"
GButton_806["justify"] = "center"
GButton_806["text"] = ""
GButton_806.place(x=240, y=290, width=114, height=102)
GButton_806["image"] = pic2
GButton_806["command"] = lambda: GButton_806_command()

GButton_229 = tk.Button()
GButton_229["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
GButton_229["font"] = ft
GButton_229["fg"] = "#000000"
GButton_229["justify"] = "center"
GButton_229["text"] = ""
GButton_229.place(x=410, y=290, width=114, height=102)
GButton_229["image"] = pic4
GButton_229["command"] = lambda: GButton_229_command()

GLabel_692 = tk.Label()
GLabel_692["bg"] = "#9fa0ab"
ft = tkFont.Font(family='Ariel', size=27)
GLabel_692["font"] = ft
GLabel_692["fg"] = "#000000"
GLabel_692["justify"] = "center"
GLabel_692["text"] = "Stm32 Easy Programmer"
GLabel_692["relief"] = "raised"
GLabel_692.place(x=80, y=10, width=430, height=36)

GLabel_949 = tk.Label()
GLabel_949["bg"] = "#9fa0ab"
ft = tkFont.Font(family='Ariel', size=16)
GLabel_949["font"] = ft
GLabel_949["fg"] = "#000000"
GLabel_949["justify"] = "center"
GLabel_949["text"] = "Select firmware to quick burn:"
GLabel_949.place(x=140, y=50, width=270, height=47)

GLabel_690 = tk.Label()
ft = tkFont.Font(family='Ariel', size=16)
GLabel_690["font"] = ft
GLabel_690["fg"] = "#333333"
GLabel_690["justify"] = "center"
GLabel_690["text"] = "Winder-g743"
GLabel_690.place(x=50, y=110, width=150, height=38)

GLabel_329 = tk.Label()
ft = tkFont.Font(family='Ariel', size=16)
GLabel_329["font"] = ft
GLabel_329["fg"] = "#333333"
GLabel_329["justify"] = "center"
GLabel_329["text"] = "Midtank-g743"
GLabel_329.place(x=220, y=110, width=150, height=38)

GLabel_935 = tk.Label()
ft = tkFont.Font(family='Ariel', size=16)
GLabel_935["font"] = ft
GLabel_935["fg"] = "#333333"
GLabel_935["justify"] = "center"
GLabel_935["text"] = "Lubricant-g743"
GLabel_935.place(x=390, y=110, width=150, height=38)

GLabel_848 = tk.Label()
ft = tkFont.Font(family='Ariel', size=16)
GLabel_848["font"] = ft
GLabel_848["fg"] = "#333333"
GLabel_848["justify"] = "center"
GLabel_848["text"] = "Head-g473"
GLabel_848.place(x=70, y=260, width=106, height=25)

GLabel_421 = tk.Label()
ft = tkFont.Font(family='Ariel', size=16)
GLabel_421["font"] = ft
GLabel_421["fg"] = "#333333"
GLabel_421["justify"] = "center"
GLabel_421["text"] = "Emulator-g473"
GLabel_421.place(x=220, y=260, width=150, height=25)

GLabel_360 = tk.Label()
ft = tkFont.Font(family='Ariel', size=16)
GLabel_360["font"] = ft
GLabel_360["fg"] = "#333333"
GLabel_360["justify"] = "center"
GLabel_360["text"] = "Dryer-g473"
GLabel_360.place(x=400, y=260, width=150, height=25)
tk.messagebox.showinfo('Welcome to Easy programmer', 'Make sure stm board is connected to the usb port')





ws.mainloop()
