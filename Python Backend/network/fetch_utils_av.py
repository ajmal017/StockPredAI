from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.timeseries import TimeSeries

# pip install alpha_vantage
ALPHA_VANTAGE_API_KEY = "ZPZSDRIOX1MCVZW7"


def fetch_stock_data(symbol):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format="pandas")
    data, meta_data = ts.get_intraday(
        symbol=symbol, interval="1min", outputsize="full")
    return data


def fetch_forex_data(from_symbol, to_symbol):
    cc = ForeignExchange(key=ALPHA_VANTAGE_API_KEY, output_format="pandas")
    data, meta_data = cc.get_currency_exchange_intraday(
        from_symbol=from_symbol, to_symbol=to_symbol, interval="1min", outputsize="full")
    return data
