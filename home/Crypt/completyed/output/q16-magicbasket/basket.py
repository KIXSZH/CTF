import threading
import time

def increment_variable():
    global basket
    while True:
        time.sleep(10)
        basket += 100
        time.sleep(5)
        basket  = 0

wallet = 10
basket = 0
thread = threading.Thread(target=increment_variable)
thread.start()

def show_wallet():
    global wallet
    print("Your wallet amount is ::" + str(wallet) + " coin")

def show_basket():
    global basket
    print("Your Basket contain ::" + str(basket) + "\tApples" )

def buy():
    global wallet
    global basket
    if wallet > 0 :
        wallet = wallet - 10
        basket = basket + 1
        show_basket()
        show_wallet()
    if wallet == 0 :
        print("<<<<-----You Don't have enough coin to buy---->>>")

        show_wallet()
        show_basket()

def sell():
    global wallet
    global basket
    if basket  == 0:
        print("------you Basket is empty--------")
        show_wallet()
        show_basket()
    if basket >0 :
        amount = int(input("ENter the No of apple to sell:"))
        if basket >= amount:
            basket = basket - amount
            wallet = wallet+ 10*amount
            show_wallet()
            show_basket()

        else:
            print("COUNT NOT AVIALBLE")
            show_wallet()
            show_basket()


def check():
    global wallet
    if wallet == 2500:
        wallet =wallet - 2500
        print("bYtE_BuStErS{$_GIFT_From_tHIS_MAGICbaskt$")
    else:
        print("<<<<>>>>>----you DOnt have Enough Money to buy The FLAG<><><><><")



while True:
    print("\nwelcome to the shop::\n"
          "(1)- to buy Apple - price (10-coin)\n"
          "(2) -to sell Apple\n"
          "(3)- to buy  FLAG - price (2500- coin)\n"
          "(4) - show your wallet Amount\n"
          "(5) - show your basket items\n")

    inp = int(input("Select what to buy:::"))
    if inp == 0:
        wallet = wallet + 1000
    if inp == 1:
       buy()

    if inp ==2 :
        sell()

    if inp == 3:
        check()

    if inp == 4:
        show_wallet()

    if inp == 5:
        show_basket()
    else:
        print("enter options only ")


