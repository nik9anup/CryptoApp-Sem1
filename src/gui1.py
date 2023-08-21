

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import gui2

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Nikita\APYTHON\ProjectCrypto\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


master = Tk()
import gui2
import gui3
import gui4
import gui5
import gui6
import gui7



master.geometry("1080x610")
master.configure(bg = "#FFFFFF")


canvas = Canvas(
    master,
    bg = "#FFFFFF",
    height = 610,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    547.0,
    305.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png")) #f2 filename---gui(n+1)
button_1 = Button(master,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: gui3.OpenWindow(master),
    relief="flat"
)
button_1.place(
    x=426.0,
    y=182.0,
    width=241.0,
    height=107.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))   #f4
button_2 = Button(master,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:gui5.OpenWindow(master),
    relief="flat"
)
button_2.place(
    x=24.0,
    y=381.0,
    width=241.0,
    height=107.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png")) #f5
button_3 = Button(master,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:gui6.OpenWindow(master),
    relief="flat"
)
button_3.place(
    x=426.0,
    y=392.0,
    width=241.0,
    height=107.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(master,    #f6
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:gui7.OpenWindow(master),
    relief="flat"
)
button_4.place(
    x=792.0,
    y=392.0,
    width=241.0,
    height=107.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(master,
    image=button_image_5,   #f3
    borderwidth=0,
    highlightthickness=0,
    command=lambda:gui4.OpenWindow(master),
    relief="flat"
)
button_5.place(
    x=792.0,
    y=182.0,
    width=241.0,
    height=107.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(master,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,   #f1
    command=lambda:gui2.OpenWindow(master),
    relief="flat"
)
button_6.place(
    x=24.0,
    y=188.0,
    width=241.0,
    height=107.0
)
master.resizable(False, False)
master.mainloop()
