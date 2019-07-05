package com.makuhita.StockPredAI.entities

class Stock {
    val symbol: String = ""
    val price: Double = 0.0
    val estimate: Double = 0.0
    val earning: Double = 0.0
    val prices: List<Price> = emptyList()
    override fun toString(): String {
        return "Stock(symbol='$symbol', price=$price, estimate=$estimate, earning=$earning, prices=$prices)"
    }
}