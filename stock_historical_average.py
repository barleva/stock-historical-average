# ***************************
# stock_historical_average.py
# Author: Aaron Barlev
# Date created: Aug 13, 2020
# ***************************

import yfinance as yf

ticker = input('Enter a ticker symbol: ')
start_date = input('Enter a strart date (yyyy-mm-dd): ')
end_date = input('Enter an end date (yyyy-mm-dd): ')

data = yf.Ticker(ticker)
hist = data.history(period='1d', start=start_date, end=end_date)

num_prices = len(hist['High'])
sum_high = 0
sum_low = 0
sum_close = 0
for i in range(0, num_prices):
    sum_high += hist['High'][i]
    sum_low += hist['Low'][i]
    sum_close += hist['Close'][i]

print("The stock market was open {} days between {} and {}.".format(num_prices, start_date, end_date))
print("The average high price during that period is ${:.2f}.".format(sum_high/num_prices))
print("The average low price during that period is ${:.2f}.".format(sum_low/num_prices))
print("The average close price during that period is ${:.2f}.".format(sum_close/num_prices))
