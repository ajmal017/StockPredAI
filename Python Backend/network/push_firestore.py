# pip install firebase-admin
from firebase_admin import credentials, firestore, initialize_app


def push_stocks_data(stock_symbols, stocks):
    cred = credentials.Certificate("./ServiceAccountKey.json")
    initialize_app(cred)
    store = firestore.client()

    stocks_dict = {}
    for i in range(len(stocks)):
        symbol = stock_symbols[i]
        if symbol not in stocks_dict:
            stocks_dict[symbol] = {}
        for key in stocks[i]:
            stocks_dict[symbol][key] = stocks[i][key].values.tolist()

    doc_ref = store.collection(u'stocks')
    doc_ref.document('data').set(stocks_dict)
