package com.makuhita.StockPredAI.entities

class Stock {
    var symbol: String = ""
    var price: Double = 0.0
    var estimate: Double = 0.0
    var prices: List<Price> = emptyList()
    override fun toString(): String {
        return "Stock(symbol='$symbol', price=$price, estimate=$estimate, prices=$prices)"
    }
}