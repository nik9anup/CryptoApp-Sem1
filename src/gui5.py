

def OpenWindow(master):

    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, OptionMenu, StringVar,Label,Toplevel

    window=Toplevel(master)
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Nikita\APYTHON\ProjectCrypto\build\assets\frame5")


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

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=window.withdraw, #homebutton
        relief="flat"
    )
    button_1.place(
        x=858.0,
        y=34.0,
        width=155.0,
        height=66.0
    )
    def Labels():
        labela=Label(window,text="Price: ",height=2,width=60,bg="yellow").place(x=180,y=200)
        label1=Label(window,text=ml.CryptoVol(clicked.get())[0],bg="yellow",height=2,width=60).place(x=450,y=200)
        
        labelb=Label(window,text="Price Change: ",bg="yellow",height=2,width=60).place(x=180,y=250)
        label2=Label(window,text=ml.CryptoVol(clicked.get())[1],bg="yellow",height=2,width=60).place(x=450,y=250)
        
        labelc=Label(window,text="Price change %: ",bg="yellow",height=2,width=60).place(x=180,y=300)
        label3=Label(window,text=ml.CryptoVol(clicked.get())[2],bg="yellow",height=2,width=60).place(x=450,y=300)

        labeld=Label(window,text="Last Price: ",bg="yellow",height=2,width=60).place(x=180,y=350)
        label4=Label(window,text= ml.CryptoVol(clicked.get())[3],bg="yellow",height=2,width=60).place(x=450,y=350)

        labele=Label(window,text="Last Quantity:",bg="yellow",height=2,width=60).place(x=180,y=400)
        label5=Label(window,text= ml.CryptoVol(clicked.get())[4],bg="yellow",height=2,width=60).place(x=450,y=400)

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=Labels, #submit button
        relief="flat"
    )
    button_2.place(
        x=858.0,
        y=504.0,
        width=153.0,
        height=67.0
    )

    canvas.create_text(
        25.0,
        214.0,
        anchor="nw",
        text="RESULT:",
        fill="#FFFFFF",
        font=("Nunito ExtraBold", 32 * -1)
    )

    canvas.create_text(
        24.50927734375,
        106.41110229492188,
        anchor="nw",
        text="SELECT CRYPTOCURRENCY:",
        fill="#FFFFFF",
        font=("Nunito Regular", 32 * -1)
    )

    clicked=StringVar()
    clicked.set("SELECT CRYPTO")
    drop=OptionMenu(window,clicked,"Tron","Ethereum","XRP","Litecoin","Dogecoin","Cardano","Solana","AAVE")
    drop.place(x=490,y=106.41110229492188)
    drop.config(width=40,bg="yellow",fg="black")

    window.resizable(False, False)
    window.mainloop()
