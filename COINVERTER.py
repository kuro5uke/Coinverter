from pycoingecko import CoinGeckoAPI
import datetime, os
cg = CoinGeckoAPI()

print ("""COINVERTER v.01\n 
A Program for Crypto Enthusiasts and the Curious\n
-------------------------------------------------\nwritten in Python by civilkmkz. \n
Tips Accepted... CashApp $340kil""")

#time = datetime.datetime.now()
#print(time) 

def usd():

    #API PULLS COIN PRICE IN DOLLARS
    coin=str(input("\nCoin? (use full name please) "))
    print(cg.get_price(ids=coin, vs_currencies='usd'))

    #ASKS USER FOR CURRENT COIN PRICE
    price = float(input("\nCurrent price? (use the number above)"))

    #CALCULATES PRICE OF $1.00 AS A FLOAT
    usd = float(1/price)
    print("\n1 USD = " + "{:.8f} ".format(float(usd)) + coin + ".")

    #ASKS USER FOR AMOUNT OF US DOLLARS
    amount = int(input("\nHow much US Dollars to convert? "))
    conv = "{:.8f} ".format(float(amount * usd))

    print("$" + str(amount) + " USD equals " + str(conv) + coin + ".")

def compare():
    coin1=str(input("\nCoin 1? (use full name please) "))
    coin2=str(input("\nCoin 2? (use full name please) "))
    print(cg.get_price(ids=coin1, vs_currencies='usd'))
    print(cg.get_price(ids=coin2, vs_currencies='usd'))

def convert():
    coin1=str(input("\nCoin 1? (use full name please) "))
    coin2=str(input("\nCoin 2? (use full name please) "))
    print(cg.get_price(ids=coin1, vs_currencies='usd'))
    print(cg.get_price(ids=coin2, vs_currencies='usd'))
    price1 = float(input("\nCoin 1 Current price? (use the number above)"))
    usd1 = float(1/price1)
    price2 = float(input("\nCoin 2 Current price? (use the number above)"))
    usd2 = float(1/price2)
    
    conv = "{:.8f} ".format(float(price1 / price2))
    print("1 " + coin1 + " equals " + str(conv) + coin2 + ".")

def main():
   init = int(input("\nPress 1 to convert coin to US Dollars.\nPress 2 to exit.\nPress 3 to compare 2 coins.\nPress 4 to convert between coins."))
   if init ==1:
       usd()

   elif init ==2:
        quit()

   elif init ==3:
       compare()

   elif init ==4:
       convert()

x = 1
while x ==1:
    main()
