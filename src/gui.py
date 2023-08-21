
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Nikita\APYTHON\ProjectCrypto\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1080x610")
window.configure(bg = "#FFFFFF")

def NextPage():
    window.destroy()
    import gui1

canvas = Canvas(
    window,
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
    540.0,
    305.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=NextPage,
    relief="flat"
)
button_1.place(
    x=680.0,
    y=320.0,
    width=320.0,
    height=161.0
)
window.resizable(False, False)
window.mainloop()
