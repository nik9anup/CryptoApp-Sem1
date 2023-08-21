def tradeslist(symb): #Trades list
    return {'Tron':'TRX',
    'Bitcoin':'BTC',
    'Ethereum':'ETH',
    'XRP':'XRP',
    'Solana':'SOL',
    'Litecoin':'LIT',
    'Dogecoin':'DOGE',
    'Cardano':'ADA',
    'AAVE':'AAVE'
    }[symb] 
def cryptolist(symb): #conversion
    return {'Bitcoin':'bitcoin',
    'Ethereum':'ethereum',
    'Tether':'tether',
    'Solana':'solana',
    'Litecoin':'litecoin',
    'Dogecoin':'dogecoin',
    'Cardano':'cardano',
    'AAVE':'aave'
    }[symb]
def infolist(symb):
    return {'Bitcoin':'btc-bitcoin',
    'Ethereum':'eth-ethereum',
    }[symb]
def fiatlist(symb): #conversion
    return {'US Dollar':'usd',
    'Indian Rupees':'inr',
    'European Euro':'eur',
    'Great Britain Pound':'gbp',
    'Russian Rubble':'rub',
    'Israeli Shekel':'ils',
    'Chinese Yuan':'cny',
    'Japanese Yen':'jpy',
    'Korean Won':'krw',
    'Singapore Dollar':'sgd',
    'Mexican Peso':'mxn'
    }[symb]

