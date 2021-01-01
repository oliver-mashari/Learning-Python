stock_prices = [('Apple',50), ('Google',500), ('Samsung',200)]

# Check who has the best stock prices 
def company_check(stock_prices):
    
    # place holder and comparison variables
    current_max = 0
    top_company = ''

    for company,stock in stock_prices:
        if stock > current_max:
            current_max = stock 
            top_company = company
        else:
            pass

    return top_company, current_max

result = company_check(stock_prices)
print(result)