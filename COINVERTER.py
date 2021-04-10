from pycoingecko import CoinGeckoAPI
import re, datetime, os
cg = CoinGeckoAPI()

print ("""COINVERTER v.01\n 
A Program for Crypto Enthusiasts and the Curious\n
-------------------------------------------------\nwritten in Python by civilkmkz. \n
Tips Accepted... CashApp $civilkmkz""")

#time = datetime.datetime.now()
#print(time) 

def usd():

    coin= input("\nCoin? (use full name)\n")
    #API PULLS COIN PRICE IN DOLLARS
    usd= str(cg.get_price(ids=coin, vs_currencies='usd'))
    #OUTPUT IS LIMITED TO NUMBERS ONLY
    usd= re.sub('[^0-9,.]', '', usd)
    print(usd)

    #SETS FLOAT TO CURRENT COIN PRICE
    price = float(usd)
    #CALCULATES PRICE OF $1.00 AS A FLOAT
    usd = float(1/price)
    print("\n1 USD = " + "{:.8f} ".format(float(usd)) + coin + ".")

    #ASKS USER FOR AMOUNT OF US DOLLARS
    amount = float(input("\nHow much US Dollars to convert? "))
    conv = "{:.8f} ".format(float(amount * usd))
    print("\n$" + str(amount) + " USD equals " + str(conv) + coin + ".")

def compare():
    coin1= input("\nCoin 1? (use full name)\n")
    coin2= input("\nCoin 2? (use full name)\n")
    print(cg.get_price(ids=coin1, vs_currencies='usd'))
    print(cg.get_price(ids=coin2, vs_currencies='usd'))

def convert():
    coin1= input("\nCoin 1? (use full name)\n")
    coin2= input("\nCoin 2? (use full name)\n")

    usd1= str((cg.get_price(ids=coin1, vs_currencies='usd')))
    price1= float(re.sub('[^0-9,.]', '', usd1))#omit letters
    
    usd2= str((cg.get_price(ids=coin2, vs_currencies='usd')))
    price2= float(re.sub('[^0-9,.]', '', usd2)) #omit letters
    
    conv = "{:.8f} ".format(float(price1 / price2))
    print("\n1 " + coin1 + " equals " + str(conv) + coin2 + ".")

def main():
   init = int(input("""\nPress 1 - CONVERT COIN TO US DOLLARS.
                    \nPress 2 - CONVERT ONE COIN TO ANOTHER.
                    \nPress 3 - COMPARE TWO COINS.
                    \nPress 4 - EXIT."""))
   if init ==1:
       usd()
   elif init ==2:
        convert()
   elif init ==3:
       compare()
   elif init ==4:
       quit()

x = 1
while x ==1:
    main()
