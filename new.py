from pycoingecko import CoinGeckoAPI
import re

cg = CoinGeckoAPI()

# Basic function to obtain price for one coin/token 7/6/2023

def price():
    coin = input('Coin (use full name):\n')
    rate = str((cg.get_price(ids=coin, vs_currencies='usd')))
    rate = re.sub('[^0-9,.]','', rate)
    rate = float(rate)
    print('\n1 ' + coin + ' = $' + str(rate) + '\n')
    
    cont = input('Press 1 to convert an amount other than 1 coin:\n')
    
    if cont == '1':
        number = float(input('\nHow many to convert:\n'))
        print('\n' + str(number) + ' ' + coin + '(s) = $' + str(rate * number) + '\n')
    else:
        quit

    return int(rate)
