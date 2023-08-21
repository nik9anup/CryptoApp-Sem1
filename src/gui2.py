
def OpenWindow(master):
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, OptionMenu, StringVar, Label,Toplevel

    window=Toplevel(master)
    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Nikita\APYTHON\ProjectCrypto\build\assets\frame2")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    import sys
    sys.path.insert(0,r"c:\Users\Nikita\APYTHON\ProjectCrypto")
    import Mylibrary as ml
    

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

    button_image_1 = PhotoImage(   #home button
        file=relative_to_assets("button_1.png"))
    button_1 = Button(window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=window.withdraw,
        relief="flat"
    )
    button_1.place(
        x=859.0,
        y=37.0,
        width=154.0,
        height=68.0
    )

    canvas.create_text(
        25.0,
        295.0,
        anchor="nw",
        text="ENTER AMOUNT",
        fill="#FFFFFF",
        font=("Nunito Regular", 30 * -1)
    )

    button_image_2 = PhotoImage(    #submit button
        file=relative_to_assets("button_2.png"))
    button_2 = Button(window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Label(window,text=ml.CryptoFiat(clicked.get(),clicked1.get(),entry_1.get()),height=2,width=60,bg="yellow",font=("Arial", 15)).place(x=300,y=412.0),
        relief="flat"
    )
    button_2.place(
        x=859.0,
        y=499.0,
        width=199.0,
        height=90.0
    )

    canvas.create_text(
        25.0,
        412.0,
        anchor="nw",
        text="RESULT:",
        fill="#FFFFFF",
        font=("Nunito ExtraBold", 32 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        454.5,
        371.0,
        image=entry_image_1
    )
    entry_1 = Entry(window,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=25.0,
        y=347.0,
        width=859.0,
        height=46.0
    )

    canvas.create_text(
        31.0,
        119.45834350585938,
        anchor="nw",
        text="SELECT CRYPTOCURRENCY:",
        fill="#FFFFFF",
        font=("Nunito Regular", 30 * -1)
    )

    clicked=StringVar()
    clicked.set("SELECT CRYPTO")
    drop=OptionMenu(window,clicked,"Bitcoin","Ethereum","Tether","Litecoin","Dogecoin","Cardano","Solana","AAVE")
    drop.place(x=475,y=119.45834350585938)
    drop.config(width=40,bg="yellow",fg="black",font=('Helvetica'))

    canvas.create_text(
        25.0,
        208.0,
        anchor="nw",
        text="SELECT FIAT CURRENCY:",
        fill="#FFFFFF",
        font=("Nunito Regular", 30 * -1)
    )

    clicked1=StringVar()
    clicked1.set("SELECT FIAT")
    drop1=OptionMenu(window,clicked1,"US Dollar","Indian Rupees","European Euro","Great Britain Pound","Russian Rubble","Israeli Shekel","Chinese Yuan","Japanese Yen","Korean Won","Singapore Dollar","Mexican Peso")
    drop1.place(x=475,y=208.0)
    drop1.config(width=40,bg="yellow",fg="black",font=('Helvetica'))


    window.resizable(False, False)
    window.mainloop()
