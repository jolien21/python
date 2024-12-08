#get float input otherwise an error
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not suited value")

#define main function
def main():
    #get product price
    product_price = get_float("Product price: ")
    #get amount given and repeat
    while True:
      amount_payed = get_float("Amount given: ")
      if amount_payed >= product_price:
        break

    amount_bills = 0
    amount_coins = 0

    #calculate amount of change
    amount_change = amount_payed - product_price

    while amount_change >= 500:
        amount_change -= 500
        amount_bills += 1
    while amount_change >=100:
        amount_change -= 100
        amount_bills += 1
    while amount_change >= 50:
        amount_change -= 50
        amount_bills += 1
    while amount_change >= 20:
        amount_change -= 20
        amount_bills +=1
    while amount_change >= 10:
        amount_change -= 10
        amount_bills += 1
    while amount_change >= 5:
        amount_change -= 5
        amount_bills += 1
    while amount_change >= 2:
        amount_change -= 2
        amount_coins += 1
    while amount_change >= 1:
        amount_change -= 1
        amount_coins += 1
    while amount_change >= 0.5:
        amount_change -= 0.5
        amount_coins += 1
    while amount_change >= 0.2:
        amount_change -= 0.2
        amount_coins += 1
    while amount_change >= 0.1:
        amount_change -= 0.1
        amount_coins += 1
    while amount_change >= 0.5:
        amount_change -= 0.05
        amount_coins += 1

    print(f"amount of coins: ", amount_coins)
    print(f"amount of bills: ", amount_bills)
    
main()

