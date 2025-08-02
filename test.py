# Say you have an array for which the ith element is the price of a given stock on day i , and if you were permitted to complete only one transaction , 

# design an algorithm to find the maximum profit.
 
# You always need to buy a stock before you sell one.
 
# [7, 1, 5, 3, 6, 4] -- prices on every single day
 
stock = [7, 1, 5, 3, 6, 4]
profit = []
def decide_stock_operation(stock):
    prev_val = 0
    prof_val = 0
    for s in stock:
        purchase_prc = s - prev_val
        print(f"Purchase Price is:{purchase_prc}")
        if s <= purchase_prc:
            print("Buy the stock")
            prof_val = s - purchase_prc
            profit.append(prof_val)
        if s > purchase_prc:
            print("Sale the stock")
            prof_val = s - purchase_prc
            profit.append(prof_val)
        prev_val = s
    return profit
price_of_stocks = decide_stock_operation(stock=stock)


