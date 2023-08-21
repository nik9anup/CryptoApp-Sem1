

def OpenWindow(master):
    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, OptionMenu, StringVar,Label,Toplevel
    window=Toplevel(master)

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Nikita\APYTHON\ProjectCrypto\build\assets\frame7")


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
        command=window.withdraw,
        relief="flat"
    )
    button_1.place(
        x=849.0,
        y=41.0,
        width=152.0,
        height=67.0
    )

    def Labels():
        labela=Label(window,text="Name: ",height=2,width=30,bg="yellow").place(x=90,y=200)
        label1=Label(window,text=ml.info(clicked.get())[0],bg="yellow",height=2,width=60).place(x=350,y=200)
        
        labelb=Label(window,text="Symbol: ",bg="yellow",height=2,width=30).place(x=90,y=250)
        label2=Label(window,text=ml.info(clicked.get())[1],bg="yellow",height=2,width=60).place(x=350,y=250)

        labeld=Label(window,text="Hash Algorithm: ",bg="yellow",height=2,width=30).place(x=90,y=300)
        label4=Label(window,text= ml.info(clicked.get())[3],bg="yellow",height=2,width=60).place(x=350,y=300)

        labele=Label(window,text="Started At:",bg="yellow",height=2,width=30).place(x=90,y=350)
        label5=Label(window,text= ml.info(clicked.get())[4],bg="yellow",height=2,width=60).place(x=350,y=350)

        labelf=Label(window,text="Organisation Structure:",bg="yellow",height=2,width=30).place(x=90,y=400)
        label6=Label(window,text= ml.info(clicked.get())[5],bg="yellow",height=2,width=60).place(x=350,y=400)

        labelg=Label(window,text="Logo:",bg="yellow",height=2,width=30).place(x=90,y=450)
        label7=Label(window,text= ml.info(clicked.get())[6],bg="yellow",height=2,width=60).place(x=350,y=450)


    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=Labels,
        relief="flat"
    )
    button_2.place(
        x=849.0,
        y=490.0,
        width=152.0,
        height=68.0
    )

    canvas.create_text(
        23.25,
        110.80078125,
        anchor="nw",
        text="SELECT CRYPTOCURRENCY:",
        fill="#FFFFFF",
        font=("Nunito Regular", 32 * -1)
    )

    clicked=StringVar()
    clicked.set("SELECT CRYPTO")
    drop=OptionMenu(window,clicked,"Bitcoin","Ethereum")
    drop.place(x=490,y=110.80078125)
    drop.config(width=40,bg="yellow",fg="black")

    window.resizable(False, False)
    window.mainloop()
