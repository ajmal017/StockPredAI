# pip install firebase-admin
from firebase_admin import credentials, firestore, initialize_app
from entities.Stock import Stock
from entities.Price import Price


def push_stocks_data(stock_symbols, stocks):
    cred = credentials.Certificate("./ServiceAccountKey.json")
    initialize_app(cred)
    store = firestore.client()

    collection = store.collection(u'stocks')

    for i in range(len(stocks)):
        symbol = stock_symbols[i]

        open = stocks[i]["open"].values.tolist()
        close = stocks[i]["close"].values.tolist()
        high = stocks[i]["high"].values.tolist()
        low = stocks[i]["low"].values.tolist()
        volume = stocks[i]["volume"].values.tolist()

        prices = []
        for j in range(len(open)):
            prices.append(Price(open[j], close[j], high[j], low[j], volume[j]).to_dict())

        stock = Stock(symbol, stocks[i]["open"].values.tolist()[0], 1, 99, prices)

        collection.document(symbol).set(stock.to_dict())