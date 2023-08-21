
def OpenWindow(master):
    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Label,Toplevel
    window=Toplevel(master)


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Nikita\APYTHON\ProjectCrypto\build\assets\frame4")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    import sys
    sys.path.insert(0,r"c:\Users\Nikita\APYTHON\ProjectCrypto")
    import Mylibrary as ml

    global image_1

    window.geometry("1080x610")
    window.configure(bg = "#FFFFFF")


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

    y1=212
    Label(window,text="Name: ",height=2,width=10,bg="yellow",fg="black",font=("Arial", 15)).place(x=90,y=130.0)
    Label(window,text="Symbol: ",height=2,width=10,bg="yellow",fg="black",font=("Arial", 15)).place(x=310,y=130.0)
    Label(window,text="Market Cap rank: ",height=2,width=16,bg="yellow",fg="black",font=("Arial", 15)).place(x=520,y=130.0)
    Label(window,text="Price in BTC: ",height=2,width=15,bg="yellow",fg="black",font=("Arial", 15)).place(x=765,y=130.0)
    for i in ml.trending(7):
        Label(window,text=i[0],height=2,width=15,bg="yellow",fg="black",font=("Arial", 15)).place(x=90,y=y1)
        Label(window,text=i[1],height=2,width=15,bg="yellow",fg="black",font=("Arial", 15)).place(x=310,y=y1)
        Label(window,text=i[2],height=2,width=15,bg="yellow",fg="black",font=("Arial", 15)).place(x=520,y=y1)
        Label(window,text=i[3],height=2,width=24,bg="yellow",fg="black",font=("Arial", 15)).place(x=765,y=y1)
        y1=y1+50
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=window.withdraw, #home button
        relief="flat"
    )
    button_1.place(
        x=848.0,
        y=37.0,
        width=155.0,
        height=68.0
    )
    window.resizable(False, False)
    window.mainloop()
