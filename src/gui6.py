
def OpenWindow(master):

    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, OptionMenu, StringVar,Toplevel
    window=Toplevel(master)


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Nikita\APYTHON\ProjectCrypto\build\assets\frame6")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)




    import sys
    sys.path.insert(0,r"c:\Users\Nikita\APYTHON\ProjectCrypto")
    import Mylibrary as ml
    import Graph as g

    global image_1
    global entry_bg_1
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

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=window.withdraw,
        relief="flat"
    )
    button_1.place(
        x=865.0,
        y=42.0,
        width=154.0,
        height=68.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: g.histrades(clicked.get(),entry_1.get()),
        relief="flat"
    )
    button_2.place(
        x=865.0,
        y=483.0,
        width=153.58984375,
        height=66.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        403.0,
        323.5,
        image=entry_image_1
    )
    entry_1 = Entry(window,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=40.0,
        y=305.0,
        width=726.0,
        height=35.0
    )

    canvas.create_text(
        39.53125,
        132.84445190429688,
        anchor="nw",
        text="SELECT CRYPTOCURRENCY:",
        fill="#FFFFFF",
        font=("Nunito Regular", 30 * -1)
    )

    clicked=StringVar()
    clicked.set("SELECT CRYPTO")
    drop=OptionMenu(window,clicked,"Bitcoin","Ethereum","Litecoin","Dogecoin","Cardano","Solana","AAVE")
    drop.place(x=490,y=132.84445190429688)
    drop.config(width=40,bg="yellow",fg="black")

    canvas.create_text(
        40.0,
        242.0,
        anchor="nw",
        text="ENTER NUMBER OF DAYS:",
        fill="#FFFFFF",
        font=("Nunito Regular", 30 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
