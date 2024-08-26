
# **Stock Market Analysis and Trading Bot**

This project is a Python-based stock market analysis and trading bot that automatically selects stocks based on certain criteria and then optionally places orders through Interactive Brokers (IB). It also sends detailed summaries of the selected stocks via Telegram.

## **Table of Contents**

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)

## **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/stock-trading-bot.git
   cd stock-trading-bot
   ```

2. **Install the required Python libraries:**

   ```bash
   pip install -r requirements.txt
   ```

   If you encounter issues with the installation, ensure you have Python 3.6+ installed.

3. **Set up Interactive Brokers (IB):**
   - Install [IB Gateway](https://www.interactivebrokers.com/en/index.php?f=16457) and set up your account.
   - Ensure that your IB Gateway is running, and note the `IP`, `Port`, and `Client ID` for connecting the bot.

## **Features**

- **Stock Selection:**
  - Fetches the list of S&P 500 companies from Wikipedia.
  - Filters stocks based on their Price-to-Earnings (P/E) ratio (≤ 20).
  - Further filters stocks based on their Price-to-Sales (P/S) ratio and selects the lowest 50.
  
- **Automated Trading (Optional):**
  - Connects to Interactive Brokers to automatically place buy orders for selected stocks.
  
- **Telegram Notifications:**
  - Sends detailed summaries of each selected stock, including sector, market cap, and business summary, to a specified Telegram chat.

## **Usage**

1. **Run the algorithm:**

   After configuring the settings, run the script:

   ```bash
   python main.py
   ```

2. **View Telegram Messages:**
   - You will receive notifications about the selected stocks via your specified Telegram bot.

3. **Automated Trading (Optional):**
   - If you choose to enable it, the bot will automatically place buy orders through your Interactive Brokers account.

## **Configuration**

1. **Interactive Brokers (IB):**
   - Update the connection details (`IP`, `Port`, `Client ID`) in the script where the IB connection is established.

2. **Telegram Bot:**
   - Replace `bot_token` and `chat_id` in the script with your own Telegram bot's token and your chat ID.

## **Project Structure**

```
├── main.py                # Main script that runs the bot
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## **Dependencies**

- `yfinance` - For fetching stock data from Yahoo Finance.
- `requests` - For making HTTP requests.
- `BeautifulSoup` - For parsing HTML and extracting data.
- `pandas` - For handling tabular data.
- `ib_insync` - For interacting with Interactive Brokers.
- `telegram` - For sending messages via Telegram.

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
