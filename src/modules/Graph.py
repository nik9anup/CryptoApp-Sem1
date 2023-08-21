import matplotlib.pyplot as plt
from tkinter import *
import requests
import Symbols as sc
#crypto to fiat
from pycoingecko import CoinGeckoAPI
import numpy as np
cg = CoinGeckoAPI()
# x axis values


# corresponding y axis values
x=[]
y=[]


def plotnow(xl):
# plotting the points
     plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=12)

# setting x and y axis range
     plt.ylim(y[0],y[-1])
     plt.xlim(1,xl)

# naming the x axis
     plt.xlabel('Number of days')
# naming the y axis
     plt.ylabel('Cryptocurrency')

# giving a title to my graph
     plt.title('Crypto vs Days trend')

# function to show the plot
     plt.show()

def histrades(crypto,dayss):
   global x
   if not dayss.isdigit() or dayss=="0":
     root=Tk()
     root.geometry("900x300")
     Label(root,text="ERROR",height=5,width=60,bg="yellow",font=("Arial", 15)).place(x=90,y=120.0)
     root.mainloop()
     return None
   xl=int(dayss)
   x = list(range(1,xl+2))
   newc=sc.cryptolist(crypto)
   hist=cg.get_coin_market_chart_by_id(id=newc,vs_currency="usd",days=dayss,interval="daily")
   l=hist["prices"]
   for i in range (len(l)):
    y.append(l[i][1])
   plotnow(xl)
