from pycoingecko import CoinGeckoAPI
import re

cg = CoinGeckoAPI()

print(
"""___________________________________________________________

********                 ***    ***  **********  **********             
***  ***                  ***   **      ***      ***    ***
***      ***  **  ***  **  *** **       ***      **********     
***  *** * *  **  ** * **   ****        ***      ***  ***    
******** ***  **  **  ***    **         ***      ***   ****    
___________________________________________________________
""")

#Function to print price of 1 coin/token.
def simple_price():
    coin = str(input("Coin name?\n"))
    price = str((cg.get_price(ids=coin, vs_currencies='usd')))
    price = re.sub("[^0-9,.]", "", price)
    price = float(price)
    print("\n1 " + coin + " = $" + str(price))
    
    def multiple_coins(coin, price):
        #Prompt user for number of coins to convert
        amount = float(input("\nHow many to convert?"))
        #Print conversion in USD
        print("\n" + str(amount) + " " + coin + "s" " = $" + str(price * amount))

    calculate = input("Do you want the price of an amount other than 1 coin? (y/N)")
    if calculate == "y" or calculate == "Y":
        multiple_coins(coin, price)
    else:
        calculate = 0

#Function to convert 1 coin/token to another
def convert():
    # Prompt user for coin pair
    coin1 = input("Coin 1? (use full name)")
    coin2 = input("Coin 2? (use full name)")
    # Call CoinGecko API for price information
    usd1 = str((cg.get_price(ids=coin1, vs_currencies='usd')))
    usd2 = str((cg.get_price(ids=coin2, vs_currencies='usd')))
    # Limit API response to chars 0-9 and convert to float
    price1 = float(re.sub('[^0-9,.]', '', usd1))
    price2 = float(re.sub('[^0-9,.]', '', usd2))
    # Calculate conversion rates w/ only 4 spaces after decimal
    conv = "{:.4} ".format(float(price1 / price2))
    conv2 = "{:.4f} ".format(float(price2 / price1))
    # Display conversion rates
    print("\n1 " + coin1 + " equals " + str(conv) + coin2 + ".")
    print("\n1 " + coin2 + " equals " + str(conv2) + coin1 + ".")

def return_on_investment():
    #select = input("Calculate based on purchase date or purchase price?")
    choice = str(input("Calculate based on coin name and date(n) or purchase price (p)?\n"))
    
    if 'n' in choice:
        coin = str(input("Coin name?\n"))
        purchase_date = input("Please enter purchase date (DD-MM-YYYY)\n")
        history = cg.get_coin_history_by_id(id= coin, date = purchase_date)
        #gets token price in US dollars on specified data 
        historic_price = float(history['market_data']['current_price']['usd'])
        #historic_price = re.sub("[^0-9,.]", "", historic_price)
        current_price = str((cg.get_price(ids=coin, vs_currencies='usd')))
        current_price = re.sub("[^0-9,.]", "", current_price)
        current_price = float(current_price)
        roi = "{:.4} ".format(((current_price - historic_price) / historic_price) * 100)
        print("\nYour ROI is " + str(roi) + " %")

    elif 'p' in choice:
        purchase_price = float(input("Purchase price?"))
        current_price = float(input("Current price?"))
        #current_price = str((cg.get_price(ids=coin, vs_currencies='usd')))
        #current_price = re.sub("[^0-9,.]", "", current_price)
        #current_price = float(current_price)
        roi = ((current_price - purchase_price) / purchase_price) * 100
        print("\nYour ROI is " + str(roi) + " %") 

    dollars_spent = float(input("How much $USD was spent on your purchase"))
    current_value = (dollars_spent * roi) + dollars_spent

def compare():
    coin1 = input("\nCoin 1? (use full name)")
    coin2 = input("\nCoin 2? (use full name)")
    # Display API response with no formatting
    print()
    print(cg.get_price(ids=coin1, vs_currencies='usd'))
    print()
    print(cg.get_price(ids=coin2, vs_currencies='usd'))

def trendy():
    #Use API to find trending coins, formatted as a dict - set to x
    x = cg.get_search_trending()
    #Initialize counter and print out trending coin's names 
    p = 0
    for i in range(0, 6):
        while p != 7:
            print(x['coins'][p]['item']['name'], end = '  |  ')
            p +=1

def main_menu():
    selection = input("\nPress 1 - PRINT CURRENT PRICE OF ONE COIN/TOKEN IN USD.\n"
                          "\nPress 2 - CONVERT BETWEEN COINS.\n"
                          "\nPress 3 - CALCULATE YOUR RETURN ON INVESTMENT.\n"
                          "\nPress 4 - VIEW PRICE INFORMATION OF 2 COINS.\n"
                          "\nPress 5 - SEE WHICH COINS ARE TRENDING.\n"
                          "\nPress 5 - CLOSE COINVERTER.\n")
    selection = int(selection)

    if selection == 1:
        simple_price()
    elif selection == 2:
        convert()
    elif selection == 3:
        return_on_investment()
    elif selection == 4:
        compare()
    elif selection == 5:
        trendy()
    elif selection == 6:
        quit()

x = 1
while x == 1:
    main_menu()