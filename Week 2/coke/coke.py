amount = 50
change = 0
while True:
    print("Amount Due: " + str(amount))
    inserted_coin = int(input("Insert Coin: "))
    while inserted_coin not in [25,10,5]:
        print("Amount Due: " + str(amount))
        inserted_coin = int(input("Insert Coin: "))
    amount -= inserted_coin
    if amount == 0 :
        print("Amount Due: " + str(amount))
        print("Change Owed: "+ str(change))
        break
    elif amount < 0:
        change = abs(amount)
        print("Change Owed: "+ str(change))
        break
