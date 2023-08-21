import requests
import Symbols as sc
import Graph as g
from pycoingecko import CoinGeckoAPI
from tkinter import *
cg = CoinGeckoAPI()                                                    #creating object of wrapper class 

def isfloat(n):                                                        #checks if ans is float if error encountered then false is returned
    try:
        float(n)
        return True
    except ValueError:
        return False

#crypto to fiat conversion
def CryptoFiat(fromc,tof,amt):
   if not isfloat(amt):
      return "ERROR, Enter a valid amount."
   newc=sc.cryptolist(fromc)                                             #formatting input for API
   newf=sc.fiatlist(tof)
   conv=cg.get_price(ids=[newc], vs_currencies=newf)                    #conv-master dictionary, cg- object to acccess fn from wrapper class
   result=conv[newc][newf]*float(amt)                                   #unit currency*amount
   return result


#fiat to crypto conversion
def Fiatcrypto(fromc,tof,amt1):
   if not isfloat(amt1):
      return "ERROR, Enter a valid amount."
   newc=sc.cryptolist(fromc)
   newf=sc.fiatlist(tof)
   conv=cg.get_price(ids=[newc], vs_currencies=newf)
   result=float(amt1)/conv[newc][newf]
   return result

#Historical trades
#g.histrades(dayss)

#top 7 trending
def trending(n):
  tr=cg.get_search_trending()                                                              #master dictionary
  lt=tr["coins"]                                                                           #accessing the coins and its properties
  i=0
  while i < n:
     yield lt[i]["item"]["name"], lt[i]["item"]["symbol"],lt[i]["item"]["market_cap_rank"],lt[i]["item"]["price_btc"] #generator
     i=i+1

#Crypto trades volume in terms of bitcoin
def CryptoVol(fromc): 
  symbc=sc.tradeslist(fromc)+sc.tradeslist("Bitcoin")                       #API needs format: ETHBTC
  query_param1={"symbol":symbc}                                             #parameter which specifies the coin whose info we require
  response1=requests.get("https://data.binance.com/api/v3/ticker/price",params=query_param1).json()
  query_param2={"symbol":symbc}
  response=requests.get("https://data.binance.com/api/v3/ticker/24hr",params=query_param2).json()
  return response1["price"], response["priceChange"],response["priceChangePercent"],response["lastPrice"],response["lastQty"]

#Information about crypto
def info(infocrypto):
    coin=sc.infolist(infocrypto)
    query_param4={"coin_id":coin}
    infoc=requests.get("https://api.coinpaprika.com/v1/coins/"+coin+"/",params=query_param4).json()
    return infoc["name"],infoc["symbol"],infoc["description"],infoc["hash_algorithm"],infoc["started_at"],infoc["org_structure"],infoc["logo"]
    

