import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
from ib_insync import IB, Stock , MarketOrder

# --------------------------------------------------------------------------------------------
#                                         THE ALGORITHM
# --------------------------------------------------------------------------------------------

# URL of the Wikipedia page with S&P 500 tickers
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the S&P 500 tickers
table = soup.find('table', {'class': 'wikitable'})

# Extract the tickers
tickers = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all('td')
    ticker = cells[0].get_text(strip=True)
    tickers.append(ticker)

pe_ratios = {}

# Loop over each ticker to fetch its P/E 
for ticker_symbol in tickers:
    stock = yf.Ticker(ticker_symbol)
    pe_ratio = stock.info.get('trailingPE')

    if pe_ratio is not None:
        if pe_ratio <= 20:
            pe_ratios[ticker_symbol] = pe_ratio
    

ps_ratios = {}

# Loop over each ticker to fetch its P/S ratio 
for ticker_symbol in pe_ratios.keys():
    stock = yf.Ticker(ticker_symbol)
    ps_ratio = stock.info.get('priceToSalesTrailing12Months')  

    if ps_ratio is not None:
        ps_ratios[ticker_symbol] = ps_ratio
        #print(ps_ratios)

# get the lowest 10% P/S ratio 
lowest_ps_ratios = dict(sorted(ps_ratios.items(), key=lambda item: item[1])[:50])
#here you should add more restriction for the program to perform better
final_tickers = lowest_ps_ratios
# --------------------------------------------------------------------------------------------
#                           buying the stocks (this is optinal)
# --------------------------------------------------------------------------------------------


# Connect to IB
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1) # for each one is own private info

# Define a stock and order
stock = Stock(final_tickers)
order = MarketOrder('BUY', 10)  # Buy 10 shares

# Place the order
trade = ib.placeOrder(stock, order)

# Print the order status
print(trade.orderStatus.status)

# Disconnect
ib.disconnect()


# --------------------------------------------------------------------------------------------
#                           sending telegram chat with summery of each stock info
# --------------------------------------------------------------------------------------------
def send_telegram_message(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")

bot_token = '7444315736:AAERueEuaQB41PxqjSZCbw3SPZiY19zw_PA'       # Replace with your bot token
chat_id = '833689584'           # Replace with your chat ID
message = 'This is another test message.'
send_telegram_message(bot_token, chat_id, message)


for ticker in final_tickers:
    stock = yf.Ticker(ticker)
    message = ticker
    send_telegram_message(bot_token, chat_id, message)
    sector = stock.info.get('sector')
    send_telegram_message(bot_token, chat_id, sector)
    market_cap = stock.info.get('marketCap')
    send_telegram_message(bot_token, chat_id, market_cap)
    business_summary = stock.info.get('longBusinessSummary')
    send_telegram_message(bot_token, chat_id, business_summary)

