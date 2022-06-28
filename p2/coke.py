coins = [5, 10, 25]
amount_due = 50


while True:
    if amount_due <= 0:
        print(f"Change owed: {abs(amount_due)}")
        break
    else:
        print(f"Amount due: {amount_due}")
        coin = int(input("Enter coin: "))
        if coin in coins:
            amount_due -= coin
