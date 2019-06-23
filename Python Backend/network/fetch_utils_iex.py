import pandas as pd

IEX_PUBLISHABLE = "pk_56a2605e39894a40974e68ccbd7de629"
IEX_SECRET = "sk_ff5d8a9b811f4aa5ae03891b6b56f6e8"


def fetch_stock_data(symbol):
    df_temp = pd.read_json('https://cloud.iexapis.com/stable/stock/' +
                           symbol+'/chart/date/20190220?token='+IEX_PUBLISHABLE+'')
    df_temp.set_index('date', inplace=True)
    data = df_temp[['open', 'high', 'low', 'close', 'volume']]
    return data


def fetch_forex_data(from_symbol, to_symbol):
    return "implement me"


print("Fetching new data...")
#in_amzn = fetch_stock_data("AMZN")
in_appl = fetch_stock_data("TSLA")
#in_intc = fetch_stock_data("INTC")

#in_eur_usd = fetch_forex_data("EUR", "USD")

# print(in_eur_usd)

# print(len(in_amzn))
print(in_appl)
# print(len(in_intc))

# print(len(in_eur_usd))
